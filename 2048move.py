import os
import msvcrt
import random
import tkinter as tk
from decorator import append
map = [[0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0]]
def init(input):
    os.system('cls')
    for x in range(0,4,1):
        for y in range(0,4,1):
            input[x][y] = 0
    return input
def ran(input):
    zero = []
    for x in range(0, 4, 1):
        for y in range(0, 4, 1):
            if input[x][y] == 0:
                zero.append([x,y])
    i, j = random.choice(zero)
    input[i][j] = random.randint(1,2)*2
def draw(input):
    print('')
    for x in range(0,4,1):
        for y in range(0,4,1):
            if y == 3:
                split = 2 * '\n'
            else:
                split = ' ' * (5 - len(str(input[x][y])))
            if y == 0:
                space = 30 * ' '
            else:
                space = ''
                print(space,input[x][0],input[x][1],input[x][2],input[x][3],sep=split)
def write(input):
    with open('D\\2048棋谱\\2048棋谱.txt', 'w', encoding='utf-8') as f:
        f.write(draw(input))
def a1(input):
    for i in range(3):
        for x in range(0,4,1):
            for y in range(0,3,1):
                if input[x][y] == 0:
                    input[x][y] = input[x][y+1]
                    input[x][y+1] = 0
                    continue
def d1(input):
    for i in range(3):
        for x in range(0,4,1):
            for y in range(1,4,1):
                if input[x][y] == 0:
                    input[x][y] = input[x][y-1]
                    input[x][y-1] = 0
                    continue
def w1(input):
    for i in range(3):
        for x in range(0,3,1):
            for y in range(0,4,1):
                if input[x][y] == 0:
                    input[x][y] = input[x+1][y]
                    input[x+1][y] = 0
                    continue
def s1(input):
    for i in range(3):
        for x in range(1,4,1):
            for y in range(0,4,1):
                if input[x][y] == 0:
                    input[x][y] = input[x-1][y]
                    input[x-1][y] = 0
                    continue
def a(input):
    os.system('cls')
    a1(input)
    for j in range(0,4,1):
        for x in range(0,4,1):
            for y in range(j,j+2,1):
                if input[x][y] == 0:
                    a1(input)
                if input[x][y] != 0:
                    if input[x][y + 1] == input[x][y]:
                        input[x][y] = 2 * input[x][y + 1]
                        input[x][y + 1] = 0
                        a1(input)
        continue
    return input
def d(input):
    os.system('cls')
    d1(input)
    for j in (3,0,-1):
        for x in range(0,4,1):
            for y in range(j,0,-1):
                if input[x][y] == 0:
                    d1(input)
                if input[x][y] != 0:
                    if input[x][y-1] == input[x][y]:
                        input[x][y] = 2 * input[x][y-1]
                        input[x][y-1] = 0
                        d1(input)
        continue
    return input
def w(input):
    os.system('cls')
    w1(input)
    for j in range(0,2,1):
        for y in range(0, 4, 1):
            for x in range(j,j+2,1):
                if input[x][y] == 0:
                    w1(input)
                if input[x][y] != 0:
                    if input[x][y] == input[x+1][y] and x < 3:
                        input[x][y] = 2 * input[x+1][y]
                        input[x+1][y] = 0
                        w1(input)
        continue
    return input
def s(input):
    os.system('cls')
    d1(input)
    for j in (3, 0, -1):
        for y in range(0, 4, 1):
            for x in range(j, 0, -1):
                if input[x][y] == 0:
                    s1(input)
                if input[x][y] != 0:
                    if input[x-1][y] == input[x][y]:
                        input[x][y] = 2 * input[x-1][y]
                        input[x-1][y] = 0
                        s1(input)
        continue
    return input

def keyboard():
    while True:
        key = msvcrt.getch()
        if key in [b'w',b's',b'a',b'd']:
            return key

def use_keyboard(key,input):
    backup = [[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]]
    for x in range(4):
        for y in range(4):
            backup[x][y] = input[x][y]
    if key == b'a':
        input = a(input)
    elif key == b'd':
        input = d(input)
    elif key == b'w':
        input = w(input)
    elif key == b's':
        input = s(input)
    this_key_work_or_not = False
    for y in range(4):
        for x in range(4):
            if backup[y][x] != input[y][x]:
                this_key_work_or_not = True
    return input,this_key_work_or_not

def check_neighbour_element(map, pos):#(x,y)
    x, y = pos
    if y > 0:
        if map[y][x] == map[y-1][x]:
            return True
    if y < 3:
        if map[y][x] == map[y+1][x]:
            return True
    if x > 0:
        if map[y][x] == map[y][x-1]:
            return True
    if x < 3:
        if map[y][x] == map[y][x+1]:
            return True
    return False

def win_lose(input):
    for y in range(4):
        for x in range(4):
            if input[y][x] == 2048:
                return 1
            elif input[y][x] == 0:
                return -1
            elif check_neighbour_element(input, (x, y)):
                return -1
    return 0




map = init(map)
ran(map)
draw(map)
while True:
    key = keyboard()
    map,this_key_work_or_not = use_keyboard(key,map)
    res = win_lose(map)
    if res == True:
        print('win')
        break
    elif res == False:
        print('lose')
        break
    elif res == -1 and this_key_work_or_not == True:
        map = ran(map)
        draw(map)
        continue
    elif res == -1 and this_key_work_or_not == False:
        continue