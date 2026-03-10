from typing import Protocol, runtime_checkable, List

from nd_robotic_ai.robot.robot import Goal
from nd_robotic_ai.robot.robot import Robot


@runtime_checkable
class Interface(Protocol):
    _memebers:List[Robot]
    def get_memebers(self) -> List[Robot]: ...
    def achieve_mission(self, robot:Robot, mission:Goal)->bool: ...