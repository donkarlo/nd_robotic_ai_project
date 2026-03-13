from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.children.memory.children.kind.explicit.children.long_term.episodic.children.autobigraphical.children.event_specific_knowledge.children.multi_modal_sensory.multi_modal_sensory import \
    MultiModalSensory
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositUnit


class EventSpecificKnowledge(RobotCompositUnit):
    """
    This class is exactly the same as Component
    """

    def __init__(self):
        RobotCompositUnit.__init__(self)
        self.add_child(MultiModalSensory())
