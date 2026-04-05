from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.shared.episode.episode import \
    Episode
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.shared.episode.modality.modality import \
    Modality
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.leaf.leaf import \
    Group
from nd_utility.data.kind.dic.dic import Dic


class MultiModal(Episode):
    def __init__(self, dic:Dic):
        """
        composed of time, location, event(particular occurrences of actions and their properties)
        """
        self._trace_group = Group()

    def add_modality(self, modality: Modality) -> None:
        self.add_child(modality)
