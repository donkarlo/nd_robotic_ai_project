from nd_robotic_ai.society.relation.relation import Relation
from nd_robotic_ai.society.component import Component as SocietyComponent
from nd_utility.oop.design_pattern.structural.composition.composite import Composite as BaseComposite
from nd_utility.data.kind.group.group import Group as UtilityGroup

class Group(SocietyComponent, BaseComposite):
    """
    The composite here is a society
    - there is a relationship graph path with length one between childrens of each society
    - parts can be both a single robot and another society
    """

    def __init__(self):
        """
        A society is also a big robot
        Args:
            parts:
        """
        BaseComposite.__init__(self)
        self._relation_group = UtilityGroup()


    def add_relation(self, relation:Relation):
        """

        Args:
            relation:

        Returns:

        """
        self._relation_group.add_member(relation)

    def run(self)->None:
        pass

