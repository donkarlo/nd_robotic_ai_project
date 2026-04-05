
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.composite import \
    Composite as MemoryComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.autobiographic.autobiographic import \
    Autobiographic


class Episodic(MemoryComposite):
    """
    This class is exactly the same as Component
    """

    def __init__(self):
        MemoryComposite.__init__(self)
        self.add_child(Autobiographic())