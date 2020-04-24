from binaryninja.plugin import PluginCommand

import binascii

def run_that_code(bv, start, length):
	shellcode = bv.read(start, length)
	shellcode_str = binascii.hexlify(shellcode).decode('utf-8')
	print('running: ', shellcode_str)

PluginCommand.register_for_range('run shellcode', 'run selected code (dangerous!)', run_that_code)
