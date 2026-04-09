from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeComponent



class Perception(RobotCompositeComponent):
    """
    Should I add the current observation point to a meaning ful group and create an abstract concept or should I pass it as it is to planning?
    """
    def __init__(self):
        RobotCompositeComponent.__init__(self)
