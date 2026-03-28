import os
import msvcrt
import random

map = [[0, 0, 0, 0], \
       [0, 0, 0, 0], \
       [0, 0, 0, 0], \
       [0, 0, 0, 0]]

empty = []


def get_keyboard():  # 获取键盘函数
    while True:
        key = msvcrt.getch()
        if key in [b'w', b's', b'a', b'd']:
            break
    return key


def lenth_of_each_num(input):  # 获取数字位数函数
    lenth = [[0, 0, 0, 0], \
             [0, 0, 0, 0], \
             [0, 0, 0, 0], \
             [0, 0, 0, 0]]
    for y in range(4):
        for x in range(4):
            lenth[y][x] = len(str(input[y][x]))
    return lenth


def show_map(input):  # 展示地图函数
    # os.system('cls')
    lenth = lenth_of_each_num(input)
    space = [[" ", " ", " ", " "], \
             [" ", " ", " ", " "], \
             [" ", " ", " ", " "], \
             [" ", " ", " ", " "]]
    for y in range(4):  # 遍历
        for x in range(4):
            for i in range(5 - lenth[y][x]):
                space[y][x] = space[y][x] + " "

    for y in range(4):
        print(' ' * 50,
              space[y][0] + str(input[y][0]) + space[y][1] + str(input[y][1]) + space[y][2] + str(input[y][2]) +
              space[y][3] + str(input[y][3]), '\n')


def init(input):  # 初始化函数
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    num = random.randint(1, 2) * 2
    input[x][y] = num
    return input


def add_num(input):
    for y in range(0, 3, 1):
        if input[x][y] != 0:
            break
        for x in range(0, 3, 1):
            if input[x][y] == 0:
                empty.append([x, y])
                num = random.randint(1, 2) * 2
                input[x][y] = num
                print('iiiiii')
                break
            elif [x, y] not in empty:
                continue
        break

    return input


def win_or_lose(input):
    a = 0
    for y in range(4):
        for x in range(4):
            if input[x][y] == 2048:
                print('you win')
                break
    for y in range(4):
        for x in range(3):
            if input[x][y] != 0:
                a = a + 1
                if a == 16:
                    print('you lose')
                    break
    return True


# 主函数

map = init(map)

add_num(map)
show_map(map)