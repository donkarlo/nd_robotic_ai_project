from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from datetime import date, datetime, timedelta
from typing import List, Optional, Tuple

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QBrush, QDesktopServices
from PySide6.QtWidgets import (
    QAbstractItemView,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from nd_robotic_ai.robot.action.kind.core.kinds.repository import Repository
from nd_robotic_ai.robot.action.kind.core.kinds.time_formatter import TimeFormatter
from nd_robotic_ai.robot.action.plan.reminder.communication.interface.to_plan_tree_builder import ToPlanTreeBuilder
from nd_robotic_ai.robot.action.plan.reminder.communication.interface.ui_plan_snapshot import UiPlanSnapshot
from nd_robotic_ai.robot.action.plan.reminder.schedule.by_date_time_loader import ScheduledItem


class MainWindow(QMainWindow):
    def __init__(self, repository: Repository, time_formatter: TimeFormatter, yaml_action_kinds_file_path: Optional[str], yaml_plan_by_date_time_file_path: Optional[str], yaml_to_plan_file_path: Optional[str]) -> None:
        super().__init__()

        self._repository = repository
        self._time_formatter = time_formatter

        self._yaml_action_kinds_file_path = yaml_action_kinds_file_path
        self._yaml_plan_by_date_time_file_path = yaml_plan_by_date_time_file_path
        self._yaml_to_plan_file_path = yaml_to_plan_file_path

        self._snapshot: Optional[UiPlanSnapshot] = None
        self._spoken_today_marker: Optional[date] = None

        self._root = QWidget()
        self.setCentralWidget(self._root)

        root_layout = QHBoxLayout(self._root)

        # Left: By date/time
        left_box = QGroupBox("By date & time")
        left_layout = QVBoxLayout(left_box)

        left_controls = QHBoxLayout()
        self._edit_by_date_time_button = QPushButton("Edit file")
        left_controls.addWidget(self._edit_by_date_time_button)
        left_controls.addStretch(1)
        left_layout.addLayout(left_controls)

        self._left_tree = QTreeWidget()
        self._left_tree.setColumnCount(2)
        self._left_tree.setHeaderLabels(["When", "Title"])
        self._left_tree.setSelectionMode(QAbstractItemView.SingleSelection)
        self._left_tree.setTextElideMode(Qt.ElideNone)
        self._left_tree.header().setStretchLastSection(True)
        left_layout.addWidget(self._left_tree)

        # Middle: Kinds
        right_box = QGroupBox("Kinds")
        right_layout = QVBoxLayout(right_box)

        right_controls = QHBoxLayout()
        self._edit_kinds_button = QPushButton("Edit file")
        right_controls.addWidget(self._edit_kinds_button)
        right_controls.addStretch(1)
        right_layout.addLayout(right_controls)

        self._status_label = QLabel("Idle")
        right_layout.addWidget(self._status_label)

        self._kinds_tree = QTreeWidget()
        self._kinds_tree.setColumnCount(3)
        self._kinds_tree.setHeaderLabels(["Title", "Remaining", "Control"])
        self._kinds_tree.setSelectionMode(QAbstractItemView.NoSelection)
        self._kinds_tree.setTextElideMode(Qt.ElideNone)
        self._kinds_tree.header().setStretchLastSection(False)
        self._kinds_tree.header().setSectionResizeMode(0, self._kinds_tree.header().ResizeMode.Stretch)
        self._kinds_tree.header().setSectionResizeMode(1, self._kinds_tree.header().ResizeMode.ResizeToContents)
        self._kinds_tree.header().setSectionResizeMode(2, self._kinds_tree.header().ResizeMode.ResizeToContents)

        right_layout.addWidget(self._kinds_tree)

        # Right: To plan
        to_plan_box = QGroupBox("To plan")
        to_plan_layout = QVBoxLayout(to_plan_box)

        controls_row = QHBoxLayout()
        self._edit_to_plan_button = QPushButton("Edit file")
        controls_row.addWidget(self._edit_to_plan_button)
        self._to_plan_expand_all = QPushButton("Expand all")
        self._to_plan_collapse_all = QPushButton("Close all")
        controls_row.addWidget(self._to_plan_expand_all)
        controls_row.addWidget(self._to_plan_collapse_all)
        controls_row.addStretch(1)
        to_plan_layout.addLayout(controls_row)

        self._to_plan_tree = QTreeWidget()
        self._to_plan_tree.setColumnCount(2)
        self._to_plan_tree.setHeaderLabels(["Item", "Value"])
        self._to_plan_tree.setSelectionMode(QAbstractItemView.SingleSelection)
        self._to_plan_tree.setTextElideMode(Qt.ElideNone)
        self._to_plan_tree.header().setStretchLastSection(True)
        to_plan_layout.addWidget(self._to_plan_tree)

        self._to_plan_expand_all.clicked.connect(self._to_plan_tree.expandAll)
        self._to_plan_collapse_all.clicked.connect(self._to_plan_tree.collapseAll)
        self._to_plan_tree.itemActivated.connect(self._on_to_plan_item_activated)

        self._edit_by_date_time_button.clicked.connect(lambda: self._open_in_pycharm(self._yaml_plan_by_date_time_file_path))
        self._edit_kinds_button.clicked.connect(lambda: self._open_in_pycharm(self._yaml_action_kinds_file_path))
        self._edit_to_plan_button.clicked.connect(lambda: self._open_in_pycharm(self._yaml_to_plan_file_path))

        root_layout.addWidget(left_box, 1)
        root_layout.addWidget(right_box, 1)
        root_layout.addWidget(to_plan_box, 1)

        self._repository.state_changed.connect(self.refresh_right)
        self._repository.ticked.connect(self.refresh_right)

        self.setWindowTitle("Reminder")
        self.resize(1200, 750)

    def set_snapshot(self, snapshot: UiPlanSnapshot) -> None:
        self._snapshot = snapshot
        self.refresh_left()
        self.refresh_right()
        self.refresh_to_plan()

    def refresh_to_plan(self) -> None:
        if self._snapshot is None:
            return

        self._to_plan_tree.clear()

        data = self._snapshot.to_plan
        if data is None:
            return

        builder = ToPlanTreeBuilder()
        top_items = builder.build_top_level_items(data)

        for item in top_items:
            self._to_plan_tree.addTopLevelItem(item)

        # Ensure nothing is expanded by default
        self._to_plan_tree.collapseAll()
        for i in range(self._to_plan_tree.topLevelItemCount()):
            self._to_plan_tree.topLevelItem(i).setExpanded(False)

    def _on_to_plan_item_activated(self, item: QTreeWidgetItem, column: int) -> None:
        text = item.text(1).strip()
        if text == "":
            return

        url = self._normalize_url(text)
        if url is None:
            return

        QDesktopServices.openUrl(QUrl(url))

    def _normalize_url(self, text: str) -> Optional[str]:
        lowered = text.lower()
        if lowered.startswith("http://") or lowered.startswith("https://"):
            return text
        if lowered.startswith("www."):
            return "https://" + text
        if "amazon." in lowered and lowered.startswith("amazon."):
            return "https://" + text
        if "amazon." in lowered and lowered.startswith("www.amazon."):
            return "https://" + text
        return None

    def _open_in_pycharm(self, file_path: Optional[str]) -> None:
        if file_path is None:
            self._status_label.setText("No file path configured")
            return

        path = Path(str(file_path))
        if not path.exists():
            self._status_label.setText(f"File not found: {path}")
            return

        candidates = ["charm", "pycharm", "pycharm.sh"]
        command = None
        for candidate in candidates:
            resolved = shutil.which(candidate)
            if resolved is not None:
                command = [resolved, str(path)]
                break

        if command is None:
            resolved = shutil.which("xdg-open")
            if resolved is not None:
                command = [resolved, str(path)]

        if command is None:
            self._status_label.setText("No launcher found (charm/pycharm/xdg-open)")
            return

        try:
            subprocess.Popen(command)
            self._status_label.setText(f"Opened: {path.name}")
        except Exception as ex:
            self._status_label.setText(f"Open failed: {ex}")

    def refresh_left(self) -> None:
        if self._snapshot is None:
            return

        self._left_tree.clear()

        today = datetime.now().date()
        past_days = 3
        future_days = 4

        start_day = today - timedelta(days=past_days)
        total_days = past_days + 1 + future_days
        days_to_show = [start_day + timedelta(days=offset) for offset in range(total_days)]

        for the_day in days_to_show:
            day_items = self._snapshot.by_day.get(the_day, [])
            header_item = QTreeWidgetItem([the_day.isoformat(), ""])
            header_font = header_item.font(0)
            header_font.setBold(True)
            header_item.setFont(0, header_font)
            self._left_tree.addTopLevelItem(header_item)

            current_marker = self._select_current_item_for_day(the_day, day_items)

            for index, item in enumerate(self._sort_day_items_for_display(day_items)):
                when_text = item.time_raw
                if item.time_value is None:
                    when_text = "pending"
                node = QTreeWidgetItem([when_text, item.title])

                if current_marker is not None and index == current_marker:
                    self._set_item_green_bold(node)

                header_item.addChild(node)

                for child_title in item.children_titles:
                    child_node = QTreeWidgetItem(["", child_title])
                    node.addChild(child_node)

                if item.reminders:
                    reminders_node = QTreeWidgetItem(["", "reminders"])
                    node.addChild(reminders_node)
                    for rem in item.reminders:
                        rem_node = QTreeWidgetItem(["", str(rem)])
                        reminders_node.addChild(rem_node)

            header_item.setExpanded(True)

    def _sort_day_items_for_display(self, items: List[ScheduledItem]) -> List[ScheduledItem]:
        def key(x: ScheduledItem) -> Tuple[int, int, int]:
            if x.time_value is None:
                return (1, 99, 99)
            return (0, x.time_value.hour, x.time_value.minute)

        return sorted(items, key=key)

    def _select_current_item_for_day(self, the_day: date, items: List[ScheduledItem]) -> Optional[int]:
        if the_day != datetime.now().date():
            return None

        sorted_items = self._sort_day_items_for_display(items)
        now = datetime.now()

        last_past_index: Optional[int] = None
        for idx, it in enumerate(sorted_items):
            dt = it.event_datetime()
            if dt is None:
                continue
            if dt <= now:
                last_past_index = idx

        if last_past_index is not None:
            return last_past_index

        for idx, it in enumerate(sorted_items):
            dt = it.event_datetime()
            if dt is None:
                continue
            if dt > now:
                return idx

        return None

    def refresh_right(self) -> None:
        if self._snapshot is None:
            return

        self._kinds_tree.clear()

        active_state = self._repository.get_active_state()

        if active_state is None:
            self._status_label.setText("Idle")
        else:
            self._status_label.setText(f"Active: {active_state.action_title}")

        for kind in self._snapshot.kinds:
            action_item = QTreeWidgetItem([kind.title, "", ""])
            self._kinds_tree.addTopLevelItem(action_item)
            action_item.setExpanded(True)

            action_button = QPushButton()
            self._configure_button_for_action(action_button, kind_title=kind.title, child_index=None)
            self._kinds_tree.setItemWidget(action_item, 2, action_button)

            if active_state is not None and active_state.action_title == kind.title:
                self._set_item_red_bold(action_item)
                action_item.setText(1, self._time_formatter.format_compact(active_state.remaining_seconds))

            for child_index, child in enumerate(kind.children):
                child_item = QTreeWidgetItem([child.title, "", ""])
                action_item.addChild(child_item)

                child_button = QPushButton("Start")
                self._configure_button_for_action(child_button, kind_title=kind.title, child_index=child_index)
                self._kinds_tree.setItemWidget(child_item, 2, child_button)

                if active_state is not None and active_state.action_title == kind.title and active_state.child_index == child_index:
                    self._set_item_red_bold(child_item)
                    child_item.setText(1, self._time_formatter.format_compact(active_state.remaining_seconds))

    def _configure_button_for_action(self, button: QPushButton, kind_title: str, child_index: Optional[int]) -> None:
        active = self._repository.get_active_state()

        if active is None:
            button.setText("Start")
            button.clicked.connect(lambda: self._repository.start_action(kind_title, 0 if child_index is None else child_index))
            return

        if active.action_title != kind_title:
            button.setText("Start")
            button.clicked.connect(lambda: self._repository.start_action(kind_title, 0 if child_index is None else child_index))
            return

        if child_index is None:
            if active.paused:
                button.setText("Resume")
                button.clicked.connect(self._repository.resume)
            else:
                button.setText("Pause")
                button.clicked.connect(self._repository.pause)
            return

        if active.child_index == child_index:
            if active.paused:
                button.setText("Resume")
                button.clicked.connect(self._repository.resume)
            else:
                button.setText("Pause")
                button.clicked.connect(self._repository.pause)
            return

        button.setText("Start")
        button.clicked.connect(lambda: self._repository.start_action(kind_title, child_index))

    def _set_item_red_bold(self, item: QTreeWidgetItem) -> None:
        font0 = item.font(0)
        font0.setBold(True)
        item.setFont(0, font0)
        font1 = item.font(1)
        font1.setBold(True)
        item.setFont(1, font1)

        item.setForeground(0, QBrush(Qt.red))
        item.setForeground(1, QBrush(Qt.red))

    def _set_item_green_bold(self, item: QTreeWidgetItem) -> None:
        font0 = item.font(0)
        font0.setBold(True)
        item.setFont(0, font0)
        font1 = item.font(1)
        font1.setBold(True)
        item.setFont(1, font1)

        item.setForeground(0, QBrush(Qt.darkGreen))
        item.setForeground(1, QBrush(Qt.darkGreen))
