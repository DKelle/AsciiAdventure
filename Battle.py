from Entity import entity
import Tools
from scanner import scan
import random

p = None
opponent = None
battleOver = False

def init(player, opp):
    Tools.clearScreen()
    global p
    global opponent
    global battleOver
    battleOver = False
    p = player
    opponent = opp

    p.setOpponent(opponent)
    opponent.setOpponent(p)

    print "While in the forrest, you encountered a",opponent.getName(),"!"
    Tools.delay()
    enterBattleLoop()


def enterBattleLoop():
    global battleOver
    while(not battleOver):
        redraw(opponent.getName())
        giveBattleOptions()

def giveBattleOptions():
    print "Do you want to attack, run, view your opponents/your stats, or look in your bag?"
    choice = scan(raw_input(">"))
    if 'attack' in choice['verbs'] or 'fight' in choice['verbs']:
        enterFight()
    elif 'run' in choice['verbs']:
        run()
    elif 'look' in choice['verbs'] or 'bag' in choice['nouns']:
        p.lookInBag()
    elif 'stats' in choice['nouns']:
        if 'opponent' in choice['nouns'] or 'opponents' in choice['nouns']:
            opponent.displayStats()
        elif 'my' in choice['nouns'] or 'mine' in choice['nouns']:
            p.displayStats()
        else:
            choice = scan("Would you like to view your stats, or the opponents stats?\n>")
            if 'mine' in choice['nouns'] or 'my' in choice['nouns']:
                p.displayStats()
            elif 'opponent' in choice['nouns'] or 'opponents' in choice['nouns']:
                opponent.displayStats()


def enterFight():

    p.attack()
    redraw(opponent.getName())
    print "You have dealt", p.getLastAttackDamage(), "damage to your opponent"
    Tools.delay()

    if checkIfBattleOver():
        return

    opponent.makeMove()
    print "Opponent has dealt ", opponent.getLastAttackDamage(), "damage to you"
    Tools.delay()
    redraw(opponent.getName())

    checkIfBattleOver()

def redraw(name):
    Tools.clearScreen()
    Tools.createBattleScene(p.getHealth(), p.getMaxHealth(), opponent.getHealth(), opponent.getMaxHealth(), name)


def checkIfBattleOver():
    if p.getHealth() <= 0 or opponent.getHealth() <= 0:
        endBattle()
        return True

def endBattle():
    global battleOver
    battleOver = True

    wonBattle = opponent.getHealth() <= 0
    if wonBattle:
        opponent.playLoseScreen(p)
    else:
        p.playLoseScreen(opponent)


def run():
    print "You have run away like a wee baby."
    if random.randint(1,3) == 3:
        damage = random.randint(opponent.getStrength()/5, opponent.getStrength())
        print "While escaping, your opponent got one attack off, and you sustained", damage,"damage."
        p.inflict(damage)
    Tools.delay()
    global battleOver
    battleOver = True
