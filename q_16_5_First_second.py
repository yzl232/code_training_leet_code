import time
import  threading
class Foo(threading.Thread):
    def __init__(self):
        self.lock1 = threading.RLock()
        self.lock2 = threading.RLock()
        self.lock3 = threading.RLock()
        self.lock1.acquire()
        self.lock2.acquire()
        self.lock3.acquire()

    def first(self):
        #do something here
        self.lock1.release()

    def second(self):
        self.lock1.acquire()  # wait until finished with first
        self.lock1.release()
        #do something here
        self.lock2.release()  #  mark finished with second()

    def third(self):
        self.lock2.acquire()  # wait until finished with second
        self.lock2.release()
        #do something here
