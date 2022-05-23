import ctypes
import os
import platform
from ctypes import cdll

CGOFunc = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
current_path = os.path.abspath(__file__)
lib_file_path = os.path.dirname(current_path)
sym = platform.system().lower()
#print(sym)
if sym == 'windows':
    lib_file_path += "/degate.dll"
elif sym == 'darwin':
    pm = platform.platform().lower()
    #print(pm)
    if 'arm' in pm:
        lib_file_path += "/degate_mac_m1.so"
    else:
        lib_file_path += "/degate_mac.so"
else:
    lib_file_path += "/degate_linux.so"

libgo = cdll.LoadLibrary(lib_file_path)
libgo.send_request.restype = ctypes.c_char_p
libgo.send_subscribe.restype = ctypes.c_char_p