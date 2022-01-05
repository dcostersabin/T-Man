from ppadb.device import Device


class Unlock:

    def __init__(self, device: Device, passwd: str):
        self.main_device = device
        self.passwd = passwd
        self.status = True
        self.__check_status()
        self.__unlock()

    def __check_status(self):
        _command = "dumpsys power | grep 'mWakefulness='"
        status = str(self.main_device.shell(_command).split('=')[1].strip())
        self.status = True if status == "Asleep" or status == "Dozing" else False

    def __unlock(self):
        _command = f'input keyevent POWER && input swipe 600 600 0 0 ' \
                   f'&& input text {self.passwd} && input keyevent 66'
        if self.status:
            self.main_device.shell(_command)
