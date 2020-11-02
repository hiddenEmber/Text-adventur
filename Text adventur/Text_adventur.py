
from enum import Enum
import Mob
import Item
import itemType

tepName = "PlaceHolder"
tep1 = 1
tep2 = 2
inCombat=False
import random

def createItem(isArmor,forWho):
    if isArmor:        
        item=Item.Item(1,"boots",0)
        forWho
    else
        item=Item.Item(0,"sword",1)

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
    elif action == "look":
        createItem(true,Player)

#Player.PlayerName=input("Hey adventuer!  What is thy name?")
#print("you entered: "+Player.PlayerName)

Player = Mob.Mob(tepName,tep1,None)
while Player.Hp > 1:    
    playerAction()


