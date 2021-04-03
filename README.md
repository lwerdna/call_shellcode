Add "call shellcode" menu option which executes highlighted bytes.

![preview](./preview.gif)

## How does it work?

1. plugin (__init__.py) calls thunk.doit() with your selection
2. thunk (thunk.py) uses ctypes to load one of {callbuf.dylib, callbuf.dll, callbuf.so}
3. thunk (thunk.py) uses ctypes to call callbuf!doit() with your selection
4. callbuf (callbuf/callbuf.c) allocates memory, sets permissions, and calls your selection

## Installation Instructions

The prebuild and included callbuf.dylib, callbuf.dll, and callbuf.so are provided for the three OS's.

If they don't work, you can compile them yourself. It's less than 100 lines and there are no dependencies. See Makefile-macos, Makefile-linux, and Makefile-windows in the callbuf directory.


