from Player import player
from Grunt import grunt
from Digger import digger
from Butler import butler
from Soldier import soldier
from BodyBuilder import bodyBuilder
from Hoard import hoard
from scanner import scan
import Battle
import Town
import random
import Tools
import bisect

p = None

def main():
	global p
	Tools.clearScreen()
	print """
Welcome, adventurer. Your quest is about to begin. 
Since you were young, your goal in life has been to find The Sword of Wonder.
You have 100 days to complete your quest, before your sickness takes over your body, and leaves you as weak as a small puppy.
	"""
	Tools.delay()
	Tools.clearScreen()
	p = player(100, 20, 0)
	while(p.getHealth() > 0):
		givePlayerOptions()
	Tools.createDeathScene()


def givePlayerOptions():
	Tools.clearScreen()
	print "day",Tools.getDays()
	print "*"*100
	print "Would you like to travel into town, venture into the forest, rest for the night, check your stats, or look in your bag?"
	choice = scan(raw_input(">"))
	if "forest" in choice['nouns'] or "venture" in choice['verbs']:
		visitForest()
	elif "town" in choice['nouns'] or "travel" in choice['verbs']:
		visitTown()
	elif "rest" in choice['verbs'] or "night" in choice['nouns'] or 'sleep' in choice['verbs']:
		rest()
	elif 'check' in choice['verbs'] or 'stats' in choice['nouns']:
		p.displayStats()
	elif 'look' in choice['verbs'] or 'bag' in choice['nouns']:
		p.lookInBag()
	else:
		print "I couldn't understand your response. Please answer again."
		givePlayerOptions()

def visitForest():
	Battle.init(getPlayer(), determineOpponent())
	Tools.incrementDays()

	Tools.clearScreen()

def determineOpponent():
	opponentConstructors = [createGrunt, createDigger, createHoard, createButler, createSoldier, createBodyBuilder]
	strengthThresholds = [30, 70, 90, 120, 160 ]
	strengthThresholdsIndex = bisect.bisect_left(strengthThresholds, p.getStrength()) 
	if random.randint(0,100) < 25:
		if random.randint(0,1) == 1:
			strengthThresholdsIndex = max(0, strengthThresholdsIndex-1)
		else:
			strengthThresholdsIndex = min(len(strengthThresholds)-1, strengthThresholdsIndex + 1)
	return opponentConstructors[strengthThresholdsIndex]() 

def createGrunt():
	return grunt(30 + random.randint(-5,5), 5 + random.randint(-2,2), random.randint(1,5))

def createDigger():
	return digger(70 + random.randint(-8,8), 20 + random.randint(-3,3), random.randint(3,10))

def createHoard():
	return hoard(120 + random.randint(-10,10), 45 + random.randint(-6,6), random.randint(15,22))

def createButler():
	return butler(150 + random.randint(-12,12), 60 + random.randint(-8,8), random.randint(25,40))

def createSoldier():
	return soldier(220 + random.randint(-6,15), 80 + random.randint(-6,15), random.randint(50,150))

def createBodyBuilder():
	return bodyBuilder(1000, 90, 500)

def visitTown():
	Town.init(getPlayer())

	Tools.clearScreen()
def rest():
	Tools.createSleeper()
	print "You have restored your health from", p.getHealth(),
	p.replenish(20)
	print "to", p.getHealth(), "by resting overnight."
	Tools.delay()
	Tools.incrementDays()

def getPlayer():
	global p
	return p

if __name__ == '__main__':
	main()