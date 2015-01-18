'''
Explain how you would design a chat server. In particular, provide details about
the various backend components, classes, and methods. What would be the
hardest problems to solve?
'''

import time

class Singleton(object):
    def __new__(cls, *args, **kw):  #override new
        if not hasattr(cls, '_instance'):  cls._instance = object.__new__(cls, *args, **kw)  #call the original __new__ method
        return cls._instance
        
ISOTIMEFORMAT='%Y-%m-%d %X'

Rejected = -2
Accepted = 2
Read = 1
Unread = -1


Offline = -2
Away = -1
Idle = 0
Available = 1
Busy = 2

IDGenerater =1000



class User:
    def __init__(self, id, accountName, fullName):
        self.id = id
        self.accountName = accountName
        self.fullName = fullName
        self.privateChats = {}
        self.status = None
        self.groupChats = {}
        self.receivedAddRequests = []
        self.sentAddRequests = []
        self.contacts = {}
        
    def sendMessageToUser(self, toUser, content):
        global IDGenerater
        if toUser.id not in self.privateChats: 
            IDGenerater+=1
            private_chat = PrivateChat(IDGenerater, self, toUser)
            self.privateChats[toUser.id] = private_chat
        private_chat = self.privateChats[toUser.id]
        message = Message(content)
        private_chat.messages.append(message)
        
    def sendMessageToGroupChat(self, groupId, content):
        if groupId not in self.groupChats:
            group_chat = GroupChat(groupId)
        group_chat = self.groupChats[groupId]
        message = Message(content)
        group_chat.messages.append(message)
            
    def addContact(self, user):
        if user.id in self.contacts:
            return False
        self.contacts[user.id] = user
        return True
        
    def receivedAddRequest(self, request):
        senderID = request.fromUser.id
        if senderID not in self.receivedAddRequests: self.receivedAddRequests[senderID] = request
        
    def sentAddRequest(self, request):
        receivedId = request.toUser.id
        if receivedId not in self.sentAddRequests: self.sentAddRequest[receivedId] = request
        
    def removeAddRequest(self, request):
        if request.toUser == self:  self.receivedAddRequests.pop(request)
        elif request.fromUser == self: self.sentAddRequests.pop(request)
    
    def requestAddUser(self, accountName):
        UserManager.addUser(self,accountName)
        
    def addGroupConversation(self, conversation):
        self.groupChats.append(conversation)
    
    def addPrivateConversation(self, conversation):
        otherUser = PrivateChat.getOtherParticipant(self)
        self.privateChats[otherUser.id] = conversation
            
class Conversation:
    def __init__(self, id):
        self.participants = []
        self.id = id
        self.messages = []
    
class GroupChat(Conversation):
    def removeParticipant(self, user):
        self.participants.remove(user)
        
    def addParticipant(self, user):
        self.participants.append(user)
        
class PrivateChat(Conversation):
    def __init__(self, id, user1, user2):
        Conversation.__init__(self, id)
        self.participants.append(user1)
        self.participants.append(user2)
    
    def getOtherParticipant(self, oneUser):
        if self.participants[0] == oneUser: return self.participants[1]
        elif self.participants[1] == oneUser: return self.participants[0]
        return 
    
class UserStatus:
    def __init__(self, statusType, message):
        self.statusType = statusType
        self.message = message
        
class Message:
    def __init__(self, content, date = time.strftime(ISOTIMEFORMAT)):
        self.content = content
        self.date = date
        
class AddRequest:
    def __init__(self, fromUser, toUser, date = time.strftime(ISOTIMEFORMAT)):
        self.fromUser = fromUser
        self.toUser = toUser
        self.date = date
        self.status = Unread
        
class System:
    pass
    
class UserManager(Singleton):
    def __init__(self, usersById={}, usersByAccountName={}, onlineUsers={}):
        Singleton.__init__(self)
        self.usersByAccountName = usersByAccountName
        self.onlineUsers = onlineUsers
        self.usersById = usersById
        
    def addUser(self, fromUser, toAccountName):
        toUser = self.usersByAccountName[toAccountName]
        req = AddRequest(fromUser, toUser)
        toUser.receivedAddRequest(req)
        fromUser.sentAddRequest(req)
        
    def approveAddRequest(self, req):
        req.status = Accepted
        fromUser = req.fromUser
        toUser = req.toUser
        fromUser.addContact(toUser)
        toUser.addContact(fromUser)
    
    def rejectAddRequest(self, req):
        req.status = Rejected
        fromUser = req.fromUser
        toUser = req.toUser
        fromUser.removeAddRequest(req)
        toUser.removeAddRequest(req)
        
    def userSignedOn(self, accountName):
        if accountName not in self.usersByAccountName: return
        user = self.usersByAccountName[accountName]
        user.status = Available
        self.onlineUsers[user.id] = user
    
    def userSignedOff(self, accountName):
        user = self.usersByAccountName[accountName]
        if user:
            user.status = Offline
            self.onlineUsers.pop(user.id)