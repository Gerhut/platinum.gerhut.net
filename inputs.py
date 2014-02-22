# -*- coding:utf-8 -*-
import ctypes
import rect
from time import time, strftime, localtime, sleep
from thread import start_new_thread, exit_thread, allocate_lock

__all__ = ['available_mouse', 'available_keys', 'mouse', 'key', 'content']

available_mouse = (0, 0, 0, 0)
available_keys = dict()

content = ''
inputs = []

input_lock = allocate_lock()

width = ctypes.windll.user32.GetSystemMetrics(0)
height = ctypes.windll.user32.GetSystemMetrics(1)

def mouse(name, x, y):
    global available_mouse, inputs, content, input_lock
    
    def _mouse(x, y):
        ctypes.windll.user32.SetCursorPos(x, y)
        ctypes.windll.user32.mouse_event(2, # MOUSEEVENTF_LEFTDOWN
            0, 0, 0, 0)
        sleep(0.2)
        ctypes.windll.user32.mouse_event(4, # MOUSEEVENTF_LEFTUP
            0, 0, 0, 0)
        sleep(0.3)
        input_lock.release()
        return exit_thread()

    x += available_mouse[0]
    y += available_mouse[1]

    if x < available_mouse[2] and y < available_mouse[3] and input_lock.acquire(0):
        inputs.insert(0, '(%s)[%s] 按了一下屏幕' % (strftime('%H:%M:%S', localtime(time()))
            , name))
        inputs = inputs[:50]
        content = '\n'.join(inputs)
        start_new_thread(_mouse, (x, y))

def key(name, keycode):
    global available_keys, inputs, content, input_lock
    
    def _key(keycode):
        ctypes.windll.user32.keybd_event(keycode, 0, 0, # KEYEVENTF_KEYDOWN
            0)
        sleep(1)
        ctypes.windll.user32.keybd_event(keycode, 0, 2, # KEYEVENTF_KEYUP
            0)
        sleep(0.3)
        input_lock.release()
        return exit_thread()

    if keycode in available_keys and input_lock.acquire(0):
        inputs.insert(0, '(%s)[%s] 按了一下%s' % (strftime('%H:%M:%S', localtime(time()))
            , name, available_keys[keycode]))
        inputs = inputs[:50]
        content = '\n'.join(inputs)
        start_new_thread(_key, (keycode,))

    return exit_thread()
