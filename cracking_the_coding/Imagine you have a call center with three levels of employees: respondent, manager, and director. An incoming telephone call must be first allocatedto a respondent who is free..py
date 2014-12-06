'''
Imagine you have a call center with three levels of employees: respondent, manager, and director. An incoming telephone call must be first allocatedto a respondent who is free.
'''

from collections import deque


class Singleton(object):
    def __new__(cls, *args, **kw):  #override new
        if not hasattr(cls, '_instance'):  cls._instance = object.__new__(cls, *args, **kw)  #call the original __new__ method
        return cls._instance

LEVELS = 3
num_respondents = 10
num_managers = 4
num_directors = 2
Responder_Rank = 0
Manager_Rank = 1
Director_Rank = 2

class CallHandler(Singleton):
    def __init__(self):
        Singleton.__init__()
        self.employees = []
        self.callQueues = []
        for i in range(LEVELS):
            self.callQueues.append(deque([]))

        self.respondents = []
        self.managers = []
        self.directors = []
        for i in range(num_respondents):
            self.respondents.append(Respondent())

        for i in range(num_managers):
            self.managers.append(Manager())

        for i in range(num_directors):
            self.directors.append(Director())

        self.employees.append(self.respondents)
        self.employees.append(self.managers)
        self.employees.append(self.directors)
        
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
                call.setHandler(emp)
                return True
        return False
            
        
    
        
class Call(object):
    def __init__(self, caller):
        self.rank = Responder_Rank
        self.caller = caller
        self.handler = None
    
    def setHandler(self, employee):
        self.handler = employee
        
    def reply(self, message):
        print message
    
    def incrementRank(self):
        if self.rank == Responder_Rank:
            self.rank = Manager_Rank
        elif self.rank == Manager_Rank:
            self.rank = Director_Rank
        return self.rank
        
    def disconnect(self):
        print 'thank you for your calling'
        

class Caller(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        

class Employee(object):
    def __init__(self):
        self.currentCall = None
        self.rank = None

    def receiveCall(self, call):
        self.currentCall = call

    def isFree(self):
        return self.currentCall == None

    def assignNewCall(self):
        if not self.isFree():
            return False
        return CallHandler.assignCall(self)

    def callCompleted(self):
        if self.currentCall != None:
            self.currentCall.disconnec()
            self.currentCall = None
        self.assignNewCall()
    pass

class Respondent(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.rank = Responder_Rank

class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.rank = Manager_Rank
        
class Director(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.rank = Director_Rank