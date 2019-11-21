# single_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken for single threaded in seconds -', end - start)

t1 = Thread(target=countdown, args=(COUNT//3,))
t2 = Thread(target=countdown, args=(COUNT//3,))
t3 = Thread(target=countdown, args=(COUNT//3,))

start = time.time()
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
end = time.time()



print('Time taken for multi threaded in seconds -', end - start)
print("This is because GIL (Global Interpreter Lock) which allows only one thread to run at a time")