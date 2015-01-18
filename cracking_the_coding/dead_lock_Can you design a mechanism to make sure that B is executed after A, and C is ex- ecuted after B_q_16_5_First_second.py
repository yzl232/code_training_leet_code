'''
dead_lock_Can you design a mechanism to make sure that B is executed after A, and C is ex- ecuted after B_q_16_5_First_second
'''
import  threading
class Foo(threading.Thread):
    def __init__(self):
        self.lock1 = threading.RLock()
        self.lock2 = threading.RLock()
        self.lock1.acquire()  #2个lock。 A占了一个。 B占了一个
        self.lock2.acquire()

    def first(self):#受到限制的部分要先acquire
        #do something here
        self.lock1.release()    #只有release以后，才能够下一步second

    def second(self):
        self.lock1.acquire()  # wait until finished with first
        #do something here
        self.lock1.release()
        self.lock2.release()  #  mark finished with second()

    def third(self):
        self.lock2.acquire()  # wait until finished with second
        #do something here
        self.lock2.release()