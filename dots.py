#в задании не использовалось
class Dot:
    def __init__(self, x="", y=""):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"точка {self.y}{self.x}"




ship_list=[]

class Ship:
    status = "full"

    def __init__(self, size=0, head="", direction="", lifes=0):
        self.size = size
        self.head = head
        self.direction = direction
        self.lifes = lifes

    def __str__(self):
        return f"корабль {self.size}"


    @property
    def dots(self):
        if self.direction == "horisontal":
            return [self.head[0] + str(int(self.head[1]) + i) for i in range(self.size)]
        else:
            return [str(int(self.head[0]) + i) + self.head[1] for i in range(self.size)]

sizes = [3,2,2,1,1,1,1]
for s in sizes:
    a= Ship(s,11,"верх",s)
    ship_list.append(a)


print(a)