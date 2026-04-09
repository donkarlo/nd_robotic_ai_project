from abc import abstractmethod, ABC

from nd_robotic_ai.robot.parts.action.composition.composite import \
    Composite as ActionComposite
from nd_robotic_ai.robot.parts.action.feedback.feedback import \
    Feedback
from nd_robotic_ai.robot.parts.goal.composition.component import Component as GoalComponent


class Action(ActionComposite, ABC):
    """
    - This class represents available actions, not running actions
    - Action is whatever consumes resorces such as energy or health(for example spare classification)
    This action can become so granular that to a action to change voltage in a rotor so in ROS we replaced Action for both Plan and COmmand and mission
    examples of actions the subclasses should support:
    - body
        - Goto

    - Mind
        - memory segregating
        - Memory
            - memorize
            - remember
    """

    def __init__(self, goal: GoalComponent):
        ActionComposite.__init__(self)
        self._goal = goal

    @abstractmethod
    def run(self) -> Feedback:
        """
        This run will be propegated to top or mabe bottom actions
        Returns:

        """
        pass
