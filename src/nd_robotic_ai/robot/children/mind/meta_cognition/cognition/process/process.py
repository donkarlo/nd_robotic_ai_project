"""
https://en.wikipedia.org/wiki/Category:Mental_processes
"""
from nd_robotic_ai.robot.children.mind.meta_cognition.cognition.process.composition.child.attention.attention import \
    Attention
from nd_robotic_ai.robot.children.mind.meta_cognition.cognition.process.composition.child.learning.learning import \
    Learning
from nd_robotic_ai.robot.children.mind.meta_cognition.cognition.process.composition.child.memory.memory import Memory
from nd_robotic_ai.robot.children.mind.meta_cognition.cognition.process.composition.child.perception.perception import \
    Perception
from nd_robotic_ai.robot.children.mind.meta_cognition.cognition.process.composition.child.thinking.thiniking import \
    Thinking
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeComponent


class Process(RobotCompositeComponent):
    def __init__(self):
        """
        memory, perception, attention: Attention, thinking: Thinking, learning: Learning
        """
        RobotCompositeComponent.__init__(self)
        self.add_children([Memory(), Learning(), Thinking(), Perception(), Attention()])