from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Dict, List, Optional

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.working.parts.plan.reminder.schedule.by_date_time_loader import ScheduledItem


@dataclass(frozen=True)
class UiPlanSnapshot:
    kinds: List[Any]
    by_day: Dict[date, List[ScheduledItem]]
    to_plan: Optional[Any]