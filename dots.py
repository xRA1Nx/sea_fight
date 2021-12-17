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

# or (d == "vertical" and sh_dot[1] == fr_point[1] and abs(
#     int(sh_dot[0]) - int(fr_point[0])) == 1) and fr_point not in item.dots \
# or (d == "horisontal" and sh_dot[0] == fr_point[0] and abs(int(sh_dot[1]) - int(fr_point[1])) == 1) and fr_point not in item.dots:

