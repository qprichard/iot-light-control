"""
Authenticate decorator that return the current user data if exist
and raise error if not
"""
from bottle import response, request
from public.config import JWT_SECRET_KEY
from functools import wraps
from components.db import my_database as db

import jwt

class AuthException(Exception):
    pass

def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization')

        try:
            if auth is None:
                raise AuthException('no token provided')

            results = db.select('tokens', conditions=[('token', auth)])

            if not len(results):
                raise AuthException('invalid token')
            token = results[0]['token']
            decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            results = db.select('users', conditions=[('login', decoded['login'])])

            if not len(results):
                raise AuthException('invalid token')

            return f(user=results[0], *args, **kwargs)
        except AuthException as e:
             response.status = 401
             e = str(e)
             return { "error": e }

    return wrapper
