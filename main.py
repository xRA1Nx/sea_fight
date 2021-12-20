from random import randrange


# функция генерации кораблей. Размещаем коробаль по одному от больших к маленьким,
# если кораблю не хватает место, то генерация запускается по новой
def generat_ship_list():
    filled_area = set()
    sizes = [3, 2, 2, 1, 1, 1, 1]
    dir_list = ["vertical", "horisontal"]
    ship_list = []
    free_points = [j + i for j in "".join(map(str, (range(1, 6 + 1)))) for i in "".join(map(str, (range(1, 6 + 1))))]

    # убираем из свободных точек
    def refresh_freepoints_and_field_area(fp, item, fa):
        fp = sorted(list(set(fp) - set(item.dotvalues)))
        for f in fp:
            for dot in item.dots:
                if abs(int(dot.v[0]) - int(f[0])) == 1 and abs(int(dot.v[1]) - int(f[1])) == 1 \
                        or abs(int(dot.v[0]) - int(f[0])) == 1 and abs(int(dot.v[1]) - int(f[1])) == 0 \
                        or abs(int(dot.v[0]) - int(f[0])) == 0 and abs(int(dot.v[1]) - int(f[1])) == 1:
                    fa.add(f)
        fp = sorted(list(set(free_points) - set(item.dotvalues) - fa))
        ship_list.append(item)
        return fp, fa

    # обновление temp файла, копирующего спискок возможных точек размещения головы коробля
    def refresh_temp(fp, size):
        t = fp.copy()
        if dir == "vertical":
            for i in fp:
                if int(i[0]) > 7 - size:
                    t.remove(i)
            if size == 2:
                for f in fp:
                    if str(int(f[0]) + 1) + f[1] not in t:
                        if f in t:
                            t.remove(f)
        if dir == "horisontal":
            for i in fp:
                if int(i[1]) > 7 - size:
                    t.remove(i)
            if size == 2:
                for i in range(1, len(fp)):
                    if int(fp[i]) - int(fp[i - 1]) != 1:
                        if fp[i - 1] in t:
                            t.remove(fp[i - 1])
        return t

    for s in sizes:
        dir = dir_list[randrange(2)]
        temp = refresh_temp(free_points, s)
        if temp:
            h = temp[randrange(len(temp))]  # голова коробля
        else:
            h = None
        if not h:
            return generat_ship_list()
        ship = Ship(size=s, head=h, direction=dir, lifes=s)
        free_points, filled_area = refresh_freepoints_and_field_area(free_points, ship, filled_area)
    return ship_list


# Выстрел игрока
def player_shot():
    flag = True
    hit = False
    while flag:
        try:
            turn = input("\n\t\t\t\t\tВаш выстрел: \t").lower()
            if turn[0].isdigit():
                turn = turn[::-1]  # Можно делать ход в формате a1 или 1a, большими или строчными буквами,без раницы.

            if len(turn) != 2 or turn.isdigit():
                raise ValueError("Ход введен не коректно, придерживайтесь формата 'А1'")
            elif turn[0] not in [chr(96 + i) for i in range(1, 7)] or int(turn[1]) not in range(1, 7):
                raise ValueError("Стрелять возможно только в пределах игрового поля")
            elif ii_desk.board[int(turn[1])][ord(turn[0]) - 96] in ["| X |", "| - |"]:
                raise ValueError("Сюда уже стреляли")
        except ValueError as e:
            print(e)
        else:
            turn = Dot(turn[1] + str(ord(turn[0]) - 96))
            for ship in ii_desk.ships_list:
                if turn.v in ship.dotvalues:
                    ii_desk.board[turn.x][turn.y] = "| X |"
                    hit = True
                    if ship.lifes > 1:
                        massage = "\t\t\t\t\t\t\tпопадание!\n"
                    else:
                        massage = "\t\t\t\t\t\t\tУничтожен!!\n"
                    return hit, massage
            else:
                ii_desk.board[turn.x][turn.y] = "| - |"
                massage = "\t\t\t\t\t\t\t\tВы промахнулись!!!\n"
                print(massage)
                return hit, massage
            flag = False


# Выстрел компьютера
# Если корабль подбит то стреляет во круг него, иначе рандом выстрел на свободном поле
def ii_shot(ii_free_turns):
    flag_hit = False
    priority_turns = []
    for ship in player_desk.ships_list:
        if ship.status == "wounded":
            if ship.size == 3 and ship.lifes == 1:
                temp = list(filter(lambda d: player_desk.board[d.x][d.y] == "| X |", ship.dots))
                delta = abs(int(temp[0].v) - int(temp[1].v))
                min_dot = str(int(min(temp, key=lambda d: d.v).v) - delta)
                max_dot = str(int(max(temp, key=lambda d: d.v).v) + delta)
                temp = list(filter(lambda x: x in ii_free_turns, [min_dot, max_dot]))
                priority_turns = temp.copy()
                break
            for dot in ship.dots:
                if player_desk.board[dot.x][dot.y] == "| X |":
                    for ft in ii_free_turns:
                        f = Dot(ft)
                        if (abs(f.x - dot.x) == 1 and abs(f.y - dot.y) == 0 and player_desk.board[f.x][f.y] != "| X |")\
                        or (abs(f.x - dot.x) == 0 and abs(f.y - dot.y) == 1 and player_desk.board[f.x][f.y] != "| X |"):
                            priority_turns.append(ft)
                    break
    if priority_turns:
        turn = priority_turns[randrange(len(priority_turns))]
    else:
        turn = ii_free_turns[randrange(len(ii_free_turns))]
    print("ход противника: ", chr(96 + int(turn[1])).upper() + turn[0])
    turn = Dot(turn)

    if player_desk.board[turn.x][turn.y] == "| O |":
        player_desk.board[turn.x][turn.y] = "| - |"
    else:
        player_desk.board[turn.x][turn.y] = "| X |"

        for ship in player_desk.ships_list:
            if turn.v in ship.dotvalues:
                ship.lifes -= 1
                if ship.lifes != ship.size and ship.lifes != 0:
                    ship.status = "wounded"
        flag_hit = True
    return flag_hit


