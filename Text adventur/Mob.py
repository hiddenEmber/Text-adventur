import Item

class Mob:
    def __init__(self, name, level, ac):
        self.name = name
        self.gold = 0
        self.xp = 0
        self.level = level
        self.hpMax = ((self.level-1)*8)+10
        self.hp = self.hpMax
        self.inventory = []
        if ac!=None:
            self.baseAc=ac
        else:
            self.baseAc=0

    def LevelUp(self, mobClass):
        if mobClass.xp >= mobClass.level * 8 :
            mobClass.xp = -(mobClass.level - 1) * 8
            mobClass.level+=1
            print("You are now Level " + str(mobClass.level))

    def printInventory (self):
        if len(self.inventory) > -1:
            inventoryView=True
            print("inventoryView is"+str(inventoryView))
            for x in range(len(self.inventory)):
                print(x+1, ",", ".")
                print(self.inventory[x].type)

    def addToInventory (self, item):
        self.inventory.append(item)

    @staticmethod
    def makeEqualMob(name):
        hostile=Mob(name,1,2)
        print("you found a level "+str(hostile.level)+" "+hostile.name+"!")