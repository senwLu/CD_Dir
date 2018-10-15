class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'

    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, tax):
        return self.price * (tax + 1)

    def return_item(self, reason_for_return):
        if reason_for_return == 'defective':
            self.status = 'defective'
        elif reason_for_return == 'like new':
            self.status = 'for sale'
        elif reason_for_return == 'opened':
            self.status = 'used'
            self.price = self.price * (1 - 0.2)
        return self

    def display_info(self):
        print(f'Item Name: {self.item_name}')
        print(f'Price: {self.price}')
        print(f'Brand: {self.brand}')
        print(f'Weight: {self.weight}')
        print(f'Status: {self.status}')


car = Product(2000, 'Ford', '2000lb', 'F1')
print(car.status)
car.return_item('opened')
print(car.status)
print(car.price)
car.display_info()
