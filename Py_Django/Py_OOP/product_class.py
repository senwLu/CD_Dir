class Product:
    def __init__(self, price, item_name, weigth, brand):
        self.price = price
        self.item_name = item_name
        self.weigth = weigth
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


car = Product(2000, 'Ford', '2000lb', 'F1')
print(car.status)
car.return_item('opened')
print(car.status)
print(car.price)
