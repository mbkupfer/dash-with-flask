from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from frontend import app as frontend
from backend import app as backend
from dash_app import app as dash_app

application = DispatcherMiddleware(frontend, {
    '/backend': backend,
    '/my-app' : dash_app.server
})

if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port = 5000,
        application = application,
        use_reloader=True)
