from nd_robotic_ai.robot.parts.action.composition.composite import \
    Composite as ActionComposite
from nd_robotic_ai.robot.parts.goal.composition.composite import \
    Composite as GoalComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.sematic import \
    Semantic


class Plan(Semantic):
    """
    Maybe plan must be changed according to action feedback
    """

    def __init__(self):
        Semantic.__init__(self)

        self._goal_composite.add_child(GoalComposite())
        self._action_composite.add_child(ActionComposite())
        self.add_child(self._goal_composite)
        self.add_child(self._action_composite)

    def get_goal_composite(self) -> GoalComposite:
        return self._goal_composite

    def get_action_composite(self) -> ActionComposite:
        return self._goal_composite
