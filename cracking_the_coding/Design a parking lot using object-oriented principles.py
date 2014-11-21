Motorcycle_size = 2
Compact_size = 5
Large_size = 10

class Vehicle:  # 
    def __init__(self, licensePlate, spotsNeeded, vehicleSize):
        self.licensePlate = licensePlate
        self.vehicleSize = vehicleSize
        self.spotsNeeded = spotsNeeded
        self.parkingSpots = []   # how many spots will the vehicle take?
        
    def parkInSpot(self, spot):
        self.parkingSpots.append(spot)
        
    def clearSpots(self):
        for spot in self.parkingSpots:
            spot.removeVehicle()
        self.parkingSpots = []
        
    def canFitInSpot(self, spot):
        pass
        
    def printInfo(self):
        pass
        
class Motorcycle(Vehicle):
    def __init__(self, licensePlate):
        Vehicle.__init__(self, licensePlate, 1, Motorcycle_size)
    
    def canFitInSpot(self, spot):
        return True
        
    def printInfo(self):
        print 'M'
        
class Car(Vehicle):
    def __init__(self, licensePlate):
        Vehicle.__init__(self, licensePlate, 1, Compact_size)
    
    def canFitInSpot(self, spot):
        return spot.size == Large_size or spot.size == Compact_size
        
    def printInfo(self):
        print 'C'
        
class Bus(Vehicle):
    def __init__(self, licensePlate):
        Vehicle.__init__(self, licensePlate, 5, Large_size)
    
    def canFitInSpot(self, spot):
        return spot.size == Large_size 
        
    def printInfo(self):
        print 'B'
        
class ParkingSpot:
    def __init__(self, level, row, number, spotSize):
        self.level = level
        self.row = row
        self.spotNumber = number
        self.spotSize = spotSize
        self.vehicle = None
    
    def isAvailable(self):
        return self.vehicle == None
        
    def canFitVehicle(self, vehicle):
        return self.isAvailable() and vehicle.canFitInSpot(self)
        
    def removeVehicle(self):
        self.level.spotFreed()
        self.vehicle = None
        
    def park(self, vehicle):
        if not self.canFitVehicle():
            return False
        vehicle.parkInSpot(self)
        self.vehicle = vehicle
        return True
        
    def printInfo(self):
        if not self.vehicle:
            if self.spotSize == Motorcycle_size: print 'm'
            elif self.spotSize == Compact_size: print 'c'
            elif self.spotSize == Large_size: print 'l'
        else: self.vehicle.printInfo()
    
       
                
class Level:
    def __init__(self, floor, numberSpots):
        self.floor = floor
        self.spots = []
        self.availableSpots = numberSpots
        self.SPOTS_PER_ROW = 10
        largeSpots = numberSpots/4
        bikeSpots = numberSpots/4
        compactSpots = numberSpots - largeSpots - bikeSpots
        for i in range(numberSpots):
            size = Motorcycle_size
            if i < largeSpots:
                size = Large_size
            elif i< largeSpots + compactSpots:
                size = Compact_size
            row = i / self.SPOTS_PER_ROW
            self.spots.append(ParkingSpot(self, row, i, size))
            
    def findAvailableSpots(self, vehicle):
        spotsNeeded = vehicle.spotsNeeded
        lastRow = -1
        spotsFound = 0
        for i in range(len(self.spots)):
            spot = self.spots[i]
            if lastRow != spot.row:  # we only consider spots in the same row. 
                spotsFound = 0
                lastRow = spot.row
            if spot.canFitVehicle(vehicle):
                spotsFound +=1
            else: spotsFound = 1
            if spotsFound == spotsNeeded:
                return i - spotsNeeded + 1
        return -1
    
    def parkVehicle(self, vehicle):
        if self.availableSpots < vehicle.spotsNeeded:
            return False
        spotNumber = self.findAvailableSpots(vehicle)
        if spotNumber < 0: return False
        return self.parkingStartingAtSpot(spotNumber, vehicle)
    
    def parkingStartingAtSpot(self, spotNumber, vehicle):
        vehicle.clearSpots()
        success = True
        for i in range(vehicle.spotsNeeded):
            success = success and self.spots[spotNumber + i].park(vehicle)
        self.availableSpots -= vehicle.spotsNeeded
        return success
        
    def spotFreed(self):
        self.availableSpots +=1
    
    def printInfo(self):
        lastRow = -1
        for spot in self.spots:
            if spot.row != lastRow:
                print '\n'
                lastRow = spot.row
            spot.printInfo() 
   
class ParkingLot:
    def __init__(self, num_levels=5):
        self.levels = []
        self.num_levels = 5
        for i in range(self.num_levels):
            self.levels.append(Level(i, 30))
    
    def parkVehicle(self, vehicle):
        for level in self.levels:
            if level.parkVehicle(vehicle):
                return True
        return False
        
    def printInfo(self):
        for i in range(len(self.levels)):
            print 'Level: %d :' %i
            self.levels[i].printInfo()
            print '\n'
        print '\n'
             