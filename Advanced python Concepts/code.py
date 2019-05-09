class Enemy:
    def __init__(self,atkl,atkh):
        self.atkl=atkl
        self.atkh=atkh
    
    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy(50,40)
enemy1.getAtk() # 50

enemy2 = Enemy(70,90)
enemy2.getAtk() # 70

print("███████████")
