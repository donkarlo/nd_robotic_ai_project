
from nd_utility.oop.design_pattern.structural.decoration.decorator import Decorator as BaseDecorator

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.component import Component as MemoryComponent


class Decorator(MemoryComponent, BaseDecorator):
    def __init__(self, inner: MemoryComponent):
        MemoryComponent.__init__(self)
        BaseDecorator.__init__(self, inner)
