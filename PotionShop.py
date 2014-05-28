import Tools
from scanner import scan
from Potion import potion
import random

def init(player):
	Tools.clearScreen()
	print "You have",player.getMoney(),"dollars."
	Tools.createPotionShop()
	

	healthPotion = getHealthPotion(player)
	strengthPotion = getStrengthPotion(player)
	potions = [healthPotion, strengthPotion]

	for pot in potions:
		pot.describe()

	choice = scan(raw_input(">"))
	if 'health' in choice['nouns']:
		numAfford = player.getMoney() / healthPotion.getCost()
		player.buy(healthPotion, Tools.getAmount("How many would you like to buy?", "Sorry, you can only afford",numAfford))
		Tools.delay()
	elif 'strength' in choice['nouns']:
		numAfford = player.getMoney() / strengthPotion.getCost()
		player.buy(strengthPotion, Tools.getAmount("How many would you like to buy?", "Sorry, you can only afford", numAfford))
		Tools.delay()
	elif 'leave' in choice['verbs'] or 'back' in choice['nouns'] or 'home' in choice['nouns']:
		pass
	else:
		print "I didn't understand"
		Tools.delay()
		init(player)

def getHealthPotion(player):
	regenerate = random.randint(player.getMaxHealth()/20, player.getMaxHealth()/10)
	cost = 10 + regenerate
	return potion("health potion", 0, regenerate, cost)

def getStrengthPotion(player):
	increase = random.randint(player.getStrength()/10, player.getStrength()/5)
	cost = 15 + increase / 2
	return potion("strength potion", increase, 0, cost)