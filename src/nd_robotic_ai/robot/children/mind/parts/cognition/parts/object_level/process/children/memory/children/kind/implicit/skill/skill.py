from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositComponent

class Skill(RobotCompositComponent):
    """
    Habituals composed of conditioning and procedural
    """
    def __init__(self):
        RobotCompositComponent.__init__(self)