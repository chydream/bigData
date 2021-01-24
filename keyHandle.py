# from pynput.mouse import  Button, Controller
from Demos.print_desktop import l
from pynput import mouse
import ctypes
# from pynput.keyboard import Key, Controller
from pynput import keyboard
# 设置缩放属性
PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)

def on_activate_h():
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')

with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+h': on_activate_h,
    '<ctrl>+<alt>+i': on_activate_i
}) as h:
    h.join()



# def on_activate():
#     print('Global hotkey activated!')
#
# def for_canonical(f):
#     return lambda k: f(l.canonical(k))
#
# hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+h'), on_activate)
#
# with keyboard.Listener(on_press=for_canonical(hotkey.press),
#                        on_release=for_canonical(hotkey.release)) as l:
#     l.join()


# with keyboard.Events() as events:
#     for event in events:
#         if event.key == keyboard.Key.esc:
#             break
#         else:
#             print('Received event {}'.format(event))


    # event = events.get(1.0)
    # if event is None:
    #     print('you did not press a key within one second')
    # else:
    #     print('Received event {}'.format(event))




# class MyException(Exception):
#     pass
#
# def on_press(key):
#     if key == keyboard.Key.esc:
#         raise MyException(key)
#
# with keyboard.Listener(on_press=on_press) as listener:
#     try:
#         listener.join()
#     except MyException as e:
#         print('{0} was pressed'.format(e.args[0]))



# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(key))
#
# def on_release(key):
#     print('{0} released'.format(key))
#     if key == keyboard.Key.esc:
#         return False
#
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

# keyboard = Controller()
# keyboard.press(Key.space)
# keyboard.release(Key.space)
# keyboard.press('a')
# keyboard.release('a')
# keyboard.press('A')
# keyboard.release('A')
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')
# keyboard.type('Hello World')

# a  aA aA  aAAHello World

# with mouse.Events() as events:
#     for event in events:
#         # print('Received event {}'.format(event))
#         print()
#         if hasattr(event, 'button'):
#             if event.button == mouse.Button.right:
#                 break
#         print('Received event {}'.format(event))

    # event = events.get(1.0)
    # if event is None:
    #     print('You did not interact with the mouse within one second')
    # else:
    #     print('Received event {}'.format(event))



# class MyException(Exception):
#     pass
#
# def on_click(x, y, button, pressed):
#     if button == mouse.Button.left:
#         raise MyException(button)
#
# with mouse.Listener(on_click=on_click) as listener:
#     try:
#         listener.join()
#     except MyException as e:
#         print('{0} was clicked'.format(e.args[0]))


# def on_move(x, y):
#     print('移动到{0}'.format((x, y)))
#
# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format('pressed' if pressed else 'Released', (x, y)))
#     if not pressed:
#         return False
#
# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format('down' if dy<0 else 'up', (x, y)))
#
# with mouse.Listener(on_move=on_move,
#                     on_click=on_click,
#                     on_scroll=on_scroll) as listener:
#     listener.join()




# mouse = Controller()
# print(dir(mouse))
# print('当前位置是{0}'.format(mouse.position))
# mouse.position = (10, 20)
# print('当前移动到{0}'.format(mouse.position))
# mouse.move(5,-5)
# mouse.press(Button.left)
# mouse.release(Button.left)
# mouse.click(Button.left, 2) #双击
# mouse.scroll(0, 2)