import random

# 初始化游戏棋盘，创建一个4x4的全零二维列表
def init_board():
    return [[0] * 4 for _ in range(4)]

# 在棋盘的空白位置随机生成一个数字（2或者4）
def add_random_tile(board):
    empty = []
    for x in range(4):
        for y in range(4):
            if board[x][y] == 0:
                empty.append((x, y))
    if empty:
        x, y = random.choice(empty)
        value = 2 if random.random() < 0.9 else 4
        board[x][y] = value
    return board


# 打印游戏棋盘的可视化界面
def print_board(board):
    for x in board:
        print(" ".join(map(str, x)))


# 判断游戏是否结束（棋盘已满且无法移动）
def is_game_over(board):
    return all(all(cell!= 0 for cell in row) for row in board) and not can_move(board)


# 判断是否可以移动（上下左右四个方向中至少有一个方向可以移动）
def can_move(board):
    return can_move_left(board) or can_move_right(board) or can_move_up(board) or can_move_down(board)


# 判断向左是否可以移动
def can_move_left(board):
    for row in board:
        non_zero_cells = [cell for cell in row if cell!= 0]
        for i in range(len(non_zero_cells) - 1):
            if non_zero_cells[i] == non_zero_cells[i + 1]:
                return True
    return False


# 判断向右是否可以移动
def can_move_right(board):
    for row in board:
        non_zero_cells = [cell for cell in reversed(row) if cell!= 0]
        for i in range(len(non_zero_cells) - 1):
            if non_zero_cells[i] == non_zero_cells[i + 1]:
                return True
    return False


# 判断向上是否可以移动
def can_move_up(board):
    transposed_board = list(map(list, zip(*board)))
    return can_move_left(transposed_board)


# 判断向下是否可以移动
def can_move_down(board):
    transposed_board = list(map(list, zip(*board)))
    return can_move_right(transposed_board)


# 向左移动操作
def move_left(board):
    new_board = [row.copy() for row in board]
    for row_index in range(4):
        non_zero_cells = [cell for cell in new_board[row_index] if cell!= 0]
        merged = []
        i = 0
        while i < len(non_zero_cells):
            if i < len(non_zero_cells) - 1 and non_zero_cells[i] == non_zero_cells[i + 1]:
                merged.append(non_zero_cells[i] * 2)
                i += 2
            else:
                merged.append(non_zero_cells[i])
                i += 1
        new_board[row_index][:len(merged)] = merged
        new_board[row_index][len(merged):] = [0] * (4 - len(merged))
    return new_board


# 向右移动操作
def move_right(board):
    new_board = [list(reversed(row)) for row in board]
    new_board = move_left(new_board)
    return [list(reversed(row)) for row in new_board]


# 向上移动操作
def move_up(board):
    transposed_board = list(map(list, zip(*board)))
    new_board = move_left(transposed_board)
    return list(map(list, zip(*new_board)))


# 向下移动操作
def move_down(board):
    transposed_board = list(map(list, zip(*board)))
    new_board = move_right(transposed_board)
    return list(map(list, zip(*new_board)))


# 游戏主循环
def play_game():
    board = init_board()
    add_random_tile(board)
    add_random_tile(board)
    while not is_game_over(board):
        print_board(board)
        move = input("请输入移动方向（w上，s下，a左，d右）：").lower()
        if move == "a":
            new_board = move_left(board)
        elif move == "d":
            new_board = move_right(board)
        elif move == "w":
            new_board = move_up(board)
        elif move == "s":
            new_board = move_down(board)
        else:
            print("无效的输入，请重新输入！")
            continue
        if new_board!= board:
            board = new_board
            add_random_tile(board)
    print("游戏结束！")


if __name__ == "__main__":
    play_game()