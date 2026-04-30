from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.composite import \
    Composite as MemoryComposite


class Composite(MemoryComposite):
    """
    Stores the way an action should be performed
    """

    def __init__(self):
        MemoryComposite.__init__(self)

    def run(self) -> None:
        self._feedback = self._action.enliven()

        for child in MemoryComposite.get_child_group_members(self):
            child.run()