
from enum import Enum

class ArmorType (Enum):
    Boots = 0
    Greves = 1
    Chest = 2
    Helm = 3

class Mob:
    def __init__(self, Name, level,ac):
        self.Name = Name
        self.Gold = 0
        self.XP = 0
        self.Level = level
        self.HpMax = ((self.Level-1)*8)+10
        self.Hp = self.HpMax
        if ac!=None:
            self.baseAc=ac
        else:
            self.baseAc=0

    def LevelUp(mobClass):
        if mobClass.XP >= mobClass.Level * 8 :                        
            mobClass.XP = -(mobClass.Level - 1) * 8
            mobClass.Level+=1
            print("You are now Level " + str(mobClass.Level))

class Armor ():
    def __init__(self,ac,type,bonus):
        self.ac=ac
        self.type=type
        self.bonus=bonus

tepName = "PlaceHolder"
tep1 = 1
tep2 = 2
Incombat=False
import random

def makeEquleMob():
    Hostile=Mob(tepName,1,2)
    print("you found a level "+str(Hostile.Level)+" "+Hostile.Name+"!")


def takeStep():
    if InCombat:
        playerCombatChoice()
    makeEquleMob()  

def ranNumb(Min,Max):
    return random.ranint(Min,Max)

def playerAction():
    action = input("What woukd you like to do?")
    if action == "step":         
        takeStep()


#Player.PlayerName=input("Hey adventuer!  What is thy name?")
#print("you entered: "+Player.PlayerName)

Player = Mob(tepName,tep1,None)
while Player.Hp > 1:    
    playerAction()


