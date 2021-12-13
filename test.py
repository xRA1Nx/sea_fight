board = [[f"  {chr(96 + j)}  " if i == 0 else (str(i) if j == 0 else "| O |") for j in range(6 + 1)] for i in range(6 + 1)]
board[0][0] = ""


turn = input("сделайте выстрел: \t").lower()
if turn[0].isdigit():
    turn = turn[::-1] #Можно делать ход в формате a1 или 1a, большими строчными буквами,без раницы.
print(turn)
#if turn[0] in [chr(96+i) for i in range(1,7)] or turn[1] in range(1,7): #or board[int(turn[1])][ord(turn[0])] != "X":
     #board[int(turn[1])][ord(turn[0])] = "X"
print(int(turn[1])-1)
print(ord(turn[0])-97)

for raw in board:
    raw = list(map(lambda x: x.ljust(2), raw))
    print(*raw)