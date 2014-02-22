import ctypes
from time import sleep

__all__ = ['get']

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

_title = None
_rect = None

def get(title = None):
    global _title, _rect
    if title != _title:
        while True:
            hwnd = ctypes.windll.user32.FindWindowA(None, title)
            if hwnd != 0:
                ctypes.windll.user32.SetForegroundWindow(hwnd)
                _rect = RECT()
                ctypes.windll.user32.ShowWindow(hwnd, 9) # SW_RESTORE
                ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(_rect))
                ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(_rect))
                _rect = tuple(_rect.bbox())
                _title = title
                break
            sleep(.1)
    return _rect
