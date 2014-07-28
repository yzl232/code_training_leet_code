from collections import deque

class Singleton(object):
    def __new__(cls, *args, **kw):  #override new
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)  #cls : class
            cls._instance = orig.__new__(cls, *args, **kw)  #call the original __new__ method
        return cls._instance

LEVELS = 3
num_respondents = 10
num_managers = 4
num_directors = 2
Responder_NO = 0
Manager_NO = 1
Director_NO = 2

class CallHandler(Singleton):
    def __init__(self):
        Singleton.__init(self)
        self.employeeLevels = []
        self.callQueues = []
        for i in range(levels):
            self.callQueues.add(deque([]))
        
        self.respondents = []
        for k in range(num_respondents-1):
            self.respondents.add(Respondent())
        self.employeeLevels.add(self.respondents)
        
        self.managers = []
        self.managers.add(Manager())
        self.employeeLevels.add(self.managers)
        
        self.directors = []
        self.directors.add(Director())
        self.employeeLevels.add(self.directors)
        
    def getHandlerForCall(self, call):
        for level in range(call.rank, LEVELS):
            emps = self.employeeLevels[level]
            for emp in emps:
                if emp.isFree():
                    return emp
        return None
        
    def dispatchCallForCaller(self, caller):
        call = Call(caller)
        self.dispatchCall(call)
        
    def dispatchCall(self, call):  
        #Try to route the call to an employee with minimal rank. 
        emp = self.getHandlerForCall(call)
        if emp:
            emp.receiveCall(call)
            call.setHandler(emp)
        else:
            call.reply('Please wait for free employee to reply')
            self.callQueues[call.rank].append(call)
            
        
        #An employee got free. Look for a waiting call that he/she can serve. Return true
     #if we were able to assign a call, false otherwise.
         
    def assignCall(self, emp):
        for rank in range(emp.rank, -1, -1):
            q = self.callQueues[rank]
            call = q.popleft()
            if call:
                emp.receiveCall(call)
                return True
        return False
            
        
    
        
class Call(object):
    def __init__(self, caller):
        self.rank = Responder_NO
        self.caller = caller
        self.handler = None
    
    def setHandler(self, employee):
        self.handler = employee
        
    def reply(self, message):
        print message
    
    def incrementRank(self):
        if self.rank == Responder_NO:
            self.rank = Manager_NO
        elif self.rank == Manager_NO:
            self.rank = Director_NO
        return self.rank
        
    def disconnect(self):
        print 'thank you for your calling'
        
class Rank(object):
    def __init__(self, val):
        self.Responder = 0
        self.Manager = 1
        self.Director = 2
        self.value = val

class Caller(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
class Employee(object):
    def __init__(self):
        self.currentCall = None
        self.rank = None
    
    def receiveCall(self, call):
        self.currentCall =call
        
    def callCompleted(self):
        if self.currentCall != None:
            self.currentCall.disconnect()
            self.currentCall = None
        self.assignNewCall()
    
    def assignNewCall(self):
        if not self.isFree():
            return False
        return CallHandler.assignCall(self)
    
    def isFree(self):
        return self.currentCall == None
    

class Respondent(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.rank = Responder_NO

class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.rank = Manager_NO
        
class Director(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.rank = Director_NO