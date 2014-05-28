from Enemy import enemy

class grunt(enemy):
	def __init__(self, health, strength, money):
		super(grunt, self).__init__(health, strength, money)
		self.name = "Grunt"
