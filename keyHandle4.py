import os
import signal
import threading
import time

from datetime import datetime
from pynput import keyboard
from pynput import mouse

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

# 上滑
def scroll_up(m):
    m.press(mouse.Button.left)
    m.move(0, -30)
    time.sleep(1)
    m.release(mouse.Button.left)
    time.sleep(3)
    m.move(0, 30)

def run_time(m, p):
    k = keyboard.Controller()
    mc = mouse.Controller()
    n = time.mktime(datetime.now().timetuple())
    i = 1
    while True:
        if flag:
            t = time.mktime(datetime.now().timetuple())
            if t == n + (m * 60) * i:
                i = i + 1
                mc.position = (1806, 236)
                time.sleep(1)
                mc.press(mouse.Button.left)
                mc.release(mouse.Button.left)
                time.sleep(1)
                mc.position = (1789, 875)
                mc.press(mouse.Button.left)
                mc.press(mouse.Button.left)
                time.sleep(1)
                time.sleep(32)
                # mc.position = (1821,141)
                # mc.press(mouse.Button.left)
                # mc.press(mouse.Button.left)
                time.sleep(1)
            else:
                time.sleep(1)
            if (i-1) == p:
                break
        else:
            continue


if __name__ == '__main__':
    
    run_time(10, 36)
