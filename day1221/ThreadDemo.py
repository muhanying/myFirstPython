import threading
import time
from threading import Thread

exitFlag = 0


class MyThread(Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadid = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程；" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程；" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
