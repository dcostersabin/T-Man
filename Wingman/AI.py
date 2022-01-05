from pathlib import Path

import cv2

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
gender_list = ['Male', 'Female']


class Model:

    def __init__(self):
        self.age_net = None
        self.gender_net = None
        self.base_dir = Path(__file__).resolve().parent.parent
        self.frontal_face_cascade = cv2.CascadeClassifier(f'{self.base_dir}/data/haarcascade_frontalface_alt.xml')
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
        image = cv2.imread(f'{self.base_dir}/temp/temp.png')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frontal_faces = self.frontal_face_cascade.detectMultiScale(gray, 1.1, 5)

        if len(frontal_faces) > 0:
            print(f'Detected {len(frontal_faces)} Frontal Faces')
            self.__predict(image, frontal_faces)

    def __predict(self, image, rectangles):
        for (x, y, w, h) in rectangles:
            w = w + 100
            h = h + 100
            face_img = image[y:y + h, x:x + w].copy()
            cv2.imwrite(f'{self.base_dir}/temp/a.png', face_img)
            blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
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
