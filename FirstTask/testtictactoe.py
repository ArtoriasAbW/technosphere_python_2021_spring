import unittest
from unittest.mock import patch

from tictactoe import TicTacToe, Cell


class TestTicTacToe(unittest.TestCase):

    def test_init(self):
        field_size = 3
        game = TicTacToe(field_size)
        self.assertEqual(game.field_size, field_size)
        self.assertEqual(game.free, list(range(1, field_size * field_size + 1)))
        self.assertEqual(game.field, [Cell.EMPTY] * field_size * field_size)

    def test_turn(self):
        field_size = 3
        game = TicTacToe(field_size)

        # текущий ход у крестиков
        self.assertEqual(game.cur_turn, Cell.X)
        with patch('builtins.input', return_value=1):
            game.turn()
        # сменился ход
        self.assertEqual(game.cur_turn, Cell.O)
        # проверяем состояние поля
        self.assertEqual(game.field, [Cell.X] + [Cell.EMPTY] * (field_size * field_size - 1))
        # проверяем список свободных клеток
        self.assertEqual(game.free, list(range(2, field_size * field_size + 1)))

        with patch('builtins.input', return_value=2):
            game.turn()
        # сменился ход
        self.assertEqual(game.cur_turn, Cell.X)
        # проверяем состояние поля
        self.assertEqual(game.field, [Cell.X] + [Cell.O] + [Cell.EMPTY] * (field_size * field_size - 2))
        # проверяем список свободных клеток
        self.assertEqual(game.free, list(range(3, field_size * field_size + 1)))

        # Ставим на занятую клетку
        with patch('builtins.input', return_value=2):
            game.turn()
        # ход не сменился
        self.assertEqual(game.cur_turn, Cell.X)
        # проверяем состояние поля
        self.assertEqual(game.field, [Cell.X] + [Cell.O] + [Cell.EMPTY] * (field_size * field_size - 2))
        # проверяем список свободных клеток
        self.assertEqual(game.free, list(range(3, field_size * field_size + 1)))

        # Некорректный ввод
        with patch('builtins.input', return_value='fdsfasdfas'):
            game.turn()
        # ход не сменился
        self.assertEqual(game.cur_turn, Cell.X)
        # проверяем состояние поля
        self.assertEqual(game.field, [Cell.X] + [Cell.O] + [Cell.EMPTY] * (field_size * field_size - 2))
        # проверяем список свободных клеток
        self.assertEqual(game.free, list(range(3, field_size * field_size + 1)))

    def test_win(self):
        field_size = 3
        game = TicTacToe(field_size)
        for i in range(1, field_size + 1):
            # X turn
            with patch('builtins.input', return_value=i):
                game.turn()
            # O turn
            if i != field_size:
                with patch('builtins.input', return_value=i + 3):
                    game.turn()
        """
            x x x
            o o _
            _ _ _
        """
        self.assertEqual(game.X_win(), True)
        self.assertEqual(game.O_win(), False)
        self.assertEqual(game.end_condition(), False)

    def test_draw(self):
        field_size = 3
        game = TicTacToe(field_size)
        # x
        with patch('builtins.input', return_value=1):
            game.turn()
        # o
        with patch('builtins.input', return_value=2):
            game.turn()
        # x
        with patch('builtins.input', return_value=3):
            game.turn()
        # o
        with patch('builtins.input', return_value=5):
            game.turn()
        # x
        with patch('builtins.input', return_value=4):
            game.turn()
        # o
        with patch('builtins.input', return_value=7):
            game.turn()
        # x
        with patch('builtins.input', return_value=6):
            game.turn()
        # o
        with patch('builtins.input', return_value=9):
            game.turn()
        # x
        with patch('builtins.input', return_value=8):
            game.turn()
        """
        x o x
        x o x
        o x o
        """
        self.assertEqual(game.end_condition(), True)
        self.assertEqual(game.X_win(), False)
        self.assertEqual(game.O_win(), False)
