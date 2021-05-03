import threading
import time

def func():
    print('ran')
    time.sleep(2)
    print('almost done')

print(threading.activeCount())

x = threading.Thread(target=func, args=())
x.start()

print(threading.activeCount())

time.sleep(0.8)
print('Back to main thread')

time.sleep(3)
print('Finally done')