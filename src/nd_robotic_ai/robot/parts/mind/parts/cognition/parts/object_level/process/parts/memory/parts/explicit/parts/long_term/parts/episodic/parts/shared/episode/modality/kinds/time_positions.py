from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.trace.kinds.core.kinds import \
    Group
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.shared.episode.modality.modality import Modality
from nd_utility.data.kind.dic.dic import Dic


class TimePositions(Modality):
    """
    DO not inject numpyz storage into this, how we store the data is different than how we remeber it
    """
    def __init__(self, dic:Dic):
        Modality.__init__(self, dic)

