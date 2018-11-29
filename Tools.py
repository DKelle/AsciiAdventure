import os
import time
import asciiConjoiner

days = 1
message = ""

def getAmount(greeting, errorMessage, cap):
    print greeting
    amount =  int(raw_input(">"))
    if amount > cap:
        print errorMessage, "", cap
        return cap
    return amount

def incrementDays():
    global days
    days += 1
def getDays():
    global days
    return days

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def drawHealthPotion(num):
    if num == 0:
        return
    print "Health potion *",num
    print """


        [~]
        |=|
      .-' '-.
      |-----|
      | ~~~ |
      | ~~~ |
      | XXX |
      |-----|
      '-----'


    """

def drawStrengthPotion(num):
    if num == 0:
        return
    print "Strength potion *",num
    print """
         []
        [||]
        ||||
        |  |
        |  |
       /    \\
       ||~~||
       ||  ||
       ||  ||
       ||  ||
       ||  ||
       |/  \|
       |-..'|
       `----`

    """

def drawBag(itemList):
    clearScreen()
    drawHealthPotion(itemList["health potion"])
    drawStrengthPotion(itemList["strength potion"])



def createPotionShop():
    print """
    Welcome to the potion shop!

                              O
                  _O_            )=(
         .--.     ) (           /   \\
        .'=='.  .'  _'.   ()    |__ |
        |____|  |  |  |  )""(   |  ||   {}
        |____|  |  |__| ( [] )  |__||   )(
        |    |  |     |  )__(   |   |  (__)
        '----'  '-----'         |___|           """

def createSleeper():
    clearScreen()
    print """


         .--"-.-"-.
       .'     /    '.               _
      /   __./__     \              /_
     ; .-'      `-.  ;            Z
     || ---    --- \ |          Z
     /|  vvv   vvv  |\        Z
     \|     /       |/     z
      |    '--      |  z
      \   .-.-.     /
       '. `'''`  .'
       /'--._.--'\\

    """

def createDeathScene():
  print """

 ::::::::::::::::::::::::::::::::::::::::::::::::::::::
 ::::::::::::::::::::::::::::::::::::::::::::::::::::::
 ::::::::::::::::::::::::::::::::::::::::::::::::::::::
 ::::::::::::::::::::::::::_:::::::::::::::::::::::::::
 :::::::::::::::::::::::::/ |::::::::::::::::::::::::::
 :::::::::::::::::::::/ \ | | /\:::::::::::::::::::::::
 ::::::::::::::::::::::\ \| |/ /:::::::::::::::::::::::
 :::::::::::::::::::::::\ Y | /___:::::::::::::::::::::
 :::::::::::::::::::::.-.) '. `__/:::::::::::::::::::::
 ::::::::::::::::::::(.-.   / /::::::::::::::::::::::::
 ~^~_-~^^-^~^_~^_^-~^~^-~| ' |~^~_-~^_^-^~^_~^_^-~^~^-~
 ~^-_~^-~^_~^-~^_~^-_ _^,|___| ,~_ _~^-_~^-~^_~^-~^_~^-
 ~^-~^~-_~^__.===~'`__..[_____]-..__`'~===.__~^-~^~-_~^
 ~_~^_.=~~'   ~_.==~-.-~|     |~=.-~==._~^-^'~~=._~_~^
 ~-:`-~^-~^_~^:-~^~-_~-.`-===-'_.=~-_~^-_:~^-~^-_~`;-~
  ~-'._~^-~^-_^~=._~-~_~-'~~'~`_^-~_^_.=~-~^-_~^-_.'^-
 _~^-~^~=._~^-~^_-^~~==..,~_^_,..==~~-_~^-~^-_.=~_~^-~^
 _-~^-~^_~^`~==.__-~^_~^-_~^-_~^-_~^-~__.==~`_-~^-~^_~^
 -~_~^~-~^-~^~_~^~`~~~==,,....,,==~~~`-~_~^~-~^-~^~_~^~
  ~jgs^-~^-_~^~^_-^~^-~^~-_~^-~^-~^_~^~-~^~-~^-~^-~^-~^
  ~^~^-~^-~^_~^~-^~_~^-^~^~^-~^-~^~^~-^~-~^-~^~~-^~-^~^

  """

  print "You died. As you realize that you will never have what it takes to become a real adventurer, you drown to death in a pool of your own tears."

def createBattleScene(playerHealth, playerMaxHealth, opponentHealth, opponentMaxHealth, name):
  clearScreen()
  print "You have encountered a "+name
  createOpponentHealthBar(opponentHealth, opponentMaxHealth)

  print "\n\n"

  fileA = open("ascii/myCharacter.txt").readlines()
  fileB = open("ascii/"+''.join(name.split())+".txt").readlines()

  startFileB = len(fileA) - len(fileB)

  if startFileB < 0:
    for i in range(startFileB, 0):
      print "\t\t\t\t\t\t"+fileB[i-startFileB],


    for index,line in enumerate(fileA):
      print line.rstrip()+"\t\t\t\t"+fileB[index-startFileB],


  else:
    for i in range(0, startFileB):
      print fileA[i],

    for index, line in enumerate(fileB):
      print fileA[index+startFileB].rstrip() +"\t\t\t\t"+ line,

  print "\n\n"

  createPlayerHealthBar(playerHealth, playerMaxHealth)

  print "\n\n"

def createPlayerHealthBar(health, maxHealth):
    for i in range(0,3):
        print "|",
        print "*" * int(min(100*health/maxHealth/5, 20)),
        print " " * int(20 - 100*health/maxHealth/5),
        print "|",
        if i == 1:
            print "Health:", health
        else:
            print ""



def createOpponentHealthBar(health, maxHealth):
    for i in range(0,3):
        print "\t"*7,"|",
        print "*" * int(min(100*health/maxHealth/5, 20)),
        print " " * int(20 - 100*health/maxHealth/5),
        print "|",
        if i == 1:
            print "Health:", health
        else:
            print ""

def delay(seconds):
    time.sleep(seconds)

def delay():
    raw_input("(press enter when ready)")
