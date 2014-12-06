class User:
    def __init__(self, id, details, accountType):
        self.userId = id
        self.details = details
        self.accountType = accountType
        
class Book:
    def __init__(self, id, details):
        self.bookId = id
        self.details = details
        
    def update(self):
        pass
        
class Library:
    def __init__(self, books = {}):
        self.books = books
        
    def addBook(self, id, details):
        if id in self.books: return
        self.books[id] = Book(id, details)
        return self.books[id]
    
    def removeUsingID(self, id):
        if id not in self.books: return False
        self.books.pop(id)
        return True
        
    def removeUsingBook(self, book):
        return self.removeUsingID(book.bookId)
        
    def findBook(self, id):
        if id in self.books:
            return self.books[id]
            
class UserManager:
    def __init__(self, users = {}):
        self.users = users
        
    def addUser(self, id, details, accountType):
        if id in self.users: return
        user = User(id, details, accountType)
        self.users[id] = user
        return user

    
    def removeUserUsingID(self, id):
        if id not in self.users: return False
        self.users.pop(id)
        return True
        
    def removeUser(self, user):
        return self.removeUserUsingID()
        
    def find(self, id):
        if id in self.users:
            return self.users[id]
        
class Display:
    def __init__(self, activeUser = None, pageNumber = 0, activeBook = None):
        self.activeUser = activeUser
        self.pageNumber = pageNumber
        self.activeBook = NactiveBookone
        
    def displayUser(self, user):
        self.activeUser = user
        self.refreshUsername()
        
    def displayBook(self, book):
        self.activeBook = book
        self.pageNumber = 0
        self.refreshTitle()
        self.refreshDetails()
        self.refreshPage()
     
    def refreshUsername(self):
        pass
    
    def refreshPage(self):
        pass
    
    def refreshTitle(self):
        pass

    def refreshDetails(self):
        pass
        
    def turnPageForward(self):
        self.pageNumber+=1
        self.refreshPage()
        
    def turnPageBackward(self):
        self.pageNumber-=1
        self.refreshPage()    
        
        

class OnlineReaderSystem:
    def __init__(self, library, userManager, display, activeBook = None, activeUser = None):
        self.library = library
        self.userManager = userManager
        self.display = display
        self.activeBook = activeBook
        self.activeUser = activeUser