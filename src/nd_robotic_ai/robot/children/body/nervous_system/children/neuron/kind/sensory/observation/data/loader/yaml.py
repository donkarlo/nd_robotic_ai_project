class MultiSensorYamlFile:
    def __init__(self, file_path:str , sensor_ids:list):
        self._file_path = file_path
        self._sensor_ids = sensor_ids