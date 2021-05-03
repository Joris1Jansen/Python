import threading
import time

def func():
    print('ran')
    time.sleep(2)
    print('done')

print(threading.activeCount())
x = threading.Thread(target=func, args=())
x.start()
print('In betweeeen')

print(threading.activeCount())