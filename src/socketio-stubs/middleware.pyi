import engineio

class WSGIApp(engineio.WSGIApp):
    def __init__(self, socketio_app, wsgi_app=None, static_files=None, socketio_path: str = 'socket.io') -> None: ...

class Middleware(WSGIApp):
    def __init__(self, socketio_app, wsgi_app=None, socketio_path: str = 'socket.io') -> None: ...
