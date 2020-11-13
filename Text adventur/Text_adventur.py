
#Import all Classes
from enum import Enum
from Mob import Mob
from Player import Player
from Item import Item
import random

#delcares some values
tempName = "PlaceHolder"
temp1 = 1
temp2 = 2
inCombat=False
print("check inv view")
inventoryView = False

def playerCombatChoice():
    return False

#takes a step and inconters a mob
def takeStep():
    if inCombat:
        playerCombatChoice()
    player.makeEqualMob(tempName)  

# This already does that just use random.randint
#def ranNumb(Min,Max):
#    return random.randint(Min,Max)

#Asks the play what they wants to do then sents them on the appropret path
def playerAction(inventoryView):
    action = input("What would you like to do?")
    if inventoryView:
        if action == "stats":
            itemCheck=input("what item do you want to see the stats of?")
            player.inventory[itemCheck].displayStats()
        elif action == "equip":
            equipedItem=input("what do you want to equip?")
            player.equipItemFromInventory(equipedItem)
    else:
        if action == "step":
            takeStep()
        elif action == "look":
            
            player.addToInventory(Item.createItem(True,player))
        elif action == "check Inv":
            inventoryView = True
            player.printInventory()


#makes the player and while the player has positive HP asks the player what they want to do
player = Player(tempName,temp1)
while player.hp > 1:
    playerAction(inventoryView)
