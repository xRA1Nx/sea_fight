#в задании не использовалось
class Dot:
    def __init__(self, x="", y=""):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"точка {self.y}{self.x}"



