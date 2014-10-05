class Server:
    def __init__(self, machines = []):
        self.machines = machines


class Machines:
    def __init__(self, persons = [], machineID):
        self.persons = persons
        self.machineID = machineID

class Person:
    def __init__(self, personID, machineID, info = '', friends=[]):
        self.friends = friends
        self.personID = personID
        self.machineID = machineID
        self.server = Server()
        self.info = info
    
    def setInfo(self, info):
        self.info = info
    
    def getFriends(self):
        return friends
        
    def getID(self):
        return self.personID
        
    def getMachineID(self):
        return self.getMachineID
    
    def addFriend(self, personId):
        self.friends.append[personId]
        
    def lookUpFriend(self, machineID, personID):
        for m in self.server.machines:
            for p in m.persons:
                if p.personID == personID:
                    return p
        return None
    
    def lookUpMachine(self, machineID):
        for m in self.server.machines:
            if m.machineID == machineID:
                return m
        return None
        
    
    
        
