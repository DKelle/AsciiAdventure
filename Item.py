class item(object):
	def __init__(self, name, attack, health, cost):
		self.attack = attack
		self.health = health
		self.cost = cost
		self.name = name

	def getHealth(self):
		return self.health
	def getAttack(self): 
		return self.attack
	def getCost(self):
		return self.cost
	def getName(self):
		return self.name

	def describe(self):
		print "This is the",self.getName(),
		if self.getHealth() > 0:
			print "It will restore your health by", self.getHealth(),
		if self.getAttack() > 0:
			print "It will increase your attack by", self.getAttack(),
		print "It will cost you", self.getCost(), "though."
