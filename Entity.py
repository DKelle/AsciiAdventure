import Tools
import random

class entity(object):

	def __init__(self, health, strength, money):
		self.name = "entity"
		self.health = health
		self.startingHealth = health
		self.maxHealth = max(100, self.health)
		self.strength = strength
		self.money = money
		self.bag = []
		self.opponent = None
		self.lastAttackDamage = 0
		

	def getStartingHealth(self):
		return self.startingHealth

	def replenish(self, hp):
		self.health = min(self.maxHealth, self.health + hp)

	def inflict(self, damage):
		self.health = max(self.health - damage, 0)

	def attack(self):
		damage = self.strength + random.randint(-1 * self.strength/5, self.strength/5)
		self.opponent.inflict(damage)
		self.setLastAttackDamage(damage)

	def setLastAttackDamage(self, damage):
		self.lastAttackDamage = damage

	def getLastAttackDamage(self):
		return self.lastAttackDamage

	def getHealth(self):
		return self.health

	def getStrength(self):
		return self.strength

	def increaseStrength(self, increase):
		self.strength += increase

	def getMoney(self):
		return self.money

	def setOpponent(self, enemy):
		self.opponent = enemy

	def increaseMaxHealth(self, hp):
		self.maxHealth += hp

	def getMaxHealth(self):
		return self.maxHealth

	def getName(self):
		return self.name

	def displayStats(self):
		print "Name:", self.getName()
		print "Max health:",self.getMaxHealth()
		print "Current health:",self.getHealth()
		print "Strength", self.getStrength()
		print "Money", self.getMoney()
		Tools.delay()

