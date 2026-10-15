class Item:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __hash__(self):
        return hash((self.name, self.category))

    def __eq__(self, other):
        return (self.name, self.category) == (other.name, other.category)

    def __repr__(self):
        return f'Item=(name={self.name!r}, category={self.category!r}, quantity={self.quantity!r}, price={self.price!r})'


items = {
    Item('laptop', 'Computers', 100, 2399.5): 100,
    Item('Tablet', 'Computers', 200, 1399.5): 200,
    Item('Speakers', 'Sound', 500, 233): 500
}

print(items)
items[Item('Speakers', 'Sound', 100, 100)] = 100
print(items)

print(items[Item('Speakers', 'Sound', None, None)])
