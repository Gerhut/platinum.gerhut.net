#coding:utf-8

from BaseHTTPServer import BaseHTTPRequestHandler
import screenshots
import multiservers

class ScreenShotHandler(BaseHTTPRequestHandler):
    def log_message(*args, **kwargs):
        pass
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.send_header('Content-Length', len(screenshots.images['No$gba Emulator ']))
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Pragma', 'no-cache')
        self.end_headers()
        self.wfile.write(screenshots.images['No$gba Emulator '])
        self.wfile.close()

multiservers.start((1000,), ScreenShotHandler)
screenshots.start('No$gba Emulator ')
