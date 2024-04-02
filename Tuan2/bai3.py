import random as r 

class Dice:
    def __init__(self,num=1):
        self.num = num
    def roll(self):
        self.num = r.randint(1,6)

