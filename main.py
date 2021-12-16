from random import randrange
matrix1 = [[f"  {chr(96 + j)}  " if i == 0 else (str(i) if j == 0 else "| O |") for j in range(6 + 1)] for i in range(6 + 1)]
matrix1[0][0] = ""

matrix2 = [[f"  {chr(96 + j)}  " if i == 0 else (str(i) if j == 0 else "| 0 |") for j in range(6 + 1)] for i in range(6 + 1)]
matrix2[0][0] = ""

def generat_ship_list():
    filled_area = set()
    sizes = [3, 2, 1]
    dir_list = ["vertical", "horisontal"]
    ship_list = []
    free_points = [j + i for j in "".join(map(str, (range(1, 6 + 1)))) for i in "".join(map(str, (range(1, 6 + 1))))]

    def refresh_freepoints_and_field_area(fp, item, filled_area):
        fp = sorted(list(set(fp)-set(item.dots)))
        for fr_point in fp:
            for sh_dot in item.dots:
                if abs(int(sh_dot[0]) - int(fr_point[0])) == 1 and abs(int(sh_dot[1]) - int(fr_point[1])) == 1 \
                        or abs(int(sh_dot[0]) - int(fr_point[0])) == 1 and abs(int(sh_dot[1]) - int(fr_point[1])) == 0 \
                        or abs(int(sh_dot[0]) - int(fr_point[0])) == 0 and abs(int(sh_dot[1]) - int(fr_point[1])) == 1: #\
                    filled_area.add(fr_point)
        fp = sorted(list(set(free_points) - set(item.dots) - filled_area))
        ship_list.append(item)

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

    def operation():
        nonlocal dir, temp, h
        dir = dir_list[randrange(2)]
        temp = refresh_temp(free_points, s)
        if temp:
            h = temp[randrange(len(temp))] # голова коробля
        else:
            h = None
        return dir, temp, h


    for s in sizes:
        if s == 3:
            dir, temp, h = operation()
            big_ship = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(free_points, big_ship, filled_area)
        elif s == 2:
            if not h:
                return generat_ship_list()
            dir, temp, h = operation()
            medium_ship1 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(free_points, medium_ship1, filled_area)

            dir, temp, h = operation()
            if not h:
                return generat_ship_list()
            medium_ship2 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(free_points, medium_ship2, filled_area)

        elif s == 1:
            dir, temp, h = operation()
            if not h:
                return generat_ship_list()
            small_ship1 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(free_points, small_ship1, filled_area)

            dir, temp, h = operation()
            if not h:
                return generat_ship_list()
            small_ship2 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(free_points, small_ship2, filled_area)

            dir, temp, h = operation()
            if not h:
                return generat_ship_list()
            small_ship3 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(free_points, small_ship3, filled_area)

            dir, temp, h = operation()
            if not h:
                return generat_ship_list()
            small_ship4 = Ship(size=s, head=h, direction=dir, lifes=s)
            free_points, filled_area = refresh_freepoints_and_field_area(free_points, small_ship4, filled_area)
    return ship_list



class Dot:
    def __init__(self, x="", y=""):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"точка {self.y}{self.x}"


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
        return [self.head[0] + str(int(self.head[1]) + i) for i in range(self.size)] if self.direction == "horisontal" \
        else [str(int(self.head[0]) + i) + self.head[1] for i in range(self.size)]




