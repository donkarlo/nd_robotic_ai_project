from nd_robotic_ai.robot.robot import Robot
from nd_robotic_ai.robot.robot import Group
class TestRobot:
    def test__init__(self, sensor_set:Group)->None:
        robot = Robot()