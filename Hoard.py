from Enemy import enemy

class hoard(enemy):
    def __init__(self, health, strength, money):
        super(hoard, self).__init__(health, strength, money)
        self.name = "Hoard"