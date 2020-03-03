import pynput.keyboard as k
import time
import threading as t
import pynput.mouse as m
c1=m.Controller()
c2=k.Controller()
b=m.Button
ch='t'
repeat='y'
def click():
    global repeat
    global ch
    while repeat=='y':
        pause=float(input('duration for a pause: '))
        ch='t'
        while ch=='t':
            time.sleep(pause)
            c1.press(m.Button.left)
            c1.release(m.Button.left)
        repeat=input('would you like to repeat? y/n')

def quit():
    
    global repeat
    if repeat == 'y':
        def on_press(key):
            pass
            #print(key)
        #        n=-1
        def on_release(key):
            if(key==k.Key.esc):
                print('exit')
                #t1.   op()
                global ch
                ch='f'
                #print(ch)
                #ch=0
                #print(ch)
                # return False

        #print('a')
        with k.Listener(on_press=on_press,on_release=on_release) as l:
            l.join()

def run():
    t1=t.Thread(target=click)

    t2=t.Thread(target=quit)
    t1.start()
    t2.start()

run()