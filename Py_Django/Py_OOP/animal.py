class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display(self):
        print(self.health)


# animal1 = Animal('hotdog', 20)
# animal1.walk().walk().walk().run().run()
# animal1.display()

class Dog(Animal):
    def __init__(self):
        self.health = 150

    def pet(self):
        self.health += 5
        return self


# dog1 = Dog()
# dog1.walk().walk().walk().run().run().pet()
# dog1.display()

class Dragon(Animal):
    def __init__(self):
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        self.display()
        print('I am a dragon')


# drag1 = Dragon()
# drag1.fly().fly().fly()
# drag1.display_health()
