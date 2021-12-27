import random
t=[]
class Pin:

    def __init__(self):

        print("A simple pin randomizer")
        self.startrange=int(input("\nEnter the starting range  "))
        self.endrange=int(input("\nEnter the ending value    "))
        self.combirange=int(input("\nHow many combination do you want   "))
        if int(self.combirange)>int(self.endrange-self.startrange):
            print("\nThe no of combination is more than possible sample outcomes","The possible outcome are ",int(self.combirange-self.endrange))
            exit(100)

        for a in range(1, self.combirange+1 ,1 ):
                self.a1=random.randrange(self.endrange,self.combirange,1)
                print(   "","","",self.a1)



b=Pin()
