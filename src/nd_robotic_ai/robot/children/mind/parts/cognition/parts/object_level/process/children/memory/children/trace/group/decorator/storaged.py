from typing import List

from nd_robotic_ai.robot.composition.kind.mind.meta_cognition.cognition.process.composition.child.memory.composition.trace.group.group import Group as TraceGroup

from nd_robotic_ai.robot.composition.kind.mind.meta_cognition.cognition.process.composition.child.memory.composition.trace.group.decorator.decorator import Decorator as TraceGroupDecorator
from nd_robotic_ai.robot.composition.kind.mind.meta_cognition.cognition.process.composition.child.memory.composition.trace.trace import Trace
from nd_utility.data.storage.decorator.multi_valued.decorator.sliced.cashed.interface import Interface as MultiValuedStorageInterface
from nd_utility.data.storage.interface import Interface as StorageInterface


class Storaged(TraceGroupDecorator, StorageInterface):
    """
    -
    """
    def __init__(self, inner:TraceGroup, storage: MultiValuedStorageInterface):
        """
        The internal_storage in storaged is brain or body part of the mind
        """
        TraceGroupDecorator.__init__(self, inner)
        self._storage = storage
        # here we connect by reference the ram of internal_storage and the mambers of the trace action_potential_group
        self._storage.set_ram(inner.get_traces())

    def get_storage(self) -> MultiValuedStorageInterface:
        return self._storage

    def save(self)->None:
        self._storage.save()

    def load(self)->None:
        self._storage.load()

    def get_traces(self)->List[Trace]:
        """
        Just a nickname
        Returns:

        """
        return self._storage.get_ram()
