from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.episodic import \
    Episodic
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositComponent


class LongTerm(RobotCompositComponent):
    """
    This class is exactly the same as Component
    """

    def __init__(self):
        RobotCompositComponent.__init__(self)
        self.add_child(Episodic())