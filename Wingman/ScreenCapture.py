import os
import cv2
from ppadb.device import Device
from pathlib import Path


class Capture:

    def __init__(self, device: Device):
        self.main_device = device
        self.base_dir = Path(__file__).resolve().parent.parent
        self.__create_dir()

    def __create_dir(self):
        if os.path.exists(f'{self.base_dir}/temp'):
            return
        print(f'Creating temp Directory In {self.base_dir}')
        os.mkdir(f'{self.base_dir}/temp')

    def capture(self):
        _command = "screencap -p sdcard/tinder_check.png"
        self.main_device.shell(_command)
        self.__save()

    def __save(self):
        self.main_device.pull('/sdcard/tinder_check.png', f'{self.base_dir}/temp/temp.png')
        self.__resize()

    def __resize(self):
        img = cv2.imread(f'{self.base_dir}/temp/temp.png')
        height, width = img.shape[0], img.shape[1]
        height_cutoff = height // 6
        crop_image = img[height_cutoff: height - height_cutoff, :]
        cv2.imwrite(f'{self.base_dir}/temp/temp.png', crop_image)
