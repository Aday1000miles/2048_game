import os
import msvcrt
import random
import platform
import time
import tkinter as tk


# 将变量名map改为board，避免与内置函数map冲突
board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]


def init(input_board):
    """
    初始化棋盘，将棋盘上的所有元素设置为0，并清屏（考虑跨平台清屏）
    """
    clear_screen()
    for x in range(4):
        for y in range(4):
            input_board[x][y] = 0
    return input_board


def ran(input_board):
    """
    在棋盘的空白位置随机生成数字（2或者4）
    """
    zero_positions = []
    for x in range(4):
        for y in range(4):
            if input_board[x][y] == 0:
                zero_positions.append([x, y])
    if zero_positions:
        i, j = random.choice(zero_positions)
        input_board[i][j] = random.randint(1, 2) * 2
    return input_board


def draw(input_board):
    """
    绘制棋盘界面，返回棋盘状态的字符串表示（方便后续写入文件等操作）
    """
    board_str = ""
    for x in range(4):
        for y in range(4):
            element_str = str(input_board[x][y])
            padding = " " * (5 - len(element_str))
            if y == 0:
                board_str += 30 * " "
            board_str += element_str + padding
            if y == 3:
                board_str += "\n"
        else:
            board_str += "\n"
    return board_str


def write(input_board):
    """
    将棋盘状态写入文件，调用draw函数获取字符串内容后写入
    """
    with open('D:\\2048棋谱\\2048棋谱.txt', 'w', encoding='utf-8') as f:
        f.write(draw(input_board))


def a1(input_board):
    """
    向左移动棋盘元素，处理空白格的移动（基础移动函数）
    """
    for i in range(3):
        for x in range(4):
            for y in range(3):
                if input_board[x][y] == 0:
                    input_board[x][y] = input_board[x][y + 1]
                    input_board[x][y + 1] = 0
    return input_board


def d1(input_board):
    """
    向右移动棋盘元素，处理空白格的移动（基础移动函数）
    """
    for i in range(3):
        for x in range(4):
            for y in range(3, 0, -1):
                if input_board[x][y] == 0:
                    input_board[x][y] = input_board[x][y - 1]
                    input_board[x][y - 1] = 0
    return input_board


def w1(input_board):
    """
    向上移动棋盘元素，处理空白格的移动（基础移动函数）
    """
    for i in range(3):
        for x in range(3):
            for y in range(4):
                if input_board[x][y] == 0:
                    input_board[x][y] = input_board[x + 1][y]
                    input_board[x + 1][y] = 0
    return input_board


def s1(input_board):
    """
    向下移动棋盘元素，处理空白格的移动（基础移动函数）
    """
    for i in range(3):
        for x in range(3, 0, -1):
            for y in range(4):
                if input_board[x][y] == 0:
                    input_board[x][y] = input_board[x - 1][y]
                    input_board[x - 1][y] = 0
    return input_board


def a(input_board):
    """
    处理向左移动及合并操作
    """
    clear_screen()
    input_board = a1(input_board)
    for x in range(4):
        for y in range(3):
            if input_board[x][y]!= 0 and input_board[x][y] == input_board[x][y + 1]:
                input_board[x][y] *= 2
                input_board[x][y + 1] = 0
    input_board = a1(input_board)
    return input_board


def d(input_board):
    """
    处理向右移动及合并操作
    """
    clear_screen()
    input_board = d1(input_board)
    for x in range(4):
        for y in range(3, 0, -1):
            if input_board[x][y]!= 0 and input_board[x][y] == input_board[x][y - 1]:
                input_board[x][y] *= 2
                input_board[x][y - 1] = 0
    input_board = d1(input_board)
    return input_board


def w(input_board):
    """
    处理向上移动及合并操作
    """
    clear_screen()
    input_board = w1(input_board)
    for y in range(4):
        for x in range(3):
            if input_board[x][y]!= 0 and input_board[x][y] == input_board[x + 1][y]:
                input_board[x][y] *= 2
                input_board[x + 1][y] = 0
    input_board = w1(input_board)
    return input_board


def s(input_board):
    """
    处理向下移动及合并操作
    """
    clear_screen()
    input_board = s1(input_board)
    for y in range(4):
        for x in range(3, 0, -1):
            if input_board[x][y]!= 0 and input_board[x][y] == input_board[x - 1][y]:
                input_board[x][y] *= 2
                input_board[x - 1][y] = 0
    input_board = s1(input_board)
    return input_board


def keyboard():
    """
    获取键盘输入，等待直到获取到代表上下左右方向键的字符
    """
    while True:
        key = msvcrt.getch()
        if key in [b'w', b's', b'a', b'd']:
            return key


def use_keyboard(input_board):

    is_key_work = False
    backup_board = [row.copy() for row in input_board]
    for x in range(4):
        for y in range(4):
            if backup_board[x][y]!= input_board[x][y]:
                is_key_work = True

    while True:
        input_board = a(input_board)
        input_board = w(input_board)
        if is_key_work == False:
            time.sleep(0.2)
            input_board = d(input_board)
            input_board = s(input_board)
            if is_key_work == False:
                time.sleep(0.2)
                input_board = a(input_board)
                input_board = w(input_board)

    return input_board, is_key_work


def check_neighbour_element(board, pos):
    """
    检查给定位置的元素是否有相邻相同元素
    """
    x, y = pos
    if y > 0 and board[y][x] == board[y - 1][x]:
        return True
    if y < 3 and board[y][x] == board[y + 1][x]:
        return True
    if x > 0 and board[y][x] == board[y][x - 1]:
        return True
    if x < 3 and board[y][x] == board[y][x + 1]:
        return True
    return False


def win_lose(input_board):
    """
    判断游戏的胜负状态
    """
    for y in range(4):
        for x in range(4):
            if input_board[y][x] == 2048:
                return 1
            elif input_board[y][x] == 0:
                return -1
            elif check_neighbour_element(input_board, (x, y)):
                return -1
    return 0


def clear_screen():
    """
    跨平台清屏函数，根据不同操作系统执行相应清屏命令
    """
    system_name = platform.system()
    if system_name == "Windows":
        os.system('cls')
    elif system_name in ["Linux", "Darwin"]:
        os.system('clear')


board = init(board)
board = ran(board)
print(draw(board))
while True:
    board, key_worked = use_keyboard(board)
    result = win_lose(board)
    if result == 1:
        print('win')
        break
    elif result == 0:
        print('lose')
        break
    elif result == -1 and key_worked:
        board = ran(board)
        print(draw(board))
        continue
    elif result == -1 and key_worked == False:
        print(draw(board))
        continue
