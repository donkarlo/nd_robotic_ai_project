from tensorflow.python.ops.gen_array_ops import deep_copy

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.autobiographic.parts.event_specific_knowledge.kinds.multi_modal import \
    modifying_single_modality_forcasting_model
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.autobiographic.parts.event_specific_knowledge.kinds.multi_modal.modifying_single_modality_forcasting_model import \
    ModifyingSingleModalityForcastingModel
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.action import \
    Action as ActionComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.goal.composition.composite import \
    Composite as GoalComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.working.parts.plan.observer.subscriber import \
    Subscriber as WorkingMamoryPlanUpdateSubscriber
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.working.parts.plan.plan import \
    Plan as WorkingMemoryPlan
from nd_utility.oop.inheritance.overriding import override_from


class Planning(ActionComposite, WorkingMamoryPlanUpdateSubscriber):
    """
    TODO: whenever called planning must alseo be added to Actioncomposite in handle_updated_plan
    """

    def __init__(self, current_working_memory_plan: WorkingMemoryPlan):
        self._current_working_memory_plan = current_working_memory_plan

        # deciding what to do when idle. Brain is not multi task it mostly switches between the tasks
        there_is_no_goal_but_suprise_reduction = True
        no_running_action = True
        # is it in offline mode
        if there_is_no_goal_but_suprise_reduction and no_running_action:
            # build forcasting models
            building_single_modality_forcasting_model = self.find_component_by_name(ModifyingSingleModalityForcastingModel)

        self._updated_working_memory_plan = deep_copy(self._current_working_memory_plan)

    def get_updated_plan(self) -> WorkingMemoryPlan:
        pass

    def get_predicted_success_rate(self) -> float:
        pass

    @override_from(WorkingMamoryPlanUpdateSubscriber, False, False)
    def handle_updated_plan(self, updated_working_memory_plan: WorkingMemoryPlan):
        """
        Action composite must be replanned
        Args:
            goal:

        Returns:

        """
        self._current_working_memory_plan = deep_copy(self._updated_working_memory_plan)
        self._updated_working_memory_plan = updated_working_memory_plan
        self.run()

    def find_updated_goal(self) -> GoalComposite:
        pass

    def find_updated_action_feedback(self) -> ActionComposite:
        pass

    def run(self) -> None:
        """
        Running planning action not the action composite
        Returns:

        """
        print("running planning")
