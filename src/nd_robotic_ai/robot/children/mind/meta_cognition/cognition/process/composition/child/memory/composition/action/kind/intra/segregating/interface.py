
from nd_robotic_ai.robot.composition.kind.mind.meta_cognition.cognition.process.composition.child.memory.composition.component import \
    Component as MemoryComponent
from typing import List

from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def __init__(self, source_memory_component: MemoryComponent):
        ...

    @abstractmethod
    def segregate(self)->None:
        ...

    @abstractmethod
    def get_segregated_components(self)->List[MemoryComponent]:
        ...