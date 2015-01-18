# encoding=utf-8


class Singleton(object):
    def __new__(cls, *args, **kw):  #override new
        if not hasattr(cls, '_instance'):  cls._instance = object.__new__(cls, *args, **kw)  #call the original __new__ method
        return cls._instance


White = -1
Black = 1


Left = -2
Right = -2
Up = 1
Down = -1


Board_row = 10
Board_col = 10
class Player:
    def __init__(self, color):
        self.color = color
        
    def playPiece(self, row, col):
        return Game.board.placeColor(row, col, self.color)
        
class Piece:
    def __init__(self, color):
        self.color = color
        
    def flip(self):
        self.color = 0-self.color

        
class Game(Singleton):
    def __init__(self, player1, player2):
        self.board = Board(Board_row, Board_col)
        self.player1 = player1
        self.player2 = player2

'''
initial board has a grid like the following in the center:
		 *     WB
		 *     BW
'''
class Board:
    def __init__(self, rows, cols):
        self.board = [[None for i in range(cols)] for j in range(rows)]
        middleRow = len(self.board)/2
        middleCol = len(self.board[0])/2
        self.board[middleRow][middleCol] = Piece(White)
        self.board[middleRow+1][middleCol] = Piece(Black)
        self.board[middleRow][middleCol+1] = Piece(Black)
        self.board[middleRow+1][middleCol+1] = Piece(White)
        self.blackCount = 2
        self.whiteCount = 2
        
    def placeColor(self, row, col, color):
        if self.board[row][col]: return False
        self.board[row][col] = Piece(color)
    
    
 #flips pieces starting at (row, column) and proceeding in * direction d

    def flipSection(self, i, j, color, d):
        r = 0
        c = 0
        if d == Up: r = -1
        elif d == Down: r = 1
        elif d == Left: c = -1
        elif d == Right: c =1
        else: return -1
        #DFS
        if i <0 or i > len(self.board) or j<0 or j>len(self.board[0]):
            return -1
        #Found same color - return nothing flipped
        if self.board[i][j].color == color: return 0
        
        flipped = self.flipSection( i+r, j+c, color, d)
        
        if flipped < 0: return -1
        
        self.board[i][j].flip()
        return flipped+1
        
    def getScoreForColor(self, color):
        if color == White: return self.whiteCount
        elif color == Black: return self.blackCount
    
    def updateScore(self, newColor, newPieces):  # newpiece = fliped + 1
        if newColor == Black:
            self.whiteCount -= newPieces-1
            self.blackCount += newPieces
        elif newColor == White:
            self.blackCount -= newPieces-1
            self.whiteCount += newPieces
    
    def printBoard(self):
        for pieces in self.board:
            for p in pieces:
                if p == None: print '_'
                elif p.color == White: print 'W'
                else: print 'B'
            print '\n'