
from enum import Enum
import Mob

class ArmorType (Enum):
    Boots = 0
    Greves = 1
    Chest = 2
    Helm = 3



class Armor ():
    def __init__(self,ac,type,bonus):
        self.ac=ac
        self.type=type
        self.bonus=bonus

tepName = "PlaceHolder"
tep1 = 1
tep2 = 2
inCombat=False
import random

def makeEquleMob():
    Hostile=Mob.Mob(tepName,1,2)
    print("you found a level "+str(Hostile.Level)+" "+Hostile.Name+"!")


def takeStep():
    if inCombat:
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

Player = Mob.Mob(tepName,tep1,None)
while Player.Hp > 1:    
    playerAction()


