from suppliments import keyboard_input as key

path=input('path of destination :')


import pynput.keyboard as k
import time
import threading as t
import pynput.mouse as m
c1=m.Controller()
c2=k.Controller()
b=m.Button
ch='t'
repeat='y'
def copy():
        s=key.keyboard_read()
        f=open(path,'a')
        f.write('\n\n'+s)
        f.close()
        # repeat=input('would you like to repeat? y/n')
def quit():
    
    global repeat
    if repeat == 'y':
        def on_press(key):
            pass
            #print(key)
        #        n=-1
        def on_release(key):
            if(key==k.Key.esc):
                exit()
            if(key==k.Key.enter):
                copy()
            
                #print(ch)
                #ch=0
                #print(ch)
            
                # return False

        #print('a')
        with k.Listener(on_press=on_press,on_release=on_release) as l:
            l.join()

def run():

    t2=t.Thread(target=quit)
    t2.start()

run()


