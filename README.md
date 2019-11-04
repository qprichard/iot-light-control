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


### paho mqtt installation

* sudo apt install mosquitto mosquitto-clients

Il vous faudra créer un fichier de users mosquitto
[source]([paho documentation](https://pypi.org/project/paho-mqtt/))


`mosquitto_passwd -c <passwordfile> <username>` (username required to create the file)

**add user and pwd:** `mosquitto_passwd -b <passwordfile> <user> <password>`

**delete user:** `mosquitto_passwd -D <passwordfile> <user>`

copy the password file to /etc/mosquitto and update file mosquitto.conf

```
allow_anonymous false
password_file <path>
```

reload the mosquitto service to reload configuration file


[paho documentation](https://pypi.org/project/paho-mqtt/)

###SQLite configuration

* pip install pysqlite3 db-sqlite3
