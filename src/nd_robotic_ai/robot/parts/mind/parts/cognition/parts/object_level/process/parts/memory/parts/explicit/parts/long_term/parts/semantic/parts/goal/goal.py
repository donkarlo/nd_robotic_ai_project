from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.composition.composite import \
    Composite as ActionComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.goal.composition.composite import \
    Composite as GoalComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.goal.parts.suprise_poise.suprise_poise import \
    SurprisePoise
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.sematic import \
    Semantic
from nd_robotic_ai.robot.state.kind.suprise import Suprise as SupriseState
from nd_math.probability.distribution.discrepancy.kind.distance.kind.mahalanobis import Mahalanobis
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.goal.acceptance.kind.suprise.suprise import \
    Suprise as SupriseAcceptance
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.goal.parts.suprise_poise.suprise_poise import \
    SurprisePoise as SuprisePoiseGoal
from nd_math.probability.distribution.discrepancy.kind.distance.kind.mahalanobis import Mahalanobis

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.composition.composite import \
    Composite as ActionComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.goal.acceptance.kind.suprise.suprise import \
    Suprise as SupriseAcceptance
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.goal.composition.composite import \
    Composite as GoalComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.goal.parts.suprise_poise.suprise_poise import \
    SurprisePoise
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.goal.parts.suprise_poise.suprise_poise import \
    SurprisePoise as SuprisePoiseGoal
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.sematic import \
    Semantic
from nd_robotic_ai.robot.state.kind.suprise import Suprise as SupriseState


class Goal(Semantic):
    """
    Maybe plan must be changed according to action feedback
    """

    def __init__(self):
        Semantic.__init__(self)
        acceptance_discrepancy_method = Mahalanobis()

        acceptance_threshold = self._compute_acceptance_threshold()
        acceptance = SupriseAcceptance(acceptance_discrepancy_method, acceptance_threshold)
        desired_suprise_state = SupriseState(self._compute_desired_suprise_state_value())
        suprise_poise_goal = SuprisePoiseGoal(desired_suprise_state, acceptance)

        self._goal_composite = GoalComposite()
        self._goal_composite.add_child(suprise_poise_goal)

    def get_goal_composite(self)->GoalComposite:
        return self._goal_composite

    def get_action_composite(self)->ActionComposite:
        return self._goal_composite

    def _compute_acceptance_threshold(self)->float:
        """
        Find a solution to replace this constant number by the mean+n*variance of running the same episode for the same forcasting model
        """
        return 0.5

    def _compute_desired_suprise_state_value(self)->float:
        return 0.1
