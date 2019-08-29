
import time
from console import fg, bg, fx 
import console
import os  
from ctypes import *
import struct
from matrixLine import MatrixLine



###  https://rosettacode.org/wiki/Terminal_control/Cursor_positioning#Python ###
class COORD(Structure):
    pass
STD_OUTPUT_HANDLE = -11
COORD._fields_ = [("X", c_short), ("Y", c_short)]
 
def print_at(r, c, s):
    dims = get_terminal_size_windows()
    if r >= dims [1] or c >= dims[0] or r < 0 or c < 0:
        return
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
    
    c = s.encode("UTF-8")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
### END  https://rosettacode.org/wiki/Terminal_control/Cursor_positioning#Python ###



###from https://gist.github.com/jtriley/1108174
def get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass



    