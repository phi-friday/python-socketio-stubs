from socketio.server import Server
from tornado.websocket import WebSocketHandler

def get_tornado_handler(socketio_server: Server) -> WebSocketHandler: ...
