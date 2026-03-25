from nd_robotic_ai.robot.composition.composite import Composite as RobotComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.trace.group.group import \
    Group
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.trace.trace import \
    Trace


class Episode(RobotComposite):
    def __init__(self):
        """
        composed of time, location, event(particular occurrences of actions and their properties)
        """
        RobotComposite.__init__(self)
