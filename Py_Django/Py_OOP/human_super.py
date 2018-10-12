class Human:
    def __init__(self):
        self.health = 5
        self.intelligence = 3
        self.strength = 2
        self.stealth = 1


class Wizard(Human):
    def __init__(self):
        super().__init__()  # use super to call the Human __init__() method
        # every wizard starts off with 10 intelligence, overwriting the 3 from Human
        self.intelligence = 10

    def heal(self):
        self.health += 10  # all wizards also get a heal() method


class Ninja(Human):
    def __init__(self):
        super().__init__()  # use super to call the Human __init__() method
        # every Ninja starts off with 10 stealth, overwriting the stealth of 1 from Human
        self.stealth = 10

    def steal(self):
        self.stealth += 5  # all ninjas also get a steal() method


class Samurai(Human):
    def __init__(self):
        super().__init__()  # use super to call the Human __init__() method
        # every Samurai starts off with 10 strength, overwriting the 2 from Human
        self.strength = 10

    def sacrifice(self):
        self.health -= 5
