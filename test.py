#!/usr/bin/env python3

import platform

import thunk

if platform.system() == 'Darwin':
	hello_world_x64_macos = \
		b'\x48\x8D\x35\x12\x00\x00\x00' + \
		b'\xBA\x0E\x00\x00\x00' + \
		b'\xBF\x01\x00\x00\x00' + \
		b'\xB8\x04\x00\x00\x02' + \
		b'\x0F\x05' + \
		b'\xC3' + \
		b'\x48\x65\x6C\x6C\x6F\x2C\x20\x77\x6F\x72\x6C\x64\x21\x0A'

	thunk.doit(hello_world_x64_macos)
else:
	raise Exception('unsupported: %s' % platform.system())
