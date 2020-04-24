# py->binary (.so/.dylib/.dll) thunk
#
# this is separate from __init__.py to allow testing without Binary Ninja

import os
import binascii
import platform

from ctypes import *

def doit(shellcode):
	shellcode_str = binascii.hexlify(shellcode).decode('utf-8')
	print('THUNK: running', shellcode_str)
	
	fpath = os.path.abspath(__file__)
	fpath = os.path.dirname(fpath)
	if platform.system() == 'Darwin':
		fpath = os.path.join(fpath, 'callbuf.dylib')

	print('THUNK: loading', fpath)
	dll = CDLL(fpath)

	print('THUNK: calling')
	rc = dll.doit(c_char_p(shellcode), len(shellcode))

	print('THUNK: returned %d' % rc)
