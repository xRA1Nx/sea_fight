class Dot:
    def __init__(self, ind=""):
        self.x = int(ind[0])
        self.y = int(ind[1])
        self.v = ind


class Ship:
    status = "full"

    def __init__(self, size=0, head="", direction="", lifes=0):
        self.size = size
        self.head = head
        self.direction = direction
        self.lifes = lifes

    @property
    def dots(self):
        if self.direction == "horisontal":
            ship_dots = [Dot(self.head[0] + str(int(self.head[1]) + i)) for i in range(self.size)]
            return ship_dots
        else:
            ship_dots = [Dot(str(int(self.head[0]) + i) + self.head[1]) for i in range(self.size)]
            return ship_dots

    @property
    def dotvalues(self):
        vals = [dot.v for dot in self.dots]
        return vals



