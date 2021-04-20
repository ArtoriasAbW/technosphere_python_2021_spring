from enum import Enum


class Cell(Enum):
    EMPTY = 0
    X = 1
    O = 2


class TicTacToe:

    def __init__(self, field_size):
        self.cur_turn = Cell.X
        self.field = list()
        self.field_size = field_size
        for _ in range(field_size * field_size):
            self.field.append(Cell.EMPTY)
        # free positions
        self.free = list(range(1, field_size * field_size + 1))

    def turn(self):
        if (self.cur_turn == Cell.X):
            print("X turn: ", end="")
        else:
            print("O turn: ", end="")
        try:
            pos = int(input())
            print()
        except ValueError:
            print("Invalid input")
            return
        if pos not in self.free:
            print("Invalid position")
            return
        self.free.remove(pos)
        if self.cur_turn == Cell.X:
            self.field[pos - 1] = Cell.X
            self.cur_turn = Cell.O
        else:
            self.field[pos - 1] = Cell.O
            self.cur_turn = Cell.X

    def draw(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.field[self.field_size*i+j] == Cell.EMPTY:
                    print("{:>2}".format(self.field_size * i + j + 1), end="")
                elif self.field[self.field_size*i+j] == Cell.X:
                    print("{:>2}".format("X"), end="")
                else:
                    print("{:>2}".format("O"), end="")
                if (j != self.field_size - 1):
                    print("|", end="")
            if (i != self.field_size - 1):
                print("\n" + "---" * self.field_size)
            else:
                print("\n")

    def win(self, player):
        # победа по горизонтали и вертикали
        for i in range(self.field_size):
            hor_win = True
            vert_win = True
            for j in range(self.field_size):
                if not hor_win and not vert_win:
                    break
                if self.field[self.field_size * i + j] != player:
                    hor_win = False
                if self.field[self.field_size * j + i] != player:
                    vert_win = False
            if hor_win or vert_win:
                return True
        # победа наискосок
        lr_win = True
        rl_win = True
        for i in range(self.field_size):
            if not lr_win and not rl_win:
                return False
            if self.field[self.field_size * i + i] != player:
                lr_win = False
            if self.field[(self.field_size - 1) + self.field_size * i - i] != player:
                rl_win = False
        return lr_win or rl_win

    def X_win(self):
        return self.win(Cell.X)

    def O_win(self):
        return self.win(Cell.O)

    def end_condition(self):
        return len(self.free) == 0

    def play(self):
        end = False
        end_string = "Draw..."
        while not end:
            self.draw()
            self.turn()
            if self.X_win():
                end_string = "First player win!"
                end = True
            elif self.O_win():
                end_string = "Second player win!"
                end = True
            elif self.end_condition():
                end = True
        self.draw()
        print(end_string)


if __name__ == "__main__":
    game = TicTacToe(3)
    game.play()
