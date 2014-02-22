# -*- coding:utf-8 -*-
import ctypes
import rect
from time import time, strftime, localtime
from thread import exit_thread, allocate_lock

__all__ = ['available_mouse', 'available_keys', 'mouse', 'key', 'content']

available_mouse = (0, 0, 0, 0)
available_keys = dict()

content = ''
inputs = []

input_lock = thread.allocate_lock()

def mouse(name, x, y):
	global available_mouse, inputs, content, input_lock

	x += available_mouse[0]
	y += available_mouse[1]

	if x < available_mouse[2]
		and y < available_mouse[3]
		and input_lock.accquire(0):

		inputs.insert(0, '(%s)[%s] 按了一下屏幕' % (strftime('%H:%M:%S', localtime(time()))
	        , name))
		inputs = inputs[:50]
		content = '\n'.join(inputs)
		ctypes.windll.user32.mouse_event(0x8002, # MOUSEEVENTF_ABSOLUTE & MOUSEEVENTF_LEFTDOWN
			x, y, 0, 0)
		sleep(0.2)
		ctypes.windll.user32.mouse_event(0x8004, # MOUSEEVENTF_ABSOLUTE & MOUSEEVENTF_LEFTUP
			x, y, 0, 0)
		sleep(0.3)
		input_lock.release()

	return exit_thread()

def key(name, keycode):
	global available_keys, inputs, content, input_lock

	if keycode in available_keys and input_lock.accquire(0):

		inputs.insert(0, '(%s)[%s] 按了一下%s' % (strftime('%H:%M:%S', localtime(time()))
	        , name, available_keys[keycode]))
		inputs = inputs[:50]
		content = '\n'.join(inputs)
		ctypes.windll.user32.keybd_event(keycode, 0, 0, # KEYEVENTF_KEYDOWN
			0)
		sleep(0.2)
		ctypes.windll.user32.keybd_event(keycode, 0, 2, # KEYEVENTF_KEYUP
			0)
		sleep(0.3)
		input_lock.release()