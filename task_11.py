desserts = ['donut', 'biscuit', 'pudding', 'icecream']


class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = int(calories)

    def is_healthy(self):
        if self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        if self.name in desserts:
            return True
        else:
            return False


dish = Dessert(str(input().lower()), int(input()))

print(dish.is_delicious())
print(dish.is_healthy())
