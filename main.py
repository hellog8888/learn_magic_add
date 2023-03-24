class Budget:
    def __init__(self):
        self.budget = []

    def add_item(self, it):
        self.budget.append(it)

    def remove_item(self, indx):
        del self.budget[indx]

    def get_items(self):
        return self.budget


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        temp = other.money if isinstance(other, Item) else other
        return self.money + temp

    def __radd__(self, other):
        return self + other