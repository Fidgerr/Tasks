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
        return True
