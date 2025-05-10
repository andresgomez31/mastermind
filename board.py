import random as rd

def_colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"]
def_hints = ["#000000", "#FFFFFF"]

class board_row:
    def __init__(self, row: int, total_spaces: int):
        self.row = row
        self.guess = [None] * total_spaces
        self.feedback = [None] * total_spaces

    def compare_guess(self, key: list[str], hint_colors: list[str]):
        if any(g is None for g in self.guess):
            raise ValueError("Guess is incomplete")

        print(f"DEBUG: Starting comparison for row {self.row}")
        print(f"DEBUG: Initial guess: {self.guess}")
        print(f"DEBUG: Key: {key}")

        self.feedback = []
        key_temp = key.copy()
        guess_temp = self.guess.copy()

        # Negras (posición y color correcto)
        for i in range(len(guess_temp)):
            if guess_temp[i] == key_temp[i]:
                self.feedback.append(hint_colors[0])
                print(f"DEBUG: Exact match at position {i}, color: {guess_temp[i]}")
                key_temp[i] = guess_temp[i] = None

        # Blancas (color correcto, posición incorrecta)
        for i in range(len(guess_temp)):
            if guess_temp[i] and guess_temp[i] in key_temp:
                self.feedback.append(hint_colors[1])
                print(f"DEBUG: Color match (wrong position) at position {i}, color: {guess_temp[i]}")
                key_temp[key_temp.index(guess_temp[i])] = None

        while len(self.feedback) < len(self.guess):
            self.feedback.append(None)

        print(f"DEBUG: Feedback for row {self.row}: {self.feedback}")
        

    def __str__(self):
        return f"Row {self.row}: Guess: {self.guess}, Feedback: {self.feedback}"


class Board:
    def __init__(self, colors=def_colors, hints=def_hints, total_rows=10, total_spaces=4):
        self.colors = colors
        self.hints = hints
        self.total_rows = total_rows
        self.total_spaces = total_spaces
        self.key = [rd.choice(colors) for _ in range(total_spaces)]
        self.active_row = 0
        self.rows = [board_row(i, total_spaces) for i in range(total_rows)]

    def set_color_on_row(self, row: int, col: int, color: str):
        if row != self.active_row:
            raise ValueError("Only the active row can be modified")
        if not (0 <= col < self.total_spaces):
            raise ValueError("Invalid column index")
        if color not in self.colors:
            raise ValueError("Invalid color")
        self.rows[row].guess[col] = color

    def set_guess_on_row(self, row_idx, colors):
        self.rows[row_idx].guess = colors
        hints = self.get_hints()

    def is_guess_complete(self):
        return None not in self.rows[self.active_row].guess

    def get_hints(self):
        if not self.is_guess_complete():
            raise ValueError("Guess is incomplete")
        current_row = self.rows[self.active_row]
        current_row.compare_guess(self.key, self.hints)
        self.active_row += 1
        return current_row.feedback

    def is_game_over(self):
        return self.active_row >= self.total_rows

    def __str__(self):
        return "\n".join(str(row) for row in self.rows)
