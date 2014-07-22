import time
import threading
class Chopstick:
    def __init__(self):
        self.myLock = threading.RLock()

    def pickUp(self):
        return self.myLock.acquire()

    def putDown(self):
        self.myLock.release()

    def canBePickedUp(self):
        self.myLock._is_owned()
class Philosopher(threading.Thread):
    def __init__(self, leftChop, rightChop, bites=0):
        self.left = leftChop
        self.right = rightChop
        self.bites = bites

    def eat(self):
        if self.pickUp():
            self.chew()
            self.putDown()

    def chew(self):
        pass

    def pickUp(self):
        if not self.left.pickUp(): return False
        if not self.right.pickUp():
            self.left.putDown()
            return False
        return True

    def putDown(self):
        self.left.putDown()
        self.right.putDown()

    def run(self):
        for i in range(self.bites):
            self.eat()
