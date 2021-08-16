import os, random, time
#pip install pywin32
import win32gui
from win32api import GetSystemMetrics

_Scr_Width = GetSystemMetrics(0)
_Scr_Height = GetSystemMetrics(1)
num_windows = 2

for i in range(num_windows):
    os.system(f'start "win {i}" '
              f'cmd /c "cd /windows'
              f' && dir /s"')
    time.sleep(0.2)
    handle = win32gui.FindWindow(0, f'win {i}')
    win32gui.MoveWindow(
        handle,
        random.randrange(_Scr_Width),
        random.randrange(_Scr_Height),
        700, 400, True)