# tell Binary Ninja we're a plugin

from binaryninja.plugin import PluginCommand

from . import callbuf

def on_select(bv, start, length):
	shellcode = bv.read(start, length)
	callbuf.run_that_code(shellcode)

PluginCommand.register_for_range('run shellcode', 'run selected code (dangerous!)', on_select)
