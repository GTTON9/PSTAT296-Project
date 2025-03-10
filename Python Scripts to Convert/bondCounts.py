import pandas as pd
# from bondSell import bondSell
# from bondBuy import bondBuy
# from bondStrip import bondStrip

class bondCounts:
    def __init__(self):
        self.bondDF = pd.DataFrame(columns = ['Date','bondType','amountMaintained','numberStripped'])
    
    def bondAction(self,doBondAction):

        bondActionKey = {'buy':1,'sell':-1,'strip':0}
        
        newRow = [doBondAction.getDate(),doBondAction.getBondOjb(),doBondAction.getUnitsBought()]
        currBondType = newRow[1]
  
        self.bondDF = pd.concat([self.bondDF,pd.DataFrame([{'Date': newRow[0], 'bondType': currBondType, 
                                                "amountMaintained": newRow[2] * bondActionKey[doBondAction.getName()], 
        "numberStripped":(newRow[2] if doBondAction.getName() == 'strip' else 0)}])])

    
    def getBondDF(self):
        return self.bondDF
    
    def setBondDF(self,newBondDF):
        self.bondDF = newBondDF