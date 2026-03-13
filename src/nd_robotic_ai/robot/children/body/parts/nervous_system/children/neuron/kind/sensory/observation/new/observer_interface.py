from typing import Protocol

from nd_robotic_ai.robot.robot import Observation


class Observer(Protocol):
    def new_observation_arrival_update(self, observation:Observation)->None: ...