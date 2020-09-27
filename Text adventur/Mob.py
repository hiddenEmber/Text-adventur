# def fight(p1,p2):
#     if p1==p2 and p1==1:
#         print("you stand there looking at each other as you both brase for and attack")


# def playerCombatChoice():
#     p2CombatAction=ranNum(1,3)

#     playerCombatChoice=input("you can block, quick or Heavy")
#     if playerCombatChoice=="block":
#         p1CombatAction=1
#     elif playerCombatChoice=="quick":
#         p1CombatAction=2
#     elif playerCombatChoice=="heavy":
#         p1CombatAction=3
#     else:       
#         playerCombatChoice=4

    #print("You took a step")
    #Player.Gold+=(random.randint(1,10))
    #print("You have:" + str(Player.Gold) + "G")
    #Player.XP+=(random.randint(1,10))
    #print("you have:" + str(Player.XP) + "/" + str(Player.Level * 8))
    #Player.LevelUp()


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