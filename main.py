from random import randrange

class Dot:
    def __init__(self, x="", y=""):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"точка {self.y}{self.x}"


class Ship:
    big_counts = 1
    medium_counts = 2
    small_counts = 4

    def __init__(self, size=0, head="", direction="", lifes=0):
        self.size = size
        self.head = head
        self.direction = direction
        self.lifes = lifes
    def __str__(self):
        return f"корабль {self.dots}"


    @property
    def dots(self):
        return [self.head[0] + str(int(self.head[1]) + i) for i in range(self.size)] if self.direction == "horisontal" \
        else [str(int(self.head[0]) + i) + self.head[1] for i in range(self.size)]


class Board():
    board = [[f"  {chr(96 + j)}  " if i == 0 else (str(i) if j == 0 else "| O |") for j in range(6 + 1)] for i in range(6 + 1)]
    board[0][0] = ""

    def __init__(self, ships_list=None, hide=None, count_live_ships=0):
        self.ships_list = ships_list
        self.hide = hide
        self.count_live_ships = 7


    @property
    def show_board(self):
        for raw in self.board:
            raw = list(map(lambda x: x.ljust(2), raw))
            print(*raw)

    def shot(self):
        try:
            turn = input("сделайте выстрел: \t").lower()
            if turn[0].isdigit():
                turn = turn[::-1]  #Можно делать ход в формате a1 или 1a, большими строчными буквами,без раницы.

            elif len(turn)!=2 or not turn[1].isdigit():
                raise ValueError("Ход введен не коректно, придерживайтесь формата 'А1'")

            elif turn[0] not in [chr(96+i) for i in range(1, 7)] or int(turn[1]) not in range(1, 7):
                raise ValueError("Стрелять возможно только в пределах игрового поля")

            elif self.board[int(turn[1])][ord(turn[0])-96] == "X":
                raise ValueError("Сюда уже стреляли")

        except ValueError as e:
            print(e)
        else:
            self.board[int(turn[1])][ord(turn[0])-96] = "| X |"


def generat_ship_list(pole):
    filled_area = set()
    sizes = [3, 2, 1]
    dir_list = ["vertical", "horisontal"]
    ship_list = []
    free_points = [j + i for j in "".join(map(str, (range(1, 6 + 1)))) for i in "".join(map(str, (range(1, 6 + 1))))]

    def refresh_freepoints_and_field_area(d, fp, item, filled_area):
        fp = sorted(list(set(fp)-set(item.dots)))
        for fr_point in fp:
            for sh_dot in item.dots:
                if abs(int(sh_dot[0]) - int(fr_point[0])) == 1 and abs(int(sh_dot[1]) - int(fr_point[1])) == 1 \
                        or abs(int(sh_dot[0]) - int(fr_point[0])) == 1 and abs(int(sh_dot[1]) - int(fr_point[1])) == 0 \
                        or abs(int(sh_dot[0]) - int(fr_point[0])) == 0 and abs(int(sh_dot[1]) - int(fr_point[1])) == 1: #\
                    filled_area.add(fr_point)
        fp = sorted(list(set(free_points) - set(item.dots) - filled_area))
        return fp, filled_area

    def refresh_temp(fp, s):
        temp = fp.copy()
        if dir == "vertical":
            for i in fp:
                if int(i[0]) > 7 - s:
                    temp.remove(i)
            if s == 2:
                for f in fp:
                    if str(int(f[0])+1)+f[1] not in temp:
                        if f in temp:
                              temp.remove(f)
        if dir == "horisontal":
            for i in fp:
                if int(i[1]) > 7 - s:
                    temp.remove(i)
            if s == 2:
                for i in range(1, len(fp)):
                    if int(fp[i]) - int(fp[i - 1]) != 1:
                        if fp[i-1] in temp:
                            temp.remove(fp[i - 1])
        return temp
    try:
    for s in sizes:
        if s == 3:
            dir = dir_list[randrange(2)]
            temp = refresh_temp(free_points, s)
            h = temp[randrange(len(temp))] # голова коробля
            big_ship = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(dir, free_points, big_ship, filled_area)
            ship_list.append(big_ship)
        elif s == 2:
            dir = dir_list[randrange(2)]
            temp = refresh_temp(free_points, s)
            h = temp[randrange(len(temp))]  # голова коробля
            medium_ship1 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(dir, free_points, medium_ship1, filled_area)
            ship_list.append(medium_ship1)

            dir = dir_list[randrange(2)]
            temp = refresh_temp(free_points, s)
            h = temp[randrange(len(temp))]  # голова коробля
            medium_ship2 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(dir, free_points, medium_ship2, filled_area)
            ship_list.append(medium_ship2)
        elif s == 1:
            dir = dir_list[randrange(2)]
            temp = refresh_temp(free_points, s)
            h = temp[randrange(len(temp))]  # голова коробля
            small_ship1 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(dir, free_points, small_ship1, filled_area)
            ship_list.append(small_ship1)

            dir = dir_list[randrange(2)]
            temp = refresh_temp(free_points, s)
            h = temp[randrange(len(temp))]  # голова коробля
            small_ship2 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(dir, free_points, small_ship2, filled_area)
            ship_list.append(small_ship2)

            dir = dir_list[randrange(2)]
            temp = refresh_temp(free_points, s)
            h = temp[randrange(len(temp))]  # голова коробля
            small_ship3 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(dir, free_points, small_ship3, filled_area)
            ship_list.append(small_ship3)

            dir = dir_list[randrange(2)]
            temp = refresh_temp(free_points, s)
            h = temp[randrange(len(temp))]  # голова коробля
            small_ship4 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(dir, free_points, small_ship4, filled_area)
            ship_list.append(small_ship4)



# не обязательная часть_________________________________________
        temp_matrix = xxx.board.copy()
        for item in ship_list:
            for i in item.dots:
                temp_matrix[int(i[0])][int(i[1])] = "| ■ |"
                xxx.board = temp_matrix

        temp_matrix = xxx.board.copy()
        for i in filled_area:
            temp_matrix[int(i[0])][int(i[1])] = "| - |"
            xxx.board = temp_matrix
#_______________________________________________________________

    return  ""

    #return ship_list


        #ship_list.append()

xxx = Board()
#xxx.show_board
#xxx.shot()
#xxx.show_board

#print(*generat_ship_list(xxx.board))
print()
print(generat_ship_list(xxx.board))

xxx.show_board

