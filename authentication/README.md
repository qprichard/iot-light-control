## Configuration

### NFCReader Installation

[source](http://tvaira.free.fr/rfid/tutoriel-nfc-acr122u.pdf)
[nfcpy documentation](https://nfcpy.readthedocs.io/en/latest/examples/sense.html)

#### Install drivers

* sudo apt install pcsc-tools pcscd
* sudo apt install libpcsclite-dev
* sudo apt install libpcsclite1
* sudo apt install libusb-dev

Install libnfc

* sudo apt install libnfc-bin libnfc-dev libnfc5

Test scan:

* sudo pcsc_scan

#### pip installation
* pip install nfcpy
