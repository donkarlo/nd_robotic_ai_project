from nd_robotic_ai.experiment.condition.condition import Condition
from nd_robotic_ai.society.society import Group


class RoboticSociety(Condition):
    def __init__(self, robotic_society:Group):
        self._robotic_society = robotic_society

    def get_robotic_society(self)->Group:
        return self._robotic_society
