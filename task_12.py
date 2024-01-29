from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, flavor):
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True


dish = JellyBean(str(input().lower()))

print(dish.is_delicious())
