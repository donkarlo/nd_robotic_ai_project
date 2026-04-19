"""
https://en.wikipedia.org/wiki/Category:Mental_processes
"""
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.attention.attention import \
    Attention
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.learning.learning import Learning
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.memory import Memory
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.perception.perception import \
    Perception
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.thinking.thiniking import \
    Thinking
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeComponent


class Process(RobotCompositeComponent):
    def __init__(self):
        """
        memory, percepting, attention: Attention, thinking: Thinking, learning: Learning
        """
        RobotCompositeComponent.__init__(self)
        self.add_children([Memory(), Learning(), Thinking(), Perception(), Attention()])