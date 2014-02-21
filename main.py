#coding:utf-8

from BaseHTTPServer import BaseHTTPRequestHandler
from urllib import unquote

import screenshots
import multiservers
import chat

class MultiPokeHandler(BaseHTTPRequestHandler):
    chat_content = ''
    def log_message(*args, **kwargs):
        pass
    def send_screen_shot(self):
        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.send_header('Content-Length', len(screenshots.images['No$gba Emulator ']))
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Pragma', 'no-cache')
        self.end_headers()
        self.wfile.write(screenshots.images['No$gba Emulator '])
        self.wfile.close()
    def send_chat(self, callback_name):
        self.send_response(200)
        self.send_header('Content-Type', 'application/javascript')
        self.end_headers()
        self.wfile.write(chat.content)
        self.wfile.close()
    def do_GET(self):
        if self.path == '/':
            self.send_screen_shot()
        elif self.path.startswith('/chat'):
            path = self.path[5:]

            callback_index = path.find('?callback=')
            if callback_index == -1:
                return self.send_error(400)
            callback_name = path[callback_index + 10:]

            path = path[:callback_index]
            if path[0] == '/':
                components = path.split('/')
                if len(components) == 3:
                    chat.add(unquote(components[1]), unquote(components[2]))

            self.send_chat(callback_name)




multiservers.start((1000,), ScreenShotHandler)
screenshots.start('No$gba Emulator ')
