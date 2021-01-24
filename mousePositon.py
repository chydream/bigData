from pynput import mouse

def on_move(x, y):
    pass
    # print('当前鼠标位置{}'.format((x, y)))

def on_click(x, y, button, pressed):
    print(x,y)
    if button == mouse.Button.right:
        return False
    # print(x,y)
    # print(button)
    # print(pressed)

def on_scroll(x, y, dx, dy):
    pass
    # print(dx)
    # print(dy)
    # print(x, y)

listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listener.start()