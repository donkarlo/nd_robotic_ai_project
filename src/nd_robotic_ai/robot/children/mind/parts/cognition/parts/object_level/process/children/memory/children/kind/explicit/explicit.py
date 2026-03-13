from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.children.memory.children.kind.explicit.children.long_term.long_term import \
    LongTerm
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositUnit


class Explicit(RobotCompositUnit):
    """
    This class is exactly the same as Component
    """

    def __init__(self):
        RobotCompositUnit.__init__(self)
        self.add_child(LongTerm())