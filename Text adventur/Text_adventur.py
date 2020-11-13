
#Import all Classes
from enum import Enum
import Mob
import Item
import random

#delcares some values
tempName = "PlaceHolder"
temp1 = 1
temp2 = 2
inCombat=False
print("check inv view")
inventoryView = False

#Displays the stats of the item selected
def displayStats(itemNumber,forWho):
    looking=forWho.Inventory[itemNumber]
    print(str(looking.type)+"\n"+"AC= "+str(looking.ac)+"\n"+"damage= "+str(looking.damage))
#prints the invintory of the selected mob
def printinventory (forWho):
    if len(forWho.Inventory) > -1:      
        inventoryView=True
        print("inventoryView is"+str(inventoryView))
        for x in range(len(forWho.Inventory)):
            print(x+1, ",", ".")
            print(forWho.Inventory[x].type)
        

#crates a item and puts it in the inventory of slected mob
def createItem(isArmor,forWho):
    if isArmor:        
        item=Item.Item(1,"boots",0)
    else:
        item=Item.Item(0,"sword",1)
    forWho.Inventory.append(item)
    print("a "+str(item.ac)+" ac "+str(item.damage)+" damage "+str(item.type)+" was created")

def equipItem(equipedItem,Player):
    return False


def playerCombatChoice():
    return False

#makes a mob 
def makeEquleMob():
    Hostile=Mob.Mob(tempName,1,2)
    print("you found a level "+str(Hostile.Level)+" "+Hostile.Name+"!")

#takes a step and inconters a mob
def takeStep():
    if inCombat:
        playerCombatChoice()
    makeEquleMob()  

#returnes a random number
def ranNumb(Min,Max):
    return random.randint(Min,Max)

#Asks the play what they wants to do then sents them on the appropret path
def playerAction():
    action = input("What would you like to do?")
    if inventoryView:
        if action == "stats":
            itemCheck=input("what item do you want to see the stats of?")
            displayStats(itemCheck,Player)
        elif action == "equip":
            equipedItem=input("what do you want to equip?")
            equipItem(equipedItem,Player)
    else:
        if action == "step":
            takeStep()
        elif action == "look":
            createItem(True,Player)
        elif action == "check Inv":
            printinventory(Player)


#makes the player and while the player has positive HP asks the player what they want to do
Player = Mob.Mob(tempName,temp1,None)
while Player.Hp > 1:
    playerAction()
