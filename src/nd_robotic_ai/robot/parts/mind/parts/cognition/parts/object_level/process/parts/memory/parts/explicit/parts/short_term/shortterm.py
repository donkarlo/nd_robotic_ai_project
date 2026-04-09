from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.composite import \
    Composite as MemoryComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.short_term.parts.plan.plan import \
    Plan as CurrentRunningPlan


class ShortTerm(MemoryComposite):
    """
    To represent short_term memory or short memory
    """

    def __init__(self):
        """
        Here we design the aritecture or philosophy of the memory. The body parts is in body
        coupling memorizing, remebering and storing
        Args:
            memory_tree: contains short- and long-term memory tree
            memorizing: contains the strategy for memorizing something
            remembering: contains the strategy to remeber something

        """
        MemoryComposite.__init__(self)
        self.add_child(CurrentRunningPlan())
