from Entity import entity

class enemy(entity):
	def __init__(self, health, strength, money):
		super(enemy, self).__init__(health, strength, money)

	def makeMove(self):
		super(enemy, self).attack()