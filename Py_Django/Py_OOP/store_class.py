from my_modules.product_class import Product


class Store:
    def __init__(self, location, owner):
        self.list = []
        self.location = location
        self.owner = owner

    def add_product(self, obj):
        (self.list).append(obj)
        return self

    def remove_product(self, item):
        result = []
        storeList = self.list
        for i in storeList:
            if i.item_name != item:
                result.append(i)
        self.list = result
        return self

    def show_list(self):
        for i in self.list:
            print(i.item_name)


car = Product(2000, 'Ford', '2000lb', 'F1')
bike = Product(1000, 'Ducati', '100lb', 'F2')

store1 = Store('Seattle', 'Dan')
store1.add_product(car)
store1.add_product(bike)
store1.show_list()
store1.remove_product('Ford')
store1.show_list()
