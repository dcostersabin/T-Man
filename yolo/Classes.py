class Classes:
    def __init__(self):
        self.classes = self.__get_classes()
        self.detection_filter_person = self.__get_filter2()
        super().__init__()

    def __get_classes(self):
        return ['person', 'bicycle', 'car', 'motorbike',
                'aeroplane', 'bus', 'train', 'truck',
                'boat', 'traffic light', 'fire hydrant',
                'stop sign', 'parking meter', 'bench',
                'bird', 'cat', 'dog', 'horse', 'sheep',
                'cow', 'elephant', 'bear', 'zebra', 'giraffe',
                'backpack', 'umbrella', 'handbag', 'tie',
                'suitcase', 'frisbee', 'skis', 'snowboard',
                'sports ball', 'kite', 'baseball bat',
                'baseball glove', 'skateboard', 'surfboard',
                'tennis racket', 'bottle', 'wine glass', 'cup',
                'fork', 'knife', 'spoon', 'bowl', 'banana',
                'apple', 'sandwich', 'orange', 'broccoli',
                'carrot', 'hot dog', 'pizza', 'donut',
                'cake', 'chair', 'sofa', 'pottedplant',
                'bed', 'diningtable', 'toilet', 'tvmonitor',
                'laptop', 'mouse', 'remote', 'keyboard',
                'cell phone', 'microwave', 'oven', 'toaster',
                'sink', 'refrigerator', 'book', 'clock', 'vase',
                'scissors', 'teddy bear', 'hair drier', 'toothbrush']

    def __get_filter2(self):
        return ['person']
