import Tools
from scanner import scan
import PotionShop
import ScrollShop

player = None

def init(p):
	global player
	player  = p
	Tools.clearScreen()
	print "You have entered the town. \nThere is a potion shop, and a scroll shop. Or would you rather go back home?"
	givePlayerOptions()


def givePlayerOptions():
	choice = scan(raw_input(">"))
	if 'potion' in choice['nouns']:
		visitPotionShop()
	elif 'scroll' in choice['nouns']:
		visitScrollShop()
	elif 'shop' in choice['nouns']:
		print "Which shop would you like to visit?"
		givePlayerOptions()
	elif 'home' in choice['nouns']:
		goHome()
	elif 'back' in choice['nouns']:
		goHome()
	else:
		print "Sorry, I couldn't understand your response. Please answer again."
		givePlayerOptions()

def visitPotionShop():
	PotionShop.init(getPlayer())
def visitScrollShop():
	ScrollShop.init(getPlayer())
def goHome():
	pass

def getPlayer():
	global player
	return player