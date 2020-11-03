
#Import all Classes
from enum import Enum
import Mob
import Item
import random

#delcares some values
tepName = "PlaceHolder"
tep1 = 1
tep2 = 2
inCombat=False
print("check inv view")
invitoryView

#Displays the stats of the item selected
def displayStats(itemNumber,forWho):
    looking=forWho.Ivitory[itemNumber]
    print(str(looking.type)+n/+"AC= "+str(looking.ac)+n/+"damage= "+str(looking.damage))
#prints the invintory of the selected mob
def printInvitory (forWho):
    if len(forWho.Ivitory) > -1:      
        invitoryView=True
        print("invitoryView is"+str(invitoryView))
        for x in range(len(forWho.Ivitory)):
            print(x+1,end=".")
            print(forWho.Ivitory[x].type)
        

#crates a item and puts it in the invitory of slected mob
def createItem(isArmor,forWho):
    if isArmor:        
        item=Item.Item(1,"boots",0)
    else:
        item=Item.Item(0,"sword",1)
    forWho.Ivitory.append(item)
    print("a "+str(item.ac)+" ac "+str(item.damage)+" damage "+str(item.type)+" was created")

#makes a mob 
def makeEquleMob():
    Hostile=Mob.Mob(tepName,1,2)
    print("you found a level "+str(Hostile.Level)+" "+Hostile.Name+"!")

#takes a step and inconters a mob
def takeStep():
    if inCombat:
        playerCombatChoice()
    makeEquleMob()  

#returnes a random number
def ranNumb(Min,Max):
    return random.ranint(Min,Max)

#Asks the play what they wants to do then sents them on the appropret path
def playerAction():
    action = input("What woukd you like to do?")
    print(str(invitoryView))
    if invitoryView:
        
        if action == "stats":
            itemCheck=imput("what item do you want to see the stats of?")
            displayStats(itemCheck,Player)
        elif action == "equip":
            equipedItem=imput("what do you want to equip?")
            equipItem(equipedItem,Player)
    else:
        if action == "step":         
            takeStep()
        elif action == "look":
            createItem(True,Player)
        elif action == "check Inv":
            printInvitory(Player)


#makes the player and while the player has positive HP asks the player what they want to do
Player = Mob.Mob(tepName,tep1,None)
while Player.Hp > 1:    
    playerAction()


