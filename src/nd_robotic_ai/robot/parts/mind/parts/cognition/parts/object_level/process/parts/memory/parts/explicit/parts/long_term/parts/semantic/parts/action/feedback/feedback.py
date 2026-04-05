from abc import abstractmethod

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.feedback.composition.composite import \
    Composite as FeedbackComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.feedback.parts.goal_gain.goal_gain import \
    GoalGain as GoalGain
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.feedback.parts.resource_gain.resource_gain import \
    ResourceGain as ResourceGain


class Feedback(FeedbackComposite):
    def __init__(self):
        FeedbackComposite.__init__(self)
        self._goal_gain = GoalGain()
        self._resource_gain = ResourceGain()

    @abstractmethod
    def get_value(self) -> float:
        """
        This method should provide a soltion to convert the discrepence between goal_gain gain and resource_gain gain
        """
        ...
