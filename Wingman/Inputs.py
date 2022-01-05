from ppadb.device import Device
import numpy as np


class Swipe:

    def __init__(self, device: Device):
        self.main_device = device

    def __swipe_right(self):
        print('________ Swiping Right ________')
        _command = "input swipe 100 500 500 500 50"
        self.main_device.shell(_command)

    def __swipe_left(self):
        print('________ Swiping Left ________')
        _command = "input swipe 100 500 -500 500 50"
        self.main_device.shell(_command)

    def decide(self, genders, ages):
        if len(genders) == 0 and len(ages) == 0:
            self.__swipe_left()
            return

        if genders.count('Male') > 0:
            self.__swipe_left()
            return

        low = 0
        high = 0
        for age in ages:
            age = age.replace('(', '').replace(')', '').replace(' ', '')
            age = age.split(',')
            low += int(age[0])
            high += int(age[1])

        low /= len(ages)
        high /= len(ages)

        age = (high + low) / 2

        if age > 0:
            self.__swipe_right()
            return

        self.__swipe_left()
