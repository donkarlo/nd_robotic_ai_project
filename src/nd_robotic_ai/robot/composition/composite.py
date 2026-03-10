from nd_utility.oop.design_pattern.structural.composition.component import Component as BaseComponent
from nd_utility.oop.design_pattern.structural.composition.composite import Composite as BaseComposite


class Composite(BaseComposite, BaseComponent):
    def __init__(self):
        BaseComposite.__init__(self)
        BaseComponent.__init__(self)
