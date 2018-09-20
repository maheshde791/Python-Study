#! usr/bin/python

import time
from threading import Thread

def printer():
    for num in range(3):
        print("hello",num)
        time.sleep(1)


thread1 = Thread(target=printer)
thread1.start()
thread2 = Thread(target=printer)
thread2.start()
threads = []
threads.append(thread1)
threads.append(thread2)
for t in threads:
	t.join()
#thread.join()
print("goodbye\r\n")
