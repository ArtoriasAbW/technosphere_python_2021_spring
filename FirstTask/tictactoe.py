class TicTacToe:

    def __init__(self):
        self.cur_turn = 1  # 1 if X, 2 if O
        self.field = list()
        for _ in range(9):
            self.field.append(0)
        self.free = list(range(1, 10))  # free positions

    def turn(self):
        try:
            pos = int(input())
        except ValueError:
            print("Invalid input")
            return
        if pos not in self.free:
            print("Invalid position")
            return
        self.free.remove(pos)
        if self.cur_turn == 1:
            self.field[pos - 1] = 1
            self.cur_turn = 2
        else:
            self.field[pos - 1] = 2
            self.cur_turn = 1

    def draw(self):
        for i in range(3):
            for j in range(3):
                if self.field[3*i+j] == 0:
                    print("{}".format(3 * i + j + 1), end="")
                elif self.field[3*i+j] == 1:
                    print("X", end="")
                else:
                    print("O", end="")
                if (j != 2):
                    print("|", end="")
            print("\n-----")

    def win(self, player):
        if self.field[0] == self.field[1] == self.field[2] == player:
            return True
        if self.field[3] == self.field[4] == self.field[5] == player:
            return True
        if self.field[6] == self.field[7] == self.field[8] == player:
            return True
        if self.field[0] == self.field[4] == self.field[8] == player:
            return True
        if self.field[2] == self.field[4] == self.field[6] == player:
            return True
        if self.field[0] == self.field[3] == self.field[6] == player:
            return True
        if self.field[1] == self.field[4] == self.field[7] == player:
            return True
        if self.field[2] == self.field[5] == self.field[8] == player:
            return True
        return False

    def X_win(self):
        return self.win(1)

    def O_win(self):
        return self.win(2)

    def end_condition(self):
        if len(self.free) == 0:
            return True
        return False

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
    game = TicTacToe()
    game.play()
