from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.children.memory.children.kind.explicit.explicit import \
    Explicit
from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.children.memory.children.kind.implicit.implicit import \
    Implicit
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositComponent


class Memory(RobotCompositComponent):
    """
    This class is exactly the same as Component
    """

    def __init__(self):
        RobotCompositComponent.__init__(self)
        self.add_child(Explicit())
        self.add_child(Implicit())