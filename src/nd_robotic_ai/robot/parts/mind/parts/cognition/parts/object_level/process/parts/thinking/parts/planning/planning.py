from abc import abstractmethod, ABC

from tensorflow.python.ops.gen_array_ops import deep_copy

from nd_robotic_ai.robot.parts.action.feedback.feedback import \
    Feedback
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.autobiographic.parts.event_specific_knowledge.kinds.multi_modal.single_modality_forcasting_models_evolving import \
    SingleModalityForcastingModelsEvolving
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.perception.trace.trace import Trace
from nd_robotic_ai.robot.parts.mind.state.kind.idle.idle import Idle as IdleMentalState
from nd_robotic_ai.robot.parts.stimulus.observer.kind.mind_state_change.mind_state_change import MindStateChange
from nd_robotic_ai.robot.parts.stimulus.observer.kind.mind_state_change.subscriber import \
    Subscriber as MindStateChangeSubscriber
from nd_robotic_ai.robot.parts.stimulus.observer.kind.trace_formation.subscriber import \
    Subscriber as TraceFormationSubscriber
from nd_utility.oop.inheritance.overriding import override_from


class Planning(MindStateChangeSubscriber, TraceFormationSubscriber, ABC):
    """
    TODO: whenever called planning must also be added to Actioncomposite in handle_updated_plan
    - planning must be such that it follows minimising suprise following one of the brain theories bayesian>predictive>active inference
    """

    def __init__(self):
        self._updated_working_memory_plan = deep_copy(self._current_working_memory_plan)

    @override_from(MindStateChangeSubscriber, False, False)
    def handle_mind_state_change(self, mental_state_change: MindStateChange) -> None:
        if isinstance(mental_state_change.get_end_mind_state(), IdleMentalState):
            # build forcasting models, TODO, look esk remeberunbg
            modifying_single_modality_forcasting_model = self.find_component_by_name(
                SingleModalityForcastingModelsEvolving)
            modifying_single_modality_forcasting_model.enlive()

    @override_from(TraceFormationSubscriber, False, False)
    def handle_trace_formation(self, trace: Trace) -> None:
        ...

    @abstractmethod
    def run(self) -> Feedback:
        """
        Running planning action not the action composite
        Returns:

        """
        print("running planning")
