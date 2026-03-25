from abc import ABC, abstractmethod

from nd_robotic_ai.society.society import Group  as RoboticGroupComposite


class Experiment(ABC):
    def __init__(self, robotic_soociety_composite: RoboticGroupComposite):
        """

        Args:
            robotic_soociety_composite: environment is already inside this
        """
        self._robotic_society = robotic_soociety_composite

    def get_robotic_society_composite(self)-> RoboticGroupComposite:
        return self._robotic_society

    @abstractmethod
    def run(self)->None:
        # run human
        # human run teleportation control on leader
        # leader controls follower
        # data recorded
        # forcasting model built

        ...
