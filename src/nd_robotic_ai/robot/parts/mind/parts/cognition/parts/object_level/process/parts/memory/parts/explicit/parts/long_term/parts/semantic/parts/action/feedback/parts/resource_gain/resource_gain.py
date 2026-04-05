from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.feedback.composition.leaf import \
    Leaf


class ResourceGain(Leaf):
    def __init__(self, value: float):
        Leaf.__init__(self)
        self._value = value

    def get_value(self) -> float:
        return self._value