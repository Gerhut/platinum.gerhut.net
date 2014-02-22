#coding:utf-8

from BaseHTTPServer import BaseHTTPRequestHandler
from urllib import unquote
from json import dump
from os import system
from thread import start_new_thread
from sys import exc_info

import screenshot
import multiservers
import chat
import inputs

class MultiPokeHandler(BaseHTTPRequestHandler):
    def log_message(*args, **kwargs):
        pass
    def send_screen_shot(self):
        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.send_header('Content-Length', len(screenshots.images['No$gba Emulator ']))
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Pragma', 'no-cache')
        self.end_headers()
        self.wfile.write(screenshot.image)
        self.wfile.close()
    def send_chat(self, callback_name):
        self.send_response(200)
        self.send_header('Content-Type', 'application/javascript')
        self.end_headers()
        self.wfile.write(callback_name)
        self.wfile.write('(')
        dump(chat.content, self.wfile)
        self.wfile.write(')')
        self.wfile.close()
    def send_inputs(self, callback_name):
        self.send_response(200)
        self.send_header('Content-Type', 'application/javascript')
        self.end_headers()
        self.wfile.write(callback_name)
        self.wfile.write('(')
        dump(inputs.content, self.wfile)
        self.wfile.write(')')
        self.wfile.close()
    def do_GET(self):
        try:
            if self.path.startswith('/?'):
                self.send_screen_shot()
            elif self.path.startswith('/chat'):
                path = self.path[5:]

                callback_index = path.find('?callback=')
                if callback_index == -1:
                    return self.send_error(400, 'Callback required'.)
                callback_name = path[callback_index + 10:]

                path = path[:callback_index]
                
                if path.startswith('/'):
                    components = path.split('/')
                    if len(components) == 3:
                        chat.add(unquote(components[1]), unquote(components[2]))

                self.send_chat(callback_name)
            elif self.path.startswith('/input'):
                path = self.path[6:]

                callback_index = path.find('?callback=')
                if callback_index == -1:
                    return self.send_error(400, 'Callback required'.)
                callback_name = path[callback_index + 10:]

                path = path[:callback_index]

                if path.startswith('/'):
                    components = path.split('/')
                    if len(components) == 4:
                        if components[2] == 'key':
                            start_new_thread(inputs.key, (unquote(components[1]), int(components[3])))
                        elif components[2] == 'mouse':
                            (x, y) = components[3].split(',')
                            start_new_thread(inputs.mouse, (unquote(components[1]), int(x), int(y)))
                self.send_chat(callback_name)
            else:
                self.send_error(400, 'Invalid request.')
        except:
            print exc_info()
            self.send_error(400, 'Invalid request.')

system('run')
inputs.available_mouse = rect.get('No$gba Emulator ')
inputs.available_keys = {
    0x57: '上',
    0x53: '下',
    0x41: '左',
    0x44: '右',
    0x5A: 'Ａ',
    0x58: 'Ｂ',
#    0x52: '选择',
    0x46: '开始',
    0x51: 'Ｌ',
    0x45: 'Ｒ',
    0x43: 'Ｘ',
    0x56: 'Ｙ',
}
multiservers.start(range(4931, 4940), MultiPokeHandler)
screenshot.start('No$gba Emulator ')
