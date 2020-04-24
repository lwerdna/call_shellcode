from binaryninja.plugin import PluginCommand

import os
import binascii
import platform

from ctypes import *

def run_that_code(bv, start, length):
	shellcode = bv.read(start, length)
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

PluginCommand.register_for_range('run shellcode', 'run selected code (dangerous!)', run_that_code)
