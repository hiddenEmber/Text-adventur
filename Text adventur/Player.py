from Mob import Mob

class Player(Mob):
    def __init__(self, Name, level,ac):
        super().__init__(Name, level,ac)