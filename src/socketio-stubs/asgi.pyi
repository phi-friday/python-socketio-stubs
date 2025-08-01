import engineio

class ASGIApp(engineio.ASGIApp):
    def __init__(self, socketio_server, other_asgi_app=None, static_files=None, socketio_path: str = 'socket.io', on_startup=None, on_shutdown=None) -> None: ...
