from nd_robotic_ai.robot.children.body.parts.nervous_system.children.central.central import Central
from nd_robotic_ai.robot.children.body.parts.nervous_system.children.peripheral.peripheral import Peripheral
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeUnit


class NervousSystem(RobotCompositeUnit):
    def __init__(self):
        RobotCompositeUnit.__init__(self)
        self.add_child(Central())
        self.add_child(Peripheral())