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

#### blacklist

in `/etc/modprobe.d/blacklist-libnfc.conf` add:

```bash=
blacklist nfc
blacklist pn533
blacklist pn533_usb
```
```
modprobe -r pn533_usb
modprobe -r pn533
modprobe -r nfc
```
`sudo service restart pcscd`

### sense-hat Installation

`sudo apt install sense-hat`
`sudo reboot`
`pip install sense-hat`


### paho mqtt installation

* sudo apt install mosquitto mosquitto-clients

Il vous faudra créer un fichier de users mosquitto


`mosquitto_passwd -c <passwordfile> <username>` (username required to create the file)

**add user and pwd:** `mosquitto_passwd -b <passwordfile> <user> <password>`

**delete user:** `mosquitto_passwd -D <passwordfile> <user>`

copy the password file to /etc/mosquitto and update file mosquitto.conf

```
allow_anonymous false
password_file <path>
```

reload the mosquitto service to reload configuration file

* pip install paho-mqtt
[paho documentation](https://pypi.org/project/paho-mqtt/)

###SQLite configuration

* pip install pysqlite3 db-sqlite3
