
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositUnit
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.autobiographic.parts.event_specific_knowledge.event_specific_knowledge import \
    EventSpecificKnowledge


class Autobiographic(RobotCompositUnit):
    """
    Whatever self is involved
    """

    def __init__(self):
        RobotCompositUnit.__init__(self)
        self.add_child(EventSpecificKnowledge())
