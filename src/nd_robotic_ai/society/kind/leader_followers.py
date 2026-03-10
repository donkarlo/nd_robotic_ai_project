from typing import List

from nd_robotic_ai.robot.robot import Robot
from nd_robotic_ai.society.society import Group


class LeaderFollowers(Group):
    def __init__(self, leader: Robot):
        self._leader = leader

    def add_follower(self, robot: Robot)-> None:
        self._children.add_member(robot)

    def get_leader(self) -> Robot:
        return self._leader

    def get_followers(self) -> List[Robot]:
        return self._followers
