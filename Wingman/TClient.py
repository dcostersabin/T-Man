import sys
import time
from ppadb.client import Client
from Wingman.Unlocker import Unlock
from Wingman.Check import TinderCheck
from Wingman.Inputs import Swipe
from Wingman.ScreenCapture import Capture
from Wingman.AI import Model


class TClient(Client):

    def __init__(self, passwd):
        super().__init__()
        self.main_device = None
        self.passwd = passwd
        self.__show_connected_devices()
        self.__select_main_device()
        self.__unlock_phone()
        self.__check_tinder()

    def __show_connected_devices(self):
        print(f'Total Connected Devices {len(self.devices())}\n')
        for idx, device in enumerate(self.devices()):
            print(f'Device #{idx + 1}\'s Serial: {device.serial}')

    def __select_main_device(self):
        self.main_device = self.devices()[0] if len(self.devices()) > 0 else self.__close()
        print(f'\nSelecting Main Device as {self.main_device.serial}')

    def __check_tinder(self):
        tinder = TinderCheck(self.main_device)
        if tinder.exists:
            time.sleep(5)
            self.__start()

    def __start(self):
        while True:
            screen = Capture(self.main_device)
            screen.capture()
            time.sleep(1)
            genders, ages = Model().predict()
            Swipe(self.main_device).decide(genders, ages)

    def __unlock_phone(self):
        Unlock(self.main_device, self.passwd)

    def __close(self):
        sys.exit(f'Device Not Detected. Device Count {len(self.devices())}')
