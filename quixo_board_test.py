import unittest
from quixo_board import QuixoBoard, Piece

# Outdated

class TestQuixo(unittest.TestCase):
    def setUp(self):
        self.quixo_board = QuixoBoard()

    def test_board_initialization(self):
        """
        Board gets initializated with the correct order of pieces.
        """
        self.assertTrue(self.quixo_board.piece_at(0, 0).has_number(1))
        self.assertTrue(self.quixo_board.piece_at(1, 0).has_number(2))
        self.assertTrue(self.quixo_board.piece_at(2, 0).has_number(3))
        self.assertTrue(self.quixo_board.piece_at(3, 0).has_number(4))
        self.assertTrue(self.quixo_board.piece_at(4, 0).has_number(5))

        self.assertTrue(self.quixo_board.piece_at(0, 1).has_number(16))
        self.assertTrue(self.quixo_board.piece_at(1, 1).has_number(17))
        self.assertTrue(self.quixo_board.piece_at(2, 1).has_number(18))
        self.assertTrue(self.quixo_board.piece_at(3, 1).has_number(19))
        self.assertTrue(self.quixo_board.piece_at(4, 1).has_number(6))

        self.assertTrue(self.quixo_board.piece_at(0, 2).has_number(15))
        self.assertTrue(self.quixo_board.piece_at(1, 2).has_number(24))
        self.assertTrue(self.quixo_board.piece_at(2, 2).has_number(25))
        self.assertTrue(self.quixo_board.piece_at(3, 2).has_number(20))
        self.assertTrue(self.quixo_board.piece_at(4, 2).has_number(7))

        self.assertTrue(self.quixo_board.piece_at(0, 3).has_number(14))
        self.assertTrue(self.quixo_board.piece_at(1, 3).has_number(23))
        self.assertTrue(self.quixo_board.piece_at(2, 3).has_number(22))
        self.assertTrue(self.quixo_board.piece_at(3, 3).has_number(21))
        self.assertTrue(self.quixo_board.piece_at(4, 3).has_number(8))

        self.assertTrue(self.quixo_board.piece_at(0, 4).has_number(13))
        self.assertTrue(self.quixo_board.piece_at(1, 4).has_number(12))
        self.assertTrue(self.quixo_board.piece_at(2, 4).has_number(11))
        self.assertTrue(self.quixo_board.piece_at(3, 4).has_number(10))
        self.assertTrue(self.quixo_board.piece_at(4, 4).has_number(9))

    def test_switching_pieces_change_selected_piece_token(self):
        """
        When selecting a piece to move, its token gets updated properly.
        """
        self.quixo_board.switch_pieces(1, 5, Piece.PLAYER_TOKEN)

        self.assertTrue(self.quixo_board.piece_at(4, 0).has_token(Piece.PLAYER_TOKEN))    

    def test_switching_pieces_in_a_row_from_left_to_right(self):
        """
        When selecting a piece to move that it's located on the left side of the board to be moved to the right side,
        it should push all the pieces of the same row to the left.

        e.g. [1,2,3,4,5] and 1 is selected

             [2,3,4,5,1]
        """
        self.quixo_board.switch_pieces(1, 5, Piece.PLAYER_TOKEN)

        self.assertTrue(self.quixo_board.piece_at(0, 0).has_number(2))
        self.assertTrue(self.quixo_board.piece_at(1, 0).has_number(3))
        self.assertTrue(self.quixo_board.piece_at(2, 0).has_number(4))
        self.assertTrue(self.quixo_board.piece_at(3, 0).has_number(5))
        self.assertTrue(self.quixo_board.piece_at(4, 0).has_number(1))

    def test_switching_pieces_in_a_row_from_right_to_left(self):
        """
        When selecting a piece to move that it's located on the right side of the board to be moved to the left side,
        it should push all the pieces of the same row to the right.

        e.g. [1,2,3,4,5] and 5 is selected

             [5,1,2,3,4]
        """
        self.quixo_board.switch_pieces(5, 1, Piece.PLAYER_TOKEN)

        self.assertTrue(self.quixo_board.piece_at(0, 0).has_number(5))
        self.assertTrue(self.quixo_board.piece_at(1, 0).has_number(1))
        self.assertTrue(self.quixo_board.piece_at(2, 0).has_number(2))
        self.assertTrue(self.quixo_board.piece_at(3, 0).has_number(3))
        self.assertTrue(self.quixo_board.piece_at(4, 0).has_number(4))

    def test_switching_pieces_in_a_column_from_top_to_bottom(self):
        """
        When selecting a piece to move that it's located on the top side of the board to be moved to the bottom side,
        it should push all the pieces of the same column to the top.

        e.g. [1,
              2,
              3,
              4,
              5] and 1 is selected

             [2,
              3,
              4,
              5,
              1]
        """
        self.quixo_board.switch_pieces(1, 13, Piece.PLAYER_TOKEN)

        self.assertTrue(self.quixo_board.piece_at(0, 0).has_number(16))
        self.assertTrue(self.quixo_board.piece_at(0, 1).has_number(15))
        self.assertTrue(self.quixo_board.piece_at(0, 2).has_number(14))
        self.assertTrue(self.quixo_board.piece_at(0, 3).has_number(13))
        self.assertTrue(self.quixo_board.piece_at(0, 4).has_number(1))

    def test_switching_pieces_in_a_column_from_bottom_to_top(self):
        """
        When selecting a piece to move that it's located on the bottom side of the board to be moved to the top side,
        it should push all the pieces of the same column to the bottom.

        e.g. [1,
              2,
              3,
              4,
              5] and 5 is selected

             [5,
              1,
              2,
              3,
              4]
        """
        self.quixo_board.switch_pieces(13, 1, Piece.PLAYER_TOKEN)

        self.assertTrue(self.quixo_board.piece_at(0, 0).has_number(13))
        self.assertTrue(self.quixo_board.piece_at(0, 1).has_number(1))
        self.assertTrue(self.quixo_board.piece_at(0, 2).has_number(16))
        self.assertTrue(self.quixo_board.piece_at(0, 3).has_number(15))
        self.assertTrue(self.quixo_board.piece_at(0, 4).has_number(14))

    def test_switching_pieces_that_are_not_on_the_same_row(self):
        """
        An error is raised.
        """
        with self.assertRaises(BaseException):
            self.quixo_board.switch_pieces(1, 6, Piece.PLAYER_TOKEN)

    def test_switching_pieces_that_are_not_on_the_same_column(self):
        """
        An error is raised.
        """
        with self.assertRaises(BaseException):
            self.quixo_board.switch_pieces(1, 12, Piece.PLAYER_TOKEN)        

    def test_switching_pieces_that_are_from_the_opponent(self):
        """
        An error is raised.
        """
        self.quixo_board.switch_pieces(1, 13, Piece.PLAYER_TOKEN)

        with self.assertRaises(BaseException):
            self.quixo_board.switch_pieces(1, 9, Piece.OPPONENT_TOKEN)

    def test_switching_pieces_that_are_not_on_the_board_limits(self):
        """
        An error is raised.
        """
        with self.assertRaises(BaseException):
            self.quixo_board.switch_pieces(17, 24, Piece.PLAYER_TOKEN)

    def test_game_is_over_on_column_with_same_symbols(self):
        """
        True when any column has all the same symbols.
        """
        self.quixo_board.switch_pieces(1, 13, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(16, 1, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(15, 16, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(14, 15, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(13, 14, Piece.PLAYER_TOKEN)

        self.assertTrue(self.quixo_board.is_finished())

    def test_game_is_over_on_row_with_same_symbols(self):
        """
        True when any row has all the same symbols.
        """
        self.quixo_board.switch_pieces(1, 5, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(2, 1, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(3, 2, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(4, 3, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(5, 4, Piece.PLAYER_TOKEN)

        self.assertTrue(self.quixo_board.is_finished())

    def test_game_is_over_on_diagonal_with_same_symbols_from_top_left_to_bottom_right(self):
        """
        True when any diagonal has all the same symbols.
        """
        self.quixo_board.switch_pieces(5, 1, Piece.PLAYER_TOKEN)

        self.quixo_board.switch_pieces(6, 16, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(19, 6, Piece.PLAYER_TOKEN)

        self.quixo_board.switch_pieces(7, 15, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(20, 7, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(25, 20, Piece.PLAYER_TOKEN)

        self.quixo_board.switch_pieces(8, 14, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(21, 8, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(22, 21, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(23, 22, Piece.PLAYER_TOKEN)

        self.quixo_board.switch_pieces(13, 9, Piece.PLAYER_TOKEN)

        self.assertTrue(self.quixo_board.is_finished())

    def test_game_is_over_on_diagonal_with_same_symbols_from_top_right_to_bottom_left(self):
        """
        True when any diagonal has all the same symbols.
        """
        self.quixo_board.switch_pieces(1, 5, Piece.PLAYER_TOKEN)

        self.quixo_board.switch_pieces(16, 6, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(17, 16, Piece.PLAYER_TOKEN)

        self.quixo_board.switch_pieces(15, 7, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(24, 15, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(25, 24, Piece.PLAYER_TOKEN)

        self.quixo_board.switch_pieces(14, 8, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(23, 14, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(22, 23, Piece.PLAYER_TOKEN)
        self.quixo_board.switch_pieces(21, 22, Piece.PLAYER_TOKEN)

        self.quixo_board.switch_pieces(9, 13, Piece.PLAYER_TOKEN)

        self.assertTrue(self.quixo_board.is_finished())

    # def test_valid_moves(self):
    #     """
    #     True when any diagonal has all the same symbols.
    #     """
    #     quixo = QuixoBoard()

    #     quixo.switch_pieces(1, 5, Piece.PLAYER_TOKEN)

    #     quixo.switch_pieces(16, 6, Piece.PLAYER_TOKEN)
    #     quixo.switch_pieces(17, 16, Piece.PLAYER_TOKEN)

    #     quixo.switch_pieces(15, 7, Piece.PLAYER_TOKEN)
    #     quixo.switch_pieces(24, 15, Piece.PLAYER_TOKEN)
    #     quixo.switch_pieces(25, 24, Piece.PLAYER_TOKEN)

    #     quixo.switch_pieces(14, 8, Piece.PLAYER_TOKEN)
    #     quixo.switch_pieces(23, 14, Piece.PLAYER_TOKEN)
    #     quixo.switch_pieces(22, 23, Piece.PLAYER_TOKEN)
    #     quixo.switch_pieces(21, 22, Piece.PLAYER_TOKEN)

    #     quixo.switch_pieces(9, 13, Piece.PLAYER_TOKEN)

    #     self.assertTrue(quixo.is_finished())     

if __name__ == '__main__':
    unittest.main()