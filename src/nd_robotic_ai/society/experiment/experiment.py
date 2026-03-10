from nd_robotic_ai.society.society import Group  as RoboticGroupComposite


class Experiment:
    def __init__(self, robotic_group_composite: RoboticGroupComposite):
        """

        Args:
            robotic_group_composite: environment is already inside this
        """
        self._robotic_group_composite = robotic_group_composite

    def get_robotic_group_composite(self)-> RoboticGroupComposite:
        return self._robotic_group_composite