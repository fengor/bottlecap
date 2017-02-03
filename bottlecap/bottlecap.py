from bottle import request, HTTPResponse
from functools import wraps


def auth_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if check_permission(request.auth):
            return view(*args, **kwargs)
        return access_denied()
    return wrapper


def role_required(view, role):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if check_permission(request.auth, role):
            return view(*args, **kwargs)
        return access_denied()
    return wrapper


def check_permission(auth, role=None):
    return True


def access_denied():
    return HTTPResponse(status=401, body='Access denied!',
                        headers={'WWW-Authenticate': 'Basic Realm="%s"' %
                                 'bottlecap'})
