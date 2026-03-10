from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from nd_robotic_ai.robot.action.kind.core.kinds.kind import Kind
from datetime import date
from nd_robotic_ai.robot.action.plan.reminder.schedule.by_date_time_loader import ScheduledItem

@dataclass(frozen=True)
class UiPlanSnapshot:
    kinds: List[Kind]
    by_day: Dict[date, List[ScheduledItem]]
    to_plan: Optional[dict]