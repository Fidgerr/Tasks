from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name=None, calories=0, flavor=None):
        super().__init__(name, calories)
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True
