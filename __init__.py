# tell Binary Ninja we're a plugin

from binaryninja.plugin import PluginCommand

from . import thunk

def on_select(bv, start, length):
	shellcode = bv.read(start, length)
	thunk.doit(shellcode)

PluginCommand.register_for_range('call shellcode', 'call selected code (dangerous!)', on_select)
