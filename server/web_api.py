from bottle import route, get, post, delete, hook, response, request

from components.user import User
from components.auth_log import AuthLog
from utils.authenticate import authenticate as auth_verification

import json

@post('/users')
@auth_verification
def add_user(user=None):
    data = json.loads(request.body.read())
    user_created = User().create_user(data)
    return user_created

@get('/users')
@auth_verification
def get_users(user=None):

    users = User().get_users()
    if users == 1:
        return {}

    return users

@delete('/users')
@auth_verification
def delete_user(user=None):
    data = json.loads(request.body.read())
    card_uid = data.get('card_uid')

    users = User().delete_user(card_uid)
    if users == 1:
        return {}

    return users

@post('/authenticate')
def authenticate():
    data = json.loads(request.body.read())
    login = data.get('login')
    password = data.get('password')

    my_response = User().basic_authentication(login, password)
    if my_response == 1:
        response.status = 401
        return { "error": "Failed Authentication." }
    return my_response
@get('/auth_log')
@auth_verification
def get_auth_log(user=None):
    data = request.query.decode()
    card_uid = data.get('card_uid', None)
    limit = data.get('limit', None)

    return AuthLog().get(card_uid, limit)

@delete('/auth_log')
@auth_verification
def delete_auth_log(user = None):
    data = json.loads(request.body.read())
    card_uid = data.get('card_uid', None)

    if card_uid == None:
        return AuthLog().delete()
    return AuthLog().delete([('card_uid', card_uid)])

@get('/stats')
@auth_verification
def get_stats(user=None):
    data = request.query.decode()
    filter = data.get('filter', 'hour')

    return AuthLog().get_stats(filter)

@hook('after_request')
#@bottle.route('/:#.*#', method='OPTIONS')  # Also tried old syntax.
def enableCORSGenericRoute():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, PATCH, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization'

@route('/', method = 'OPTIONS')
@route('/<path:path>', method = 'OPTIONS')
def options_handler(path = None):
    return


#run(host='0.0.0.0', port=8000, debug=False, reloader=True)
