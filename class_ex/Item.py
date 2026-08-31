class Item:
    def __init__(self, uid, name, category, price, manufacturer):
        self.__uid = uid
        self.__name = name
        self.__category = category
        self.__price = price
        self.__manufacturer = manufacturer

    @property
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, new_uid):
        self.__uid = new_uid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        self.__category = new_category

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, new_manufacturer):
        self.__manufacturer = new_manufacturer

    def print_item(self):
        print(f'{self.name} ({self.category}) sold at: {self.price}$, manufactured by {self.manufacturer}')


if __name__ == "__main__":
    smartphone = Item(1, 'Iphone534', 'Smartphone', 30000000, "Apple")
    earphones = Item(2, 'xin you min', 'Audio Accessories', 34, "China")

    earphones.manufacturer = 'AliExpress'

    smartphone.print_item()
    earphones.print_item()