class Dot:
    def __init__(self, ind=""):
        self.x = int(ind[0])
        self.y = int(ind[1])
        self.v = ind

    def __str__(self):
        return f"точка {self.v}"

a = Dot("15")
b = Dot("16")

class Ship:
    status = "full"

    def __init__(self, size=0, head="", direction="", lifes=0):
        self.size = size
        self.head = head
        self.direction = direction
        self.lifes = lifes
    def __str__(self):
        return f"корабль {self.dots}"
    @property
    def dots(self):
        if self.direction == "h":
            return [Dot(self.head[0] + str(int(self.head[1]) + i)) for i in range(self.size)]
        else:
            return [Dot(str(int(self.head[0]) + i) + self.head[1]) for i in range(self.size)]

ship = Ship(3,"15","v",3)

print(a)
#for i in ship.dots:
#    print(i)
#print(ship.dots)

if a in ship.dots:
    print(a)

