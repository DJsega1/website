from website import __init__
from functools import wraps


def no_cache(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        resp = func(*args, **kwargs)
        resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        resp.headers['Cache-Control'] = 'public, max-age=0'
        return resp
    return decorated
