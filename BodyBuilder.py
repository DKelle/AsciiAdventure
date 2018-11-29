from Enemy import enemy

class bodyBuilder(enemy):
    def __init__(self, health, strength, money):
        super(bodyBuilder, self).__init__(health, strength, money)
        self.name = "Body builder"
