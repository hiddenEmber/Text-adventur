def fight(p1,p2):
    if p1==p2 and p1==1:
        print("you stand there looking at each other as you both brase for and attack")


def playerCombatChoice():
    p2CombatAction=ranNum(1,3)

    playerCombatChoice=input("you can block, quick or Heavy")
    if playerCombatChoice=="block":
        p1CombatAction=1
    elif playerCombatChoice=="quick":
        p1CombatAction=2
    elif playerCombatChoice=="heavy":
        p1CombatAction=3
    else:       
        playerCombatChoice=4

    #print("You took a step")
    #Player.Gold+=(random.randint(1,10))
    #print("You have:" + str(Player.Gold) + "G")
    #Player.XP+=(random.randint(1,10))
    #print("you have:" + str(Player.XP) + "/" + str(Player.Level * 8))
    #Player.LevelUp()


