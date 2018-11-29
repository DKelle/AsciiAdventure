from Entity import entity
from scanner import scan
import Tools

class player(entity):
    def __init__(self, health, strength, money):
        super(player, self).__init__( health, strength, money)
        self.name = raw_input("What is your name, traveller?\n>")
        self.itemList = {"health potion" : 0, "strength potion" : 0}
        self.money = 100

    def addMoney(self, money):
        self.money += money

    def spendMoney(self, cost):
        self.money = max(self.money - cost, 0)

    def getBag(self):
        return self.bag

    def getItemList(self):
        return self.itemList

    def lookInBag(self):
        Tools.drawBag(self.getItemList())

        if len(self.getBag()) > 0:
            self.determineWhichItemToUse()
        else:
            print "You have nothing in your bag."
            Tools.delay()

    def determineWhichItemToUse(self):
        usedItem = False

        choice = scan(raw_input("Which item would you like to use?\n>"))
        if 'none' in choice['nouns'] or 'back' in choice['nouns']:
            usedItem = True
        else:

            for item in self.getBag():
                if usedItem:
                    break
                keywords = item.getName().split(" ")
                for word in range(0,len(keywords)-1):
                    if keywords[word] in choice['nouns']:
                        usedItem = True
                        amount = Tools.getAmount("How many would you like to use?","Sorry, you only have", self.getItemList()[item.getName()])
                        self.usePotions(self.getListOfPotions(item.getName(), amount))
                        self.getItemList()[item.getName()] -= amount
                        break
                if(not usedItem):
                    print "I didn't understand your answer."
                    Tools.delay()
                    self.lookInBag()


    def addToBag(self, item, amount):
        for i in range(0,amount):
            self.getBag().append(item)
        self.getItemList()[item.getName().lower()] += amount
        print "You have put",amount,"",item.getName(), "in your bag."

    def buy(self, item, amount):
        if item.getCost() > self.getMoney():
            print "Sorry, you can't afford this item"
        else:
            self.spendMoney(item.getCost() * amount)
            print "You have purchased",amount, "",item.getName()
            self.addToBag(item, amount)

    def getListOfPotions(self,potionName, amount):
        if amount == 0:
            return
        potionList = []
        for item in self.getBag():
            if item.getName() == potionName:
                potionList.append(item)
                if len(potionList) == amount:
                    return potionList
        return potionList

    def usePotions(self, potionList):
        startingHealth = self.getHealth()
        startingStrength = self.getStrength()
        for item in potionList:
            self.getBag().remove(item)
            self.increaseMaxHealth(item.getHealth())
            self.replenish(item.getHealth())
            self.increaseStrength(item.getAttack())

        if not startingStrength == self.getStrength():
            print "Your strength has increased from", startingStrength, "to", self.getStrength()
        if not startingHealth == self.getHealth():
            print "Your current health has increased from", startingHealth, "to", self.getHealth(), "and your max health is now", self.getMaxHealth()

        Tools.delay()

    def playLoseScreen(self, opponent):
        print "You are dead. Time to head back home."
        Tools.delay()
