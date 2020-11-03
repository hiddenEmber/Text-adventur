import Item

class Mob:
    def __init__(self, Name, level,ac):
        self.Name = Name
        self.Gold = 0
        self.XP = 0
        self.Level = level
        self.HpMax = ((self.Level-1)*8)+10
        self.Hp = self.HpMax
        self.Ivitory = []
        if ac!=None:
            self.baseAc=ac
        else:
            self.baseAc=0

    def LevelUp(mobClass):
        if mobClass.XP >= mobClass.Level * 8 :                        
            mobClass.XP = -(mobClass.Level - 1) * 8
            mobClass.Level+=1
            print("You are now Level " + str(mobClass.Level))
