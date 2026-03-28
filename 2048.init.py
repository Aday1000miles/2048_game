import random
map = [[0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0]]
def init(input):
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    num = random.randint(1, 2)*2
    input[x][y] = num
    return input

map = init(map)
show_map(map)

init(map)
print(next)
def move_and_merge(list_input):
    col = 0
    next = 0
    while col < 4:
        next = col + 1
        while next < 4 and list_input[next] == 0:
            next += 1
        if next > 3:
            break
        if list_input[col] == 0:
            list_input[col] == list_input[next]
            list_input[next] = 0
            updated = True
            continue
        elif list_input[col] == list_input[next]:
            list_input[col] *= 2
            list_input[next] = 0
            updated = True
        col += 1
    return list_input

            if input[x][1] == 0:
                input[x][1] = input[x][2]
                input[x][2] = 0
            if input[x][2] == 0:
                input[x][2] = input[x][3]
                input[x][3] = 0
            if input[x][3] == 0:
                continue
    return True