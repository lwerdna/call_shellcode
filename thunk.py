# py->binary (.so/.dylib/.dll) thunk
#
# this is separate from __init__.py to allow testing without Binary Ninja

import os
import binascii
import platform
import threading

import ctypes

def doit_worker(dll, shellcode):
	dynamic_type = {'Darwin':'dylib', 'Windows':'dll', 'Linux':'so'}[platform.system()]
	ccp = ctypes.c_char_p(shellcode)
	scaddr = ctypes.cast(ccp, ctypes.c_void_p).value
	print('THUNK: calling to %s.doit(0x%X, 0x%X)' % (dynamic_type, scaddr, len(shellcode)))
	rc = dll.doit(ccp, len(shellcode))
	print('THUNK: %s returned %d' % (dynamic_type, rc))

def doit(shellcode, use_thread=True):
	shellcode_str = binascii.hexlify(shellcode).decode('utf-8')
	#shellcode_str = ' '.join([shellcode_str[x:x+2] for x in range(0,len(shellcode_str),2)])
	print('THUNK: running', shellcode_str)

	# resolve path to dll
	fpath = os.path.abspath(__file__)
	fpath = os.path.dirname(fpath)
	fpath = os.path.join(fpath, 'callbuf')
	if platform.system() == 'Darwin':
		fpath = os.path.join(fpath, 'callbuf.dylib')
	elif platform.system() == 'Windows':
		fpath = os.path.join(fpath, 'callbuf.dll')

	# load dll
	print('THUNK: loading', fpath)
	dll = ctypes.CDLL(fpath)

	# call into dll
	if use_thread:
		print('THUNK: creating thread')
		threading.Thread(target=doit_worker, args=(dll, shellcode)).start()
	else:
		doit_worker(shellcode)

	print('THUNK: returning')
