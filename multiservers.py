from BaseHTTPServer import HTTPServer
from thread import start_new_thread

__all__ = ['start']

def start_http_server(port, handler):
    HTTPServer(("", port), handler).serve_forever()

def start(ports, handler):
    for port in ports:
        start_new_thread(start_http_server, (port, handler))
