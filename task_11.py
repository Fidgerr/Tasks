class Dessert:
    def __init__(self, name=None, calories=0):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        if self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True
