from nd_physics.quantity.kind.time.time import Time
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.trace.decorator.decorator import \
    Decorator

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.trace.interface import \
    Interface as TraceInterface


class Timed(Decorator):
    def __init__(self, inner: TraceInterface, time: Time):
        Decorator.__init__(self, inner)
        self._time = time

    def get_time(self) -> Time:
        return self._time
