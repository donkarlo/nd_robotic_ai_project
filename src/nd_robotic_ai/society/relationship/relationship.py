from nd_robotic_ai.society.component import Component as SocietyComponent


class Relation:
    def __init__(self, left: SocietyComponent, right: SocietyComponent):
        """
        Announces a relationship between all classification of a society
        """
        self._left = left
        self._right = right
