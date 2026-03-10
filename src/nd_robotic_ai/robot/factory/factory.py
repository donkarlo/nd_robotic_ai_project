from nd_robotic_ai.robot.robot import Structure


class Factory:
    def __init__(self):
        self._built_object:Structure = None

    def build_from_dir_structure(self, str_dir_path:str)->Structure:
        pass