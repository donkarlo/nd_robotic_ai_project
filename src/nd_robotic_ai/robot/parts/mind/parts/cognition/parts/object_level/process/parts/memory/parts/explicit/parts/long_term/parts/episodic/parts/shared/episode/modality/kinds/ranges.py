from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositUnit
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.episodic.parts.shared.episode.episode import \
    Episode


class TimeLidar(Episode):
    def __init__(self):
        RobotCompositUnit.__init__(self)
