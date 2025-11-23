from tornado.websocket import WebSocketHandler

from socketio.server import Server

def get_tornado_handler(socketio_server: Server) -> WebSocketHandler: ...
