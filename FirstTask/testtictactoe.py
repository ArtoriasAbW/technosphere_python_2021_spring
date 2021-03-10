import tictactoe

import pytest


# TODO: create tests
class TestClass(object):

    def test_initialization(self):
        game = tictactoe.TicTacToe()
        assert game.field == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        assert game.free == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert game.cur_turn == 1

    def test_win(self):
        game = tictactoe.TicTacToe()
        game.field = [1, 1, 1,
                      0, 0, 0,
                      0, 0, 0]
        assert game.X_win()
        assert not game.O_win()
        assert not game.end_condition()
        game.field = [1, 0, 0,
                      0, 1, 0,
                      0, 0, 1]
        assert game.X_win()
        assert not game.O_win()
        assert not game.end_condition()
        game.field = [1, 1, 2,
                      2, 1, 1,
                      1, 2, 2]
        assert not game.X_win()
        assert not game.O_win()
        assert game.end_condition()
        game.field = [2, 0, 0,
                      2, 0, 1,
                      2, 1, 1]
        assert not game.X_win()
        assert game.O_win()
        assert not game.end_condition()

    def test_turn(self):
        game = tictactoe.TicTacToe()
        assert game.cur_turn == 1
        tictactoe.input = lambda : 1
        game.turn()
        assert game.cur_turn == 2
        assert game.field == [1, 0, 0, 0, 0, 0, 0, 0, 0]
        assert game.free == [2, 3, 4, 5, 6, 7, 8, 9]
        tictactoe.input = lambda : 4
        game.turn()
        assert game.cur_turn == 1
        assert game.field == [1, 0, 0, 2, 0, 0, 0, 0, 0]
        assert game.free == [2, 3, 5, 6, 7, 8, 9]
        tictactoe.input = lambda : 4
        game.turn()
        assert game.cur_turn == 1
        assert game.field == [1, 0, 0, 2, 0, 0, 0, 0, 0]
        assert game.free == [2, 3, 5, 6, 7, 8, 9]
        

    def teardown_method(self, method):
        tictactoe.input = input