class Board():
    # board = [[f"  {chr(96 + j)}  " if i == 0 else (str(i) if j == 0 else "| O |") for j in range(6 + 1)] for i in range(6 + 1)]
    # board[0][0] = ""
    board = None

    def __init__(self, ships_list=None, hide=None, count_live_ships=0):
        self.ships_list = ships_list
        self.hide = hide
        self.count_live_ships = 7

    @property
    def show_board(self):
        for raw in self.board:
            raw = list(map(lambda x: x.ljust(2), raw))
            print(*raw)


    def check(self, ft):
        counter = 0
        for ship in self.ships_list:
            ship.lifes = sum(map(lambda x: 1 if player_desk.board[int(x[0])][int(x[1])] ==  "| ■ |" else 0, ship.dots))
            if ship.lifes > 0:
                counter += 1
                if ship.lifes < ship.size:
                    print(ship, "ранен")

            else:
                for f in ft:
                    for dot in ship.dots:
                        if abs(int(f[0]) - int(dot[0])) == 1 and abs(int(f[1]) - int(dot[1])) == 1 \
                                or abs(int(f[0]) - int(dot[0])) == 1 and abs(int(f[1]) - int(dot[1])) == 0 \
                             or abs(int(f[0]) - int(dot[0])) == 0 and abs(int(f[1]) - int(dot[1])) == 1:
                            self.board[int(f[0])][int(f[1])] = "| X |"
            self.count_live_ships = counter










    def player_shot(self):
        flag = True
        while flag:
            try:
                turn = input("\n\t\t\t\t\tсделайте выстрел: \t").lower()
                if turn[0].isdigit():
                    turn = turn[::-1]  #Можно делать ход в формате a1 или 1a, большими строчными буквами,без раницы.

                elif len(turn)!=2 or not turn[1].isdigit():
                    raise ValueError("Ход введен не коректно, придерживайтесь формата 'А1'")

                elif turn[0] not in [chr(96+i) for i in range(1, 7)] or int(turn[1]) not in range(1, 7):
                    raise ValueError("Стрелять возможно только в пределах игрового поля")

                elif ii_desk.board[int(turn[1])][ord(turn[0])-96] in ["| X |", "| ! |"]:
                    raise ValueError("Сюда уже стреляли")

            except ValueError as e:
                print(e)

            else:
                ii_desk.board[int(turn[1])][ord(turn[0])-96] = "| X |"
                flag = False

    def ii_shot(self, ii_free_turns):
        flag_hit = False
        turn = ii_free_turns[randrange(len(ii_free_turns))]
        print("ход противника: ", turn)
        #turn = input("\n\t\t\t\t\tсделайте выстрел: \t").lower()
        if player_desk.board[int(turn[0])][int(turn[1])] == "| O |":
            player_desk.board[int(turn[0])][int(turn[1])] = "| X |"
        else:
            player_desk.board[int(turn[0])][int(turn[1])] = "| ! |"
            flag_hit = True
        return flag_hit

player_desk = Board(ships_list=generat_ship_list(), hide=False, count_live_ships=7)
player_desk.board = matrix1.copy()

ii_desk = Board(ships_list=generat_ship_list(), hide=True, count_live_ships=7)
ii_desk.board = matrix2.copy()


def game():
    ii_free_turns = [j + i for j in "".join(map(str, (range(1, 6 + 1)))) for i in "".join(map(str, (range(1, 6 + 1))))]

    # размещаем корабли игрока на доске
    for ship in player_desk.ships_list:
        for dot in ship.dots:
            player_desk.board[int(dot[0])][int(dot[1])] = "| ■ |"

    while any([player_desk.count_live_ships, ii_desk.count_live_ships]):
        if ii_desk.count_live_ships == 0:
            print("Поздравляем, вы победили")
            break
        elif player_desk.count_live_ships == 0:
            print("вы проиграли")

        print("колличество живых кораблей =", player_desk.count_live_ships)

        print("Ваше игровое поле")
        player_desk.show_board
        print()
        print("Поле противника")
        ii_desk.show_board

        player_desk.player_shot()

        #Ходит компьютер
        flag_ii_hit = ii_desk.ii_shot(ii_free_turns)
        if flag_ii_hit:
            print("по Вам попали")
            player_desk.check(ii_free_turns)
        # рефрешим список свободных ходов для компьютера
        for raw in range(len(player_desk.board)):
            for i in range(len(player_desk.board[raw])):
                #print(i, end =" ")
                if player_desk.board[raw][i] in ["| X |", "| ! |"] and str(raw)+str(i) in ii_free_turns:
                    #print("удаляем", str(raw)+str(i))
                    ii_free_turns.remove(str(raw)+str(i))

game()
