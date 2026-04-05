from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.composite import \
    Composite as MemoryComposite
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.shared.episode.episode import \
    Episode
from nd_utility.oop.design_pattern.structural.composition.component import Component


class EventSpecificKnowledge(MemoryComposite):
    """
    It is composed of episodes in which the robot itself is involved
    """

    def __init__(self):
        MemoryComposite.__init__(self)

    def add_child(self, child: Component) -> None:
        if not isinstance(child, Episode):
            raise TypeError('Child must be an ' + Episode.__class__.__name__)
        MemoryComposite.add_child(self, child)

    def add_episode(self, episode: Episode) -> None:
        self.add_child(episode)
