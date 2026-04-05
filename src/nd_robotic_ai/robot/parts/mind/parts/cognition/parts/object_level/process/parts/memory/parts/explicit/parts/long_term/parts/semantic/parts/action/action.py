from abc import abstractmethod, ABC

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.composition.composite import \
    Composite as CompositeAction


class Action(CompositeAction, ABC):
    """
    - This class represents availab le actions not running actions
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

    def __init__(self):
        CompositeAction.__init__(self)

    @abstractmethod
    def run(self) -> None:
        """
        This run will be propegated to top or mabe bottom actions
        Returns:

        """
        pass
