from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.composite import \
    Composite as MemoryComposite


class Skill(MemoryComposite):
    """
    Habituals composed of conditioning and procedural
    """

    def __init__(self):
        MemoryComposite.__init__(self)
