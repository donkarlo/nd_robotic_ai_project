"""
https://en.wikipedia.org/wiki/Category:Mental_processes
"""
from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.children.attention.attention import \
    Attention
from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.children.learning.learning import Learning
from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.children.memory.memory import Memory
from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.children.perception.perception import \
    Perception
from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.children.thinking.thiniking import \
    Thinking
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeComponent


class Process(RobotCompositeComponent):
    def __init__(self):
        """
        memory, perception, attention: Attention, thinking: Thinking, learning: Learning
        """
        RobotCompositeComponent.__init__(self)
        self.add_children([Memory(), Learning(), Thinking(), Perception(), Attention()])