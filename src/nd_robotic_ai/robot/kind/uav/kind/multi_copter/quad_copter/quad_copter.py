# from nd_robotic_ai.robot.children.uav.children.multi_copter.quad_copter.children.body.actuator.rotor.composite import Group as RotorGroup
from nd_robotic_ai.robot.kind.uav.uav import Uav


class QuadCopter(Uav):
    def __init__(self):
        Uav.__init__(self)
        # rotor = [Rotor(Positions.)]
        # rotor_group = RotorGroup()
        #
        # self.add_child()