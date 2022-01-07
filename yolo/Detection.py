import random
import cv2
import numpy as np
from yolo.Model import Model
from pathlib import Path


class Detection(Model):

    def __init__(self, image, threshold=0.5, nms_threshold=0.4, save=False):
        super(Detection, self).__init__()
        self.image = image
        self.threshold = threshold
        self.nms_threshold = nms_threshold
        self.font = cv2.FONT_HERSHEY_PLAIN
        self.save = save
        self.filter = self.detection_filter_person
        self.filter_counts = self.__get_filter_counts()
        self.base_dir = Path(__file__).resolve().parent.parent
        self.boxes = []
        self.conf = []
        self.class_ids = []
        self.labels = []
        self.__load_pipeline()
        super().__init__()

    def __get_filter_counts(self):
        return {class_name: 0 for class_name in self.filter}

    def __load_image(self):
        self.height, self.width, self.channels = self.image.shape

    def __detect_object(self):
        blob = cv2.dnn.blobFromImage(self.image, scalefactor=0.00392,
                                     size=(416, 416),
                                     mean=(0, 0, 0),
                                     swapRB=True, crop=False)
        self.model.setInput(blob)
        self.outputs = self.model.forward(self.output_layers)

    def __get_box_dimensions(self):
        for output in self.outputs:
            for detect in output:
                scores = detect[5:]
                class_id = np.argmax(scores)
                conf = scores[class_id]
                if conf > self.threshold:
                    center_x = int(detect[0] * self.width)
                    center_y = int(detect[1] * self.height)
                    w = int(detect[2] * self.width)
                    h = int(detect[3] * self.height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    self.boxes.append([x, y, w, h])
                    self.conf.append(float(conf))
                    self.class_ids.append(class_id)

    def __draw_labels(self):
        indexes = cv2.dnn.NMSBoxes(self.boxes, self.conf, self.threshold, self.nms_threshold)
        for i in range(len(self.boxes)):
            if i in indexes:
                x, y, w, h = self.boxes[i]
                label = str(self.classes[self.class_ids[i]])
                if label in self.filter:
                    self.filter_counts[label] += 1
                    cv2.imwrite(f'{self.base_dir}/temp/temp.png', self.image[y:y + h, x:x + w])

    def __load_pipeline(self):
        self.__load_image()
        self.__detect_object()
        self.__get_box_dimensions()
        self.__draw_labels()
