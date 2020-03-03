
import pynput.keyboard as k

c=k.Controller()


def on_press(key):
    pass


def on_release(key):
    if(key==k.Key.esc):
        exit()
    if(key==k.Key.left):
        print('l')
        c.press(k.Key.shift)
        c.press(k.Key.ctrl)
        c.press('a')
        c.release(k.Key.shift)
        c.release(k.Key.ctrl)
        c.release('a')

while(True):        
    with k.Listener(on_press=on_press,on_release=on_release) as l:
        l.join()


