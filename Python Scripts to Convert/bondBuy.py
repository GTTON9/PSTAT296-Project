class bondBuy:

    def __init__(self, units, bondObj,date):
        self.units = units
        self.bondObj = bondObj
        self.name = 'buy'
        self.date = date
        
    def getUnitsBought(self):
        return self.units
    
    def setUnitsBought(self,newUnits):
        self.units = newUnits

    def getBondObj(self):
        return self.bondObj
    
    def setBondObj(self,newObj):
        self.bondObj = newObj
    
    def getBondDate(self):
        return self.date
    
    def setBondDate(self,newDate):
        self.date = newDate

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    