from enum import Enum

class Item ():
    def __init__(self,type,ac,damage):
        self.ac=ac
        self.type=type
        self.damage=damage

    @staticmethod
    def createItem(self, isArmor):
        if isArmor:
            item=Item("boots",1,0)
        else:
            item=Item("sword",0,1)
        print("a "+str(item.ac)+" ac "+str(item.damage)+" damage "+str(item.type)+" was created")

    def displayStats(self):
        print(str(self.type)+"\n"+"AC= "+str(self.ac)+"\n"+"damage= "+str(self.damage))

class ItemType(Enum):
    HELMET = 1
    BREAST_PLATE = 2
    PANTS = 3
    BOOTS = 4
    GAUNTLETS = 5
