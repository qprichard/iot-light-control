import hashlib, binascii, os, jwt, json, time, datetime

from public.config import JWT_SECRET_KEY
from components.db import my_database as db

class FailedAuth(Exception):
    pass

class User():
    def card_authentication(self, data):
        if data['flag'] == "authentication":
            results = db.select(table='users', conditions=[("card_uid", data["card_uid"])])
            if len(results) > 0 :
                data['authorization'] = 1
                data['last_name'] = results[0]["last_name"]
                data['first_name'] = results[0]["first_name"]
            else:
                # Si authorization failed enregistrer dans une table pour permettre
                # de proposer à l'admin de l'enregistrer en tant que user
                data['authorization'] = 0

            now = datetime.datetime.now()
            now = now.strftime('%Y-%m-%d %H:%M:%S')
            db.insert('auth_log', (data['card_uid'], now))

        return data

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def create_user(self, data):
        login = data.get('login')
        last_name = data.get('last_name')
        first_name = data.get('first_name')
        card_uid = data.get('card_uid')
        password = data.get('password')
        password = self.hash_password(password)

        try:
            db.insert('users', (card_uid, last_name, first_name, login, password))
            db.delete('auth_log', [('card_uid', card_uid)])

            results = db.select('users', conditions=[('login', login)])
            if len(results) == 0:
                return 1

            del results[0]['id']
            del results[0]['password']
            return results[0]

        except Exception as e:
            print(e)
            return 1

    def basic_authentication(self, login, password):
        try:
            results = db.select(table='users', conditions=[('login', login)])

            if len(results) == 0:
                raise FailedAuth
            if self.verify_password(results[0]['password'],password):
                token = jwt.encode({'login': login}, JWT_SECRET_KEY, algorithm='HS256')
                token = token.decode('utf-8')
                token = str(token)
                db.insert('tokens', [token])
                del results[0]['id']
                del results[0]['password']
                return {'user': results[0], 'token': token }

            raise FailedAuth

        except FailedAuth:
            print('Failed authentication')
            return 1
        except Exception as e:
            print(e)
            return 1
