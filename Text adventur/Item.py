class Item ():
    def __init__(self,ac,type,damage):
        self.ac=ac
        self.type=type
        self.damage=damage

    @staticmethod
    def createItem(self, isArmor):
        if isArmor:        
            item=Item(1,"boots",0)
        else:
            item=Item(0,"sword",1)
        print("a "+str(item.ac)+" ac "+str(item.damage)+" damage "+str(item.type)+" was created")

    def displayStats(self):
        print(str(self.type)+"\n"+"AC= "+str(self.ac)+"\n"+"damage= "+str(self.damage))