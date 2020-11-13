from Item import Item
from Item import ItemType

class Mob:
    def __init__(self, name, level):
        self.name = name
        self.gold = 0
        self.xp = 0
        self.level = level
        self.hpMax = ((self.level-1)*8)+10
        self.hp = self.hpMax
        self.inventory = []
        self.equipped = {}

    def addXpFromMobDefeat(self, mobClass):
        xpToAdd = mobClass.level
        self.xp += xpToAdd
        while self.level * 8 <= self.xp:
            self.xp -= (self.level * 8)
            self.level+=1
            print("You are now Level " + str(self.level))

    def calculateBaseAC(self):
        return self.level

    def printInventory (self):
        for x in range(len(self.inventory)):
            print(x+1, ",", ".")
            print(self.inventory[x].type)

    def addToInventory (self, item):
        self.inventory.append(item)

    def equipItemFromInventory(self, itemId):
        #if there is already a item in the slot put it into our inventory
        if self.equipped[self.inventory[itemId].type] != None:
            self.inventory.append(self.equipped[self.inventory[itemId].type])
        #add the equipment to the now empty slot
        self.equipped[self.inventory[itemId].type] = self.inventory[itemId]

    @staticmethod
    def makeEqualMob(self, name):
        hostile=Mob(name, self.level-1)
        print("you found a level "+str(hostile.level)+" "+hostile.name+"!")