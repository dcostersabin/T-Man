import cv2
import numpy as np
from pathlib import Path
from face_recognition import face_locations
from face_recognition import load_image_file
from PIL import Image

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
gender_list = ['Male', 'Female']


class Model:

    def __init__(self, detection_type='haarcascade'):
        self.age_net = None
        self.gender_net = None
        self.detection_type = detection_type
        self.base_dir = Path(__file__).resolve().parent.parent
        self.frontal_face_cascade = cv2.CascadeClassifier(f'{self.base_dir}/data/haarcascade_frontalface_alt.xml')
        self.person_detected = False
        self.detected_genders = list()
        self.detected_ages = list()
        self.__initialize_model()
        self.__detect_face()

    def __initialize_model(self):
        self.age_net = cv2.dnn.readNetFromCaffe(
            f'{self.base_dir}/data/deploy_age.prototxt',
            f'{self.base_dir}/data/age_net.caffemodel')

        self.gender_net = cv2.dnn.readNetFromCaffe(
            f'{self.base_dir}/data/deploy_gender.prototxt',
            f'{self.base_dir}/data/gender_net.caffemodel')

    def __detect_face(self):
        image = load_image_file(f'{self.base_dir}/temp/temp.png')
        locations = face_locations(image)

        if len(locations) > 0:
            top, right, bottom, left = locations[0]
            print("____ Face Detected ____")
            img = Image.fromarray(image)
            cropped = img.crop((left, top, right, bottom))
            self.__predict(np.asarray(cropped))

    def __predict(self, image):

        blob = cv2.dnn.blobFromImage(image, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        self.gender_net.setInput(blob)

        gender_preds = self.gender_net.forward()
        gender = gender_list[gender_preds[0].argmax()]
        self.detected_genders.append(gender)

        self.age_net.setInput(blob)
        age_predict = self.age_net.forward()
        age = age_list[age_predict[0].argmax()]
        self.detected_ages.append(age)

    def predict(self):
        return self.detected_genders, self.detected_ages
