from yolo.AssetsPath import AssetsPath
from yolo.Classes import Classes
import cv2


class Model(AssetsPath, Classes):

    def __init__(self):
        super(Model, self).__init__()
        self.model = self.__get_model()
        self.output_layers = self.__get_output_layers()
        super().__init__()

    def __get_model(self):
        return cv2.dnn.readNet(self.weights, self.cfg)

    def __get_output_layers(self):
        layer_names = self.model.getLayerNames()
        unconnected_layers = self.model.getUnconnectedOutLayers()
        output_layers = [layer_names[i - 1] for i in unconnected_layers]
        return output_layers
