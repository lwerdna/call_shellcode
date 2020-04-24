# call to the .so/.dylib/.dll to run code
#
# this is separate from __init__.py to allow testing without Binary Ninja

import os
import binascii
import platform

from ctypes import *

def run_that_code(shellcode):
	shellcode_str = binascii.hexlify(shellcode).decode('utf-8')
	print('running: ', shellcode_str)
	
	fpath = os.path.abspath(__file__)
	fpath = os.path.dirname(fpath)
	if platform.system() == 'Darwin':
		fpath = os.path.join(fpath, 'callbuf.dylib')

	print('loading: ', fpath)
	dll = CDLL(fpath)

	print('calling')
	rc = dll.doit(c_char_p(shellcode), len(shellcode))
	print('returned %d' % rc)
