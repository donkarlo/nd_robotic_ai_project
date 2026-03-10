from nd_robotic_ai.society.society import Group
from nd_utility.data.kind.group.group import Group


class Container(Group):
    def __init__(self, container_robot, included_robots:Group):
        Group.__init__(self)
        self._container_robot = container_robot
        self._children.add_members(included_robots)