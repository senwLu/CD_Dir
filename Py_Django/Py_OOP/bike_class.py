class Bike:
    def __init__(self, price, max_speed):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed

    def displayInfo(self):
        print(f'{self.price} - {self.max_speed} - {self.miles}')

    def ride(self):
        self.miles += 10

        # return self, useful/needed when planning to chain
        # if no return self present during chaining
        # will throw...AttributeError: 'NoneType' object has no attribute
        return self

    def reverse(self):
        if(self.miles - 10 < 0):
            print('0 miles, can not go lower')
        else:
            self.miles -= 10
        return self


bike1 = Bike(200, "25mph")


bike1.displayInfo()
bike1.ride().ride().ride().reverse()
bike1.displayInfo()
bike1.reverse().reverse()
bike1.displayInfo()
bike1.reverse()