def show_game():
    print("\nВаше игровое поле")
    player_desk.show_board()
    print("\nПоле противника")
    ii_desk.show_board()


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

    def __str__(self):
        return f"корабль {self.dots}"

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


class Board:
    def __init__(self, ships_list=None, hide=None, count_live_ships=0):
        self.ships_list = ships_list
        self.hide = hide
        self.count_live_ships = count_live_ships
        self.board = [[f"  {chr(96 + j)}  " if i == 0 else (str(i) if j == 0 else "| O |")
                       for j in range(6 + 1)] for i in range(6 + 1)]
        self.board[0][0] = ""

    def show_board(self):
        for raw in self.board:
            raw = list(map(lambda x: x.ljust(2), raw))
            print(*raw)

    # Проверка после выстрела (очерчиваем убитые корабли, считаем оставшиеся жизни)
    def check(self, ft):
        counter = 0
        for ship in self.ships_list:
            if self == player_desk:
                ship.lifes = sum(
                    map(lambda d: 1 if player_desk.board[d.x][d.y] == "| ■ |" else 0, ship.dots))
            else:
                ship.lifes = ship.size - sum(map(lambda d: 1 if ii_desk.board[d.x][d.y] == "| X |"
                else 0, ship.dots))
            if ship.lifes > 0:
                counter += 1
            else:
                for ind in ft:
                    f = Dot(ind)
                    for dot in ship.dots:
                        if abs(f.x - dot.x) == 1 and abs(f.y - dot.y) == 1 \
                                or (abs(f.x - dot.x) == 1 and abs(f.y - dot.y) == 0 and
                                    self.board[f.x][f.y] != "| X |") \
                                or (abs(f.x - dot.x) == 0 and abs(f.y - dot.y) == 1 and
                                    self.board[f.x][f.y] != "| X |"):
                            self.board[f.x][f.y] = "| - |"
            self.count_live_ships = counter


player_desk = Board(ships_list=generat_ship_list(), hide=False, count_live_ships=7)
ii_desk = Board(ships_list=generat_ship_list(), hide=True, count_live_ships=7)


def game():
    ii_free_turns = [j + i for j in "".join(map(str, (range(1, 6 + 1)))) for i in "".join(map(str, (range(1, 6 + 1))))]
    pl_free_turns = [j + i for j in "".join(map(str, (range(1, 6 + 1)))) for i in "".join(map(str, (range(1, 6 + 1))))]

    # рефрешим список свободных выстрелов для ИИ
    def ii_free_turns_refresh():
        for raw in range(len(player_desk.board)):
            for i in range(len(player_desk.board[raw])):
                if player_desk.board[raw][i] in ["| - |", "| X |"] and str(raw) + str(i) in ii_free_turns:
                    ii_free_turns.remove(str(raw) + str(i))

    # размещаем корабли игрока на доске
    for ship in player_desk.ships_list:
        for dot in ship.dots:
            player_desk.board[dot.x][dot.y] = "| ■ |"

    #размещаем корабли противника на доске (!!!ДЛЯ ОТЛАДКИ!!!)
    for ship in ii_desk.ships_list:
        for dot in ship.dots:
            ii_desk.board[dot.x][dot.y] = "| ■ |"

    while any([player_desk.count_live_ships, ii_desk.count_live_ships]):
        if player_desk.count_live_ships == 0:
            show_game()
            print("\n>>>>>> Вы проиграли :(  <<<<<<")
            break
        show_game()

        # ходит игрок
        flag_pl_hit, hit_massage = player_shot()
        ii_desk.check(pl_free_turns)
        while flag_pl_hit and ii_desk.count_live_ships:
            show_game()
            print("\n\t", hit_massage)
            print("\t\t\t\t\tВЫ СТРЕЛЯЕТЕ СНОВА")
            flag_pl_hit, hit_massage = player_shot()
            ii_desk.check(pl_free_turns)
        if ii_desk.count_live_ships == 0:
            show_game()
            print("\n>>>>>> Поздравляем, Вы победили! <<<<<<")
            break

        # Ходит компьютер
        flag_ii_hit = ii_shot(ii_free_turns)
        player_desk.check(ii_free_turns)
        while flag_ii_hit and player_desk.count_live_ships:
            ii_free_turns_refresh()
            flag_ii_hit = ii_shot(ii_free_turns)
            player_desk.check(ii_free_turns)
        ii_free_turns_refresh()


game()
