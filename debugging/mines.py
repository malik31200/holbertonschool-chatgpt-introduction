#!/usr/bin/python3
import random
import os

CLEAR_SCREEN = True  # Set to False if your terminal doesn't like clearing

def clear_screen():
    if CLEAR_SCREEN:
        os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines >= width * height:
            raise ValueError("Mines must be fewer than total cells.")
        self.width = width
        self.height = height
        self.mines_count = mines
        self.mines = set()  # indices (y * width + x); placed after first move
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.first_move_done = False

    def pos_to_idx(self, x, y):
        return y * self.width + x

    def place_mines(self, forbidden_idx=None):
        """Place mines while avoiding the forbidden cell (first click)."""
        cells = list(range(self.width * self.height))
        if forbidden_idx is not None and forbidden_idx in cells:
            cells.remove(forbidden_idx)
        self.mines = set(random.sample(cells, self.mines_count))

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f'{i:2d}' for i in range(self.width)))
        print('   ' + '-' * (3 * self.width - 1))
        for y in range(self.height):
            row = [f'{y:2d}|']
            for x in range(self.width):
                idx = self.pos_to_idx(x, y)
                if reveal or self.revealed[y][x]:
                    if idx in self.mines:
                        ch = '*'
                    else:
                        c = self.count_mines_nearby(x, y)
                        ch = str(c) if c > 0 else ' '
                else:
                    ch = '.'
                row.append(f' {ch}')
            print(' '.join(row))

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue  # don't count the center cell
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.pos_to_idx(nx, ny) in self.mines:
                        count += 1
        return count

    def flood_reveal(self, x, y):
        """Iterative flood fill to reveal contiguous zero-neighbor cells."""
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if self.revealed[cy][cx]:
                continue
            self.revealed[cy][cx] = True
            if self.count_mines_nearby(cx, cy) == 0:
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            if not self.revealed[ny][nx] and self.pos_to_idx(nx, ny) not in self.mines:
                                stack.append((nx, ny))

    def reveal(self, x, y):
        """Return False if a mine was hit, True otherwise."""
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # ignore out-of-bounds
        if self.revealed[y][x]:
            return True  # already revealed

        if not self.first_move_done:
            # Ensure first move is always safe
            self.place_mines(forbidden_idx=self.pos_to_idx(x, y))
            self.first_move_done = True

        if self.pos_to_idx(x, y) in self.mines:
            self.revealed[y][x] = True
            return False

        self.flood_reveal(x, y)
        return True

    def has_won(self):
        total = self.width * self.height
        revealed = sum(sum(1 for c in row if c) for row in self.revealed)
        return revealed == total - self.mines_count

    def reset(self):
        self.mines = set()
        self.revealed = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.first_move_done = False

    def play(self):
        self.reset()
        while True:
            self.print_board()
            try:
                raw = input("Enter 'x y' (or 'q' to quit): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nBye!")
                break
            if raw in ('q', 'quit', 'exit'):
                print("Bye!")
                break

            parts = raw.replace(',', ' ').split()
            if len(parts) != 2:
                print("Invalid input. Use: x y")
                continue
            try:
                x, y = int(parts[0]), int(parts[1])
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
            if not (0 <= x < self.width and 0 <= y < self.height):
                print(f"Out of bounds. x in [0,{self.width-1}], y in [0,{self.height-1}].")
                continue

            safe = self.reveal(x, y)
            if not safe:
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

            if self.has_won():
                self.print_board(reveal=True)
                print("You win! Well played.")
                break

if __name__ == "__main__":
    game = Minesweeper(width=10, height=10, mines=10)
    game.play()
