import http.server
import socketserver
import socket

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(bytes('Hello world from ' + socket.gethostname(), 'utf-8'))

httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
