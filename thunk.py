# py->binary (.so/.dylib/.dll) thunk
#
# this is separate from __init__.py to allow testing without Binary Ninja

import os
import binascii
import platform
import threading

from ctypes import *

def call_dll(dll, shellcode):
	print('THUNK: calling to dll')
	rc = dll.doit(c_char_p(shellcode), len(shellcode))
	print('THUNK: dll returned %d' % rc)

def doit(shellcode, use_thread=True):
	shellcode_str = binascii.hexlify(shellcode).decode('utf-8')
	print('THUNK: running', shellcode_str)

	# resolve path to dll
	fpath = os.path.abspath(__file__)
	fpath = os.path.dirname(fpath)
	if platform.system() == 'Darwin':
		fpath = os.path.join(fpath, 'callbuf.dylib')

	# load dll
	print('THUNK: loading', fpath)
	dll = CDLL(fpath)

	# call into dll
	if use_thread:
		print('THUNK: creating thread')
		threading.Thread(target=call_dll, args=(dll, shellcode)).start()
	else:
		call_dll(shellcode)

	print('THUNK: returning')
