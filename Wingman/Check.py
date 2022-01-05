from ppadb.device import Device


class TinderCheck:

    def __init__(self, device: Device):
        self.main_device = device
        self.exists = False
        self.__check_tinder()

    def __check_tinder(self):
        if self.main_device.is_installed('com.tinder'):
            print('*********** Opening Tinder ***********')
            self.__open_tinder()
        else:
            print('************ Tinder Not Found ************ \n')
            self.__install_tinder()

    def __install_tinder(self):
        _command = "am start -a android.intent.action.VIEW -d 'market://details?id=com.tinder'"
        self.main_device.shell(_command)
        print("___________ Redirecting To Tinder On Play Store ___________")

    def __open_tinder(self):
        _command = "monkey -p com.tinder -c android.intent.category.LAUNCHER 1"
        self.main_device.shell(_command)
        self.exists = True
