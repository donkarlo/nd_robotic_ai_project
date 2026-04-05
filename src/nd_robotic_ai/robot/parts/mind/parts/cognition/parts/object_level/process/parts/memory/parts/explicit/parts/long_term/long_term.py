from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.composite import \
    Composite as MemoryComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.episodic import \
    Episodic
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.sematic import \
    Semantic


class LongTerm(MemoryComposite):
    """
    This class is exactly the same as Component
    """

    def __init__(self):
        MemoryComposite.__init__(self)
        self.add_child(Episodic())
        self.add_child(Semantic())