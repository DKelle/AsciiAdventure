from Enemy import enemy

class soldier(enemy):
    def __init__(self, health, strength, money):
        super(soldier, self).__init__(health, strength, money)
        self.name = "Soldier"
