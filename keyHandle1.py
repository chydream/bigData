import os
import signal
import threading
import time
from pynput import keyboard

print('ESC=退出程序 F11=停止程序 F12=开始程序')
flag = True

def stop():
    def on_press(key):
        pass
    def on_release(key):
        global flag
        if key == keyboard.Key.esc:
            print('退出')
            os.kill(os.getpid(), signal.SIGTERM)
        elif key == keyboard.Key.f12:
            print('开始')
            flag = True
        elif key == keyboard.Key.f11:
            print('停止')
            flag = False
        else:
            pass
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

t = threading.Thread(target=stop)
t.start()

def main():
    print('正在..')
    c = keyboard.Controller()
    while True:
        if flag:
            c.press('m')
            c.release('m')
            print('m')
            time.sleep(190)
        else:
            continue

print('182s后自动开始程序')
time.sleep(190)
main()