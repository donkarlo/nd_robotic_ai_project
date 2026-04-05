from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.action import Action
from nd_robotic_ai.robot.composition.kind.body.limb.kind.rotor.action.change_arming_mode.mode import Mode


class ChangeArmingMode(Action):
    def __init__(self):
        Action.__init__(self)

    def set_mode(self, mode:Mode)->None:
        self._mode = mode