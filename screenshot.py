from StringIO import StringIO
from time import sleep
from ImageGrab import grab
import rect

__all__ = ['image', 'delay', 'start']

image = ''
delay = .1

def shotScreen(rect):
    global image
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
    shotScreen(rect.get(title))
