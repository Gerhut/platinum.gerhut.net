#coding:utf-8

import ctypes
from StringIO import StringIO
from time import sleep
from ImageGrab import grab

__all__ = ['shots', 'delay', 'start']

images = dict()
delay = .1

rects = dict()

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

def grabRects(titles):
    global rects
    toGets = list(titles)
    while toGets:
        for toGet in toGets:
            hwnd = ctypes.windll.user32.FindWindowA(None, toGet)
            if hwnd == 0:
                continue
            rect = RECT()
            ctypes.windll.user32.ShowWindow(hwnd, 9) # SW_RESTORE
            ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(rect))
            ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(rect))
            rects[toGet] = tuple(rect.bbox())
            print toGet + ' rect grabbed.'
            toGets.remove(toGet)
        sleep(delay)

    shotScreen()

def shotScreen():
    global shots, rects
    print 'start screenshotting.'
    while True:
        for title in rects:
            stringIO = StringIO()
            grab(rects[title]).save(stringIO, 'PNG')
            images[title] = stringIO.getvalue()
            stringIO.close()
        sleep(delay)

def start(titles, newThread=True):
    if isinstance(titles, basestring):
        titles = (titles,)
    grabRects(titles)