from bottle import route, get, post, delete, hook, response, request

from components.user import User
from components.auth_log import AuthLog

import json

@post('/users')
def add_user():
    data = json.loads(request.body.read())
    user_created = User().create_user(data)
    return user_created

@post('/authenticate')
def authenticate():
    data = json.loads(request.body.read())
    login = data.get('login')
    password = data.get('password')
    return User().basic_authentication(login, password)

@get('/auth_log')
def get_auth_log():
    data = json.loads(request.body.read())
    card_uid = data.get('card_uid', None)

    return AuthLog().get(card_uid)

@delete('/auth_log')
def delete_auth_log():
    data = json.loads(request.body.read())
    card_uid = data.get('card_uid', None)

    if card_uid == None:
        return AuthLog().delete()
    return AuthLog().delete([('card_uid', card_uid)])

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
