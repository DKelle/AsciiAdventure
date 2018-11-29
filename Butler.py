from Enemy import enemy

class butler(enemy):
    def __init__(self, health, strength, money):
        super(butler, self).__init__(health, strength, money)
        self.name = "Butler"
