import os
from pathlib import Path


class AssetsPath:
    def __init__(self):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.parent = Path(self.current_path).parent
        self.weights = self.__set_weights_path()
        self.cfg = self.__set_cfg_path()
        super().__init__()

    def __set_weights_path(self):
        return f'{self.parent}/data/model/weights/yolov4.weights'

    def __set_cfg_path(self):
        return f'{self.parent}/data/model/cfg/yolov4.cfg'
