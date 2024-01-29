from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name, calories, flavor=None,):
        super().__init__(name, calories)
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True


dish = JellyBean(str(input().lower()), int(input()), flavor=str(input().lower()))

print(dish.is_healthy())
print(dish.is_delicious())
