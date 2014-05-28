from Enemy import enemy

class digger(enemy):
	def __init__(self, health, strength, money):
		super(digger, self).__init__(health, strength, money)
		self.name = "Digger"