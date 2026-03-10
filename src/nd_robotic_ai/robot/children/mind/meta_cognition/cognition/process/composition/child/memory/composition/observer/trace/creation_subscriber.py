from typing import Protocol, runtime_checkable

from nd_robotic_ai.robot.composition.kind.mind.meta_cognition.cognition.process.composition.child.memory.composition.trace.trace import Trace

@runtime_checkable
class TraceCreationSubscriber(Protocol):
    def do_with_created_trace(self, trace: Trace)->None: ...