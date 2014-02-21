from BaseHTTPServer import HTTPServer
from thread import start_new_thread

__all__ = ['start']

def start_http_server(port, handler):
    HTTPServer(("127.0.0.1", port), handler).serve_forever()

def start(ports, handler):
    for port in ports:
        start_new_thread(start_http_server, (port, handler))
        print 'Start HTTP server on port %d' % (port,)
