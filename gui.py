import tkinter as tk
from tkinter import ttk
from board import Board

# Configuracion
WIDTH, HEIGHT = 500, 700
ROWS, COLS = 10, 4
COLOR_OPTIONS_HEX = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"]
HINTS_OPTIONS_HEX = ["#000000", "#FFFFFF"]
RADIUS = 20
HINT_RADIUS = RADIUS // 2
ROW_SPACING = 50
COLOR_BTN_SIZE = 30

class MastermindGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#F0F0F0")
        self.canvas.pack()

        self.colors = COLOR_OPTIONS_HEX
        self.hints = HINTS_OPTIONS_HEX
        self.active_color = None
        self.guesses = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.board = Board(colors=self.colors, hints=self.hints, total_rows=ROWS, total_spaces=COLS)
        self.active_row = self.board.active_row

        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_ui()

    def draw_ui(self):
        self.canvas.delete("all")

        y_offset = 50
        for i in range(ROWS):
            y = y_offset + i * ROW_SPACING
            # Circulos de colores
            for j in range(COLS):
                x = 50 + j * (2 * RADIUS + 10)
                color = self.guesses[i][j] or "#CCCCCC"
                self.canvas.create_oval(x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS, fill=color, outline="black")

            # Circulos de pistas (2x2)
            for k in range(2):
                for l in range(2):
                    hx = 300 + l * (HINT_RADIUS * 2 + 4)
                    hy = y - HINT_RADIUS + k * (HINT_RADIUS * 2 + 4)
                    hint_color = self.board.rows[i].feedback[k * 2 + l] if i < self.active_row else "#CCCCCC"
                    self.canvas.create_oval(hx-HINT_RADIUS, hy-HINT_RADIUS, hx+HINT_RADIUS, hy+HINT_RADIUS, fill=hint_color, outline="black")

        # Boton de verificacion
        self.check_btn = ttk.Button(self.root, text="Check", command=self.check_guess)
        self.canvas.create_window(400, y_offset + self.active_row * ROW_SPACING, window=self.check_btn)

        # Paleta de colores
        color_y = HEIGHT - 60
        for idx, color in enumerate(self.colors):
            cx = 50 + idx * (COLOR_BTN_SIZE + 10)
            tag = f"color_btn_{idx}"
            self.canvas.create_oval(cx-COLOR_BTN_SIZE//2, color_y-COLOR_BTN_SIZE//2, cx+COLOR_BTN_SIZE//2, color_y+COLOR_BTN_SIZE//2, fill=color, outline="black", tags=tag)
            if self.active_color == idx:
                self.canvas.create_oval(cx-COLOR_BTN_SIZE//2-3, color_y-COLOR_BTN_SIZE//2-3, cx+COLOR_BTN_SIZE//2+3, color_y+COLOR_BTN_SIZE//2+3, outline="black", width=2)
        
        if all(hint == "#000000" for hint in self.board.rows[abs(self.active_row - 1)].feedback):
            self.end_game()

    def on_click(self, event):
        # Seleccion de color
        color_y = HEIGHT - 60
        for idx, color in enumerate(self.colors):
            cx = 50 + idx * (COLOR_BTN_SIZE + 10)
            if (event.x - cx) ** 2 + (event.y - color_y) ** 2 <= (COLOR_BTN_SIZE // 2) ** 2:
                self.active_color = idx
                self.draw_ui()
                return

        # Colocacion de color en la fila activa
        y = 50 + self.active_row * ROW_SPACING
        for j in range(COLS):
            x = 50 + j * (2 * RADIUS + 10)
            if (event.x - x) ** 2 + (event.y - y) ** 2 <= RADIUS ** 2 and self.active_color is not None:
                self.guesses[self.active_row][j] = self.colors[self.active_color]
                self.draw_ui()
                return

    def check_guess(self):
        if all(self.guesses[self.active_row]):
            self.board.set_guess_on_row(self.active_row, self.guesses[self.active_row])
            self.active_row = self.board.active_row
            print(f"Checking guess: {self.guesses[self.active_row]}", f"Key: {self.board.key}", f"Feedback: {self.board.rows[self.active_row].feedback}")
            self.draw_ui()

    def end_game(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MastermindGUI(root)
    root.mainloop()
