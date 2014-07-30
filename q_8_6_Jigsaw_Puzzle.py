Inner = -1
Outer = 1
Flat = 0

class Edge:
    def __init__(self, edgeType, index, pieceParent,attachedToEdge = None):
        self.edgeType = edgeType
        self.index = index
        self.pieceParent = pieceParent
        self.attachedToEdge = attachedToEdge
    
    def fitsWith(self,edge):
        pass
    
class Piece:
    def __init__(self, edges, isCorner=False):
        self.edges = edges
        self.isCorner = isCorner
        
class Puzzle:
    def __init__(self, pieces, inners, outers, flats, corners = [], solution= []):
        self.pieces = pieces
        self.inners = inners
        self.outers = outers
        self.flats = flats
        self.corners = corners   
        self.solution = solution
        
    def sort(self):
        for p in self.pieces:
            count = 0
            for e in p.edges:
                if e.edgeType == Inner:self.inners.append(e)
                elif e.edgeType == Outer:self.outers.append(e)
                elif e.edgeType == Flat: count+=1
            if count==2: self.corners.append(p)
        pass
    
    def solve(self):
        currentEdge = self.getExposedEdge(self.corners[0])
        while currentEdge:
            opposites = self.outers if currentEdge.edgeType == Inner else self.inners
            for e in opposites:
                if e.fitsWith(currentEdge):
                    self.attachEdges(e, currentEdge)
                    self.removeFromList(currentEdge)
                    self.removeFromList(e)
                    currentEdge = self.nextExposedEdge(e)
                    break
        pass
        
    def removeFromList(self, edge):
        if edge.edgeType == Flat: return
        array = self.inners if edge.edgeType == Inner else self.outers
        array.pop(edge)
        
        
    def isExposed(self, edge):
        return edge.edgeType != Flat and edge.attachedToEdge 
    
    def attachEdges(self, edge1, edge2):
        edge1.attachedToEdge = edge2
        edge2.attachedToEdge = edge1
    
    def getExposedEdge(self, piece):
        for e in piece.edges:
            if self.isExposed(e): return e
        return
    
    def nextExposedEdge(self, edge):
        next_index = (edge.index+2)%4
        next_edge = edge.pieceParent.edges[next_index]
        if self.idExposed(next_edge): return next_edge
        return self.getExposedEdge(edge.pieceParent)
        
    
