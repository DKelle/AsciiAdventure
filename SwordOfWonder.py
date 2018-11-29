from Enemy import enemy
import Tools

class swordOfWonder(enemy):
    def __init__(self):
        super(swordOfWonder, self).__init__(-1, 10000, 10000)
        self.name = "The Sword Of Wonder"

        def playLoseScreen(self, p):
            swordAscii = open("ascii/TheSwordOfWonder.txt").readlines()
            print 'the sword ofwonder is {}'.format(swordAscii)
            for line in swordAscii:
                print "\t\t{}".format(line)

            print "\n\n\n\n"
            "Congratulations, {}. You have finally found the Sword Of Wonder. You have completed your quest.".format(p.name)
            Tools.delay()
            p.addMoney(self.getMoney())
