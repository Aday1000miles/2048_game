import tkinter as tk
import random

class Game2048:
    def __init__(self, master):#初始化
        self.master = master
        self.master.title("2048 Game")#题目
        self.grid = [[0] * 4 for _ in range(4)]#
        self.score = 0
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='lightgray')
        self.canvas.pack()
        self.score_label = tk.Label(self.master, text="Score: 0", font=('Helvetica', 24))
        self.score_label.pack()
        self.master.bind("<Key>", self.key_event)

    def start_game(self):
        self.reset_grid()
        self.add_new_tile()
        self.add_new_tile()
        self.update_canvas()

    def reset_grid(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.score_label.config(text="Score: 0")

    def add_new_tile(self):
        empty_tiles = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.grid[i][j] = random.choice([2, 4])

    def update_canvas(self):
        self.canvas.delete("all")
        for i in range(4):
            for j in range(4):
                value = self.grid[i][j]
                x0, y0, x1, y1 = j * 100, i * 100, j * 100 + 100, i * 100 + 100
                if value > 0:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.get_color(value))
                    self.canvas.create_text(x0 + 50, y0 + 50, text=str(value), font=('Helvetica', 32))
        self.score_label.config(text="Score: " + str(self.score))

    def get_color(self, value):
        colors = {
            0: "lightgray",
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f67c5f",
            128: "#f9f8f0",
            256: "#f9f8f0",
            512: "#f9f8f0",
            1024: "#f9f8f0",
            2048: "#f9f8f0"
        }
        return colors.get(value, "#3c3a32")

    def key_event(self, event):
        if event.keysym in ('Up', 'Down', 'Left', 'Right'):
            moved = False
            if event.keysym == 'Up':
                moved = self.move_up()
            elif event.keysym == 'Down':
                moved = self.move_down()
            elif event.keysym == 'Left':
                moved = self.move_left()
            elif event.keysym == 'Right':
                moved = self.move_right()
            if moved:
                self.add_new_tile()
                self.update_canvas()
            if not self.can_move():
                self.canvas.create_text(200, 200, text="Game Over", font=('Helvetica', 48), fill='red')

    def move_up(self):
        moved = False
        for j in range(4):
            temp = [self.grid[i][j] for i in range(4) if self.grid[i][j]!= 0]
            new_row = []
            i = 0
            while i < len(temp):
                if i + 1 < len(temp) and temp[i] == temp[i + 1]:
                    new_row.append(temp[i] * 2)
                    self.score += temp[i] * 2
                    i += 1
                else:
                    new_row.append(temp[i])
                i += 1
            new_row += [0] * (4 - len(new_row))
            for i in range(4):
                if self.grid[i][j]!= new_row[i]:
                    moved = True
                    self.grid[i][j] = new_row[i]
        return moved

    def move_down(self):
        moved = False
        for j in range(4):
            temp = [self.grid[i][j] for i in range(3, -1, -1) if self.grid[i][j]!= 0]
            new_row = []
            i = 0
            while i < len(temp):
                if i + 1 < len(temp) and temp[i] == temp[i + 1]:
                    new_row.append(temp[i] * 2)
                    self.score += temp[i] * 2
                    i += 1
                else:
                    new_row.append(temp[i])
                i += 1
            new_row = [0] * (4 - len(new_row)) + new_row[::-1]
            for i in range(4):
                if self.grid[i][j]!= new_row[3 - i]:
                    moved = True
                    self.grid[i][j] = new_row[3 - i]
        return moved

    def move_left(self):
        moved = False
        for i in range(4):
            temp = [self.grid[i][j] for j in range(4) if self.grid[i][j]!= 0]
            new_row = []
            j = 0
            while j < len(temp):
                if j + 1 < len(temp) and temp[j] == temp[j + 1]:
                    new_row.append(temp[j] * 2)
                    self.score += temp[j] * 2
                    j += 1
                else:
                    new_row.append(temp[j])
                j += 1
            new_row += [0] * (4 - len(new_row))
            for j in range(4):
                if self.grid[i][j]!= new_row[j]:
                    moved = True
                    self.grid[i][j] = new_row[j]
        return moved

    def move_right(self):
        moved = False
        for i in range(4):
            temp = [self.grid[i][j] for j in range(3, -1, -1) if self.grid[i][j]!= 0]
            new_row = []
            j = 0
            while j < len(temp):
                if j + 1 < len(temp) and temp[j] == temp[j + 1]:
                    new_row.append(temp[j] * 2)
                    self.score += temp[j] * 2
                    j += 1
                else:
                    new_row.append(temp[j])
                j += 1
            new_row = [0] * (4 - len(new_row)) + new_row[::-1]
            for j in range(4):
                if self.grid[i][j]!= new_row[3 - j]:
                    moved = True
                    self.grid[i][j] = new_row[3 - j]
        return moved

    def can_move(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == self.grid[i + 1][j] or self.grid[i][j] == self.grid[i][j + 1]:
                    return True
        for j in range(3):
            if self.grid[3][j] == self.grid[3][j + 1]:
                return True
        for i in range(3):
            if self.grid[i][3] == self.grid[i + 1][3]:
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()