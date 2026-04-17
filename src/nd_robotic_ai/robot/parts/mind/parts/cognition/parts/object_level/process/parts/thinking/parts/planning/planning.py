from tensorflow.python.ops.gen_array_ops import deep_copy

from nd_robotic_ai.robot.parts.action.feedback.feedback import \
    Feedback

from nd_robotic_ai.robot.parts.body.parts.nervous_system.neural_coding.action_potential.observer.publisher import \
    Publisher as ObservationPublisher
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.autobiographic.parts.event_specific_knowledge.kinds.multi_modal.single_modality_forcasting_models_evolving import \
    SingleModalityForcastingModelsEvolving
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.perception.observer.kind.trace_formation.subscriber import \
    Subscriber as PerceptionSubscriber
from nd_robotic_ai.robot.parts.mind.state.kinds.idle import Idle as IdleMentalState
from nd_robotic_ai.robot.parts.mind.state.state import State as MentalState


class Planning(PerceptionSubscriber, ObservationPublisher):
    """
    TODO: whenever called planning must also be added to Actioncomposite in handle_updated_plan
    - planning must be such that it follows minimising suprise following one of the brain theories bayesian>predictive>active inference
    """

    def __init__(self):
        self._updated_working_memory_plan = deep_copy(self._current_working_memory_plan)

    def handle_new_mind_state(self, mental_state: MentalState) -> None:
        if isinstance(mental_state, IdleMentalState):
            # build forcasting models, TODO, look esk remeberunbg
            modifying_single_modality_forcasting_model = self.find_component_by_name(
                SingleModalityForcastingModelsEvolving)
            modifying_single_modality_forcasting_model.enlive()



    def run(self) -> Feedback:
        """
        Running planning action not the action composite
        Returns:

        """
        print("running planning")
