from Entity import entity
import random
import Tools

class enemy(entity):
    def __init__(self, health, strength, money):
        super(enemy, self).__init__(health, strength, money)

    def makeMove(self):
        super(enemy, self).attack()

    def playLoseScreen(self, opponent):
        opponent.addMoney(self.getMoney())
        if not self.getMoney() == 0:
            print "Your opponent has dropped", self.getMoney(),"dollars! You now have $", opponent.getMoney()
        if random.randint(1,2) == 2:
            healthIncrease = random.randint(self.getStrength()/5, self.getStrength()/5*2)
            opponent.increaseMaxHealth(healthIncrease)
            print "Your max health has increased by", healthIncrease,"to", opponent.getMaxHealth(), "!"
            Tools.delay()

        if random.randint(1,2) == 2:
            strengthIncrease = 3 + random.randint(self.getStartingHealth()/20, self.getStartingHealth()/10)
            opponent.increaseStrength(strengthIncrease)
            print "Your strength has increased by", strengthIncrease,"to", opponent.getStrength(),"!"
            Tools.delay()

        print "You have killed your opponent! Time to head back home."
        Tools.delay()
