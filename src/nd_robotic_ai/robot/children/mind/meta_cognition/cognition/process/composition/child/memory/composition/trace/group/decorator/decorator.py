from nd_robotic_ai.robot.composition.kind.mind.meta_cognition.cognition.process.composition.child.memory.composition.trace.group.interface import Interface as TraceGroupInterface
from nd_utility.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, TraceGroupInterface):
    """
    """

    def __init__(self, inner: TraceGroupInterface):
        BaseDecorator.__init__(self, inner)
