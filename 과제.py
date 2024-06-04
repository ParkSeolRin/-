fp = open('input.txt', 'r', encoding="UTF-8")
msg_list = [m.strip() for m in fp.readlines()]
fp.close()

arr = [[0 for _ in range(8)] for _ in range(8)]

arr[0][0], arr[0][7] = "Rw", "Rw"
arr[0][1], arr[0][6] = "Nw", "Nw"
arr[0][2], arr[0][5] = "Bw", "Bw"
arr[0][3], arr[0][4] = "Qw", "Kw"
arr[1] = ["Pw"] * 8

arr[7][0], arr[7][7] = "Rb", "Rb"
arr[7][1], arr[7][6] = "Nb", "Nb"
arr[7][2], arr[7][5] = "Bb", "Bb"
arr[7][3], arr[7][4] = "Qb", "Kb"
arr[6] = ["Pb"] * 8

missing_horse = []

for move in msg_list:
    move_parts = move.split()
    start_x, start_y, end_x, end_y = map(int, move_parts)

    if arr[end_y][end_x] != 0:
        missing_horse.append(arr[end_y][end_x])

    arr[end_y][end_x] = arr[start_y][start_x]
    arr[start_y][start_x] = 0

for y in arr:
    print(y)

ft = open("output.txt", 'w', encoding='UTF - 8')
for i in range(len(missing_horse)):
    ft.write(f'{missing_horse[i]}\n')
ft.close()