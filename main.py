class Dot:
    def __init__(self, x="", y=""):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f"точка {self.y}{self.x}"

a1 = Dot("1", "a")
a2 = Dot("2", "a")
a3 = Dot("3", "a")
a4 = Dot("4", "a")
a5 = Dot("5", "a")
a6 = Dot("6", "a")

# noinspection PyTypeChecker
b1 = Dot(1, "b")
b2 = Dot("2", "b")
b3 = Dot("3", "b")
b4 = Dot("4", "b")
b5 = Dot("5", "b")
b6 = Dot("6", "b")

c1 = Dot("1", "c")
c2 = Dot("2", "c")
c3 = Dot("3", "c")
c4 = Dot("4", "c")
c5 = Dot("5", "c")
c6 = Dot("6", "c")

d1 = Dot("1", "d")
d2 = Dot("2", "d")
d3 = Dot("3", "d")
d4 = Dot("4", "d")
d5 = Dot("5", "d")
d6 = Dot("6", "d")

e1 = Dot("1", "e")
e2 = Dot("2", "e")
e3 = Dot("3", "e")
e4 = Dot("4", "e")
e5 = Dot("5", "e")
e6 = Dot("6", "e")

f1 = Dot("1", "f")
f2 = Dot("2", "f")
f3 = Dot("3", "f")
f4 = Dot("4", "f")
f5 = Dot("5", "f")
f6 = Dot("6", "f")

print(f5)

class Ship:
    def __init__(self, size=0, head="", direction="", lifes=0):
        self.size = size
        self.head = head
        self.direction = direction
        self.lifes = lifes

    @property
    def dots(self):
        return [self.head[0] + str(int(self.head[1]) + i) for i in range(self.size)] if self.direction == "vertical" \
        else [chr(ord(self.head[0])+i) + self.head[1] for i in range(self.size)]

big_ship = Ship(size=3,head="A3", direction="gorizontal",lifes=3)
print(big_ship.dots)

class Board():
    board = [[f"  {chr(96 + j)}  " if i == 0 else (str(i) if j == 0 else "| O |") for j in range(6 + 1)] for i in range(6 + 1)]
    board[0][0] = ""

    def __init__(self, ships_list=[], hide=None, count_live_ships=0):
        self.ships_list = ships_list
        self.hide = hide
        self.count_live_ships = 7

    @property
    def show_board(self):
        for raw in self.board:
            raw = list(map(lambda x: x.ljust(2), raw))
            print(*raw)

    # def add_ship(self):
    #     for dot in self.ship.dots:
    #         print(dot)

    def shot(self):
        turn = input("сделайте выстрел: \t").lower()
        if turn[0].isdigit():
            turn = turn[::-1] #Можно делать ход в формате a1 или 1a, большими строчными буквами,без раницы.
        if turn[0] in [chr(96+i) for i in range(1,7)] or turn[1] in range(1,7) or self.board[int(turn[1])][ord(turn[0])-96] != "X":
            self.board[int(turn[1])][ord(turn[0])-96] = "| X |"

        #if turn[0] in [chr(96+i) for i in range(1,7)] or turn[1] in range(1,7) or self.board[int(turn[1])][ord(turn[0])-96] != "X":
            #self.board[int(turn[1])][ord(turn[0])-96] = "| X |"

        column = turn[0]
        raw = turn[1]





#x = "■"

xxx = Board()
xxx.show_board
xxx.shot()
xxx.show_board


