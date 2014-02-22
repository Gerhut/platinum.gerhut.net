#coding:utf-8

import ctypes
from StringIO import StringIO
from time import sleep
from ImageGrab import grab

__all__ = ['image', 'delay', 'start']

image = ''
delay = .1

rect = None

class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long),
                ('top', ctypes.c_long),
                ('width', ctypes.c_long),
                ('height', ctypes.c_long)]
    def bbox(self):
        yield self.left
        yield self.top
        yield self.left + self.width
        yield self.top + self.height

def shotScreen():
    global image, rect
    print 'Start screenshotting.'
    while True:
        stringIO = StringIO()
        try:
            grab(rect).save(stringIO, 'PNG')
            image = stringIO.getvalue()
        except IOError:
            print 'Screennshotting failed.'
        finally:
            stringIO.close()
        sleep(delay)

def start(title):
    global rect
    while True:
        hwnd = ctypes.windll.user32.FindWindowA(None, title)
        if hwnd != 0:
            rect = RECT()
            ctypes.windll.user32.ShowWindow(hwnd, 9) # SW_RESTORE
            ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(rect))
            ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(rect))
            rect = tuple(rect.bbox())
            break
        print 'Cannot find the window to grab.'
        sleep(delay)
        continue

    shotScreen()