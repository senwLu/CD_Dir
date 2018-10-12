class Car:
    # def __init__(self, price, speed, fuel, mileage):
    #     self.price = price
    #     self.speed = speed
    #     self.fuel = fuel
    #     self.mileage = mileage
    #     self.tax = 0.15 if self.price > 10000 else 0.12

    # def display_all(self):
    #     print(f'Price: {self.price}')
    #     print(f'Speed: {self.speed}')
    #     print(f'Fuel: {self.fuel}')
    #     print(f'Mileage: {self.price}')
    #     print(f'Tax: {self.tax}')

    ######################################################

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def display_all(self):
        print(f'Price: {self.price}')
        print(f'Speed: {self.speed}')
        print(f'Fuel: {self.fuel}')
        print(f'Mileage: {self.price}')
        # if self.price < 10000:
        #     print(f'Tax: {0.12}')
        # else:
        #     print(f'Tax: {0.15}')
        ### or ###
        print(f'Tax: {0.12}') if self.price < 10000 else print(f'Tax: {0.15}')


car1 = Car(9000, '35mph', 'full', '15mph')

car1.display_all()
