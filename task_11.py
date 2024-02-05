class Dessert:
    def __init__(self, name=None, calories=0):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        try:
            if int(self.calories) < 200:
                return True
            else:
                return False
        except:
            return None

    def is_delicious(self):
        return True