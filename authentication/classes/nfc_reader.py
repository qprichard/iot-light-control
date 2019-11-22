import nfc
from time import sleep

class NFCReader():
    def __init__(self):
        """
        connect the nefc reader
        """
        self.clf = nfc.ContactlessFrontend('usb')
        assert self.clf.open('usb') is True

        self.target = None
        self.is_listening = False

    def read_tag(self):
        """
        launch listening until it find a card to read
        """
        self.tag = self.clf.connect(rdwr={'on-connect': lambda tag: False, 'beep-on-connect': True})

    def listen(self, on_reading = None):
        """
        reload the listening each time it's done
        launch actions on tag reading
        """
        self.is_listening = True
        self.read_tag()
        while self.is_listening:
            if self.tag is not None:
                UID = self.get_UID(self.tag)

                if on_reading is not None:
                    on_reading(UID)

    def stop_listening(self):
        self.is_listening = False

    def start_listening(self):
        self.is_listening = True

    def shutdown(self):
        self.is_listening = False
        self.clf.close()
        exit()

    def get_UID(self, tag):
        """
        Parse the dumped tag and return only the UID
        return -1 if there is an error
        """
        try:
            dumped_tag = tag.dump()
            dumped_tag = [occ.replace(' ', '').split(':')[1] for occ in dumped_tag[0:2]]

            UID = dumped_tag[0][0:6]+dumped_tag[1][0:8]
            return UID
        except:
            return -1

    def red_buzz(self):
        self.clf.device.turn_on_led_and_buzzer()

    def green(self):
        self.clf.device.turn_off_led_and_buzzer()
