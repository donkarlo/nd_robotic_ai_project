from nd_robotic_ai.robot.parts.body.parts.nervous_system.parts.central.central import Central
from nd_robotic_ai.robot.parts.body.parts.nervous_system.parts.peripheral.peripheral import Peripheral
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeUnit


class NervousSystem(RobotCompositeUnit):
    def __init__(self):
        RobotCompositeUnit.__init__(self)
        self.add_child(Central())
        self.add_child(Peripheral())