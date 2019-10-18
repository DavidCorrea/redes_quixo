import unittest
from quixo_board import QuixoBoard, Piece

class TestQuixo(unittest.TestCase):
    def test_board_initialization(self):
        """
        Board gets initializated with the correct order of pieces.
        """
        quixo = QuixoBoard()
        self.assertTrue(quixo.piece_at(0, 0).has_number(1))
        self.assertTrue(quixo.piece_at(1, 0).has_number(2))
        self.assertTrue(quixo.piece_at(2, 0).has_number(3))
        self.assertTrue(quixo.piece_at(3, 0).has_number(4))
        self.assertTrue(quixo.piece_at(4, 0).has_number(5))

        self.assertTrue(quixo.piece_at(0, 1).has_number(16))
        self.assertTrue(quixo.piece_at(1, 1).has_number(17))
        self.assertTrue(quixo.piece_at(2, 1).has_number(18))
        self.assertTrue(quixo.piece_at(3, 1).has_number(19))
        self.assertTrue(quixo.piece_at(4, 1).has_number(6))

        self.assertTrue(quixo.piece_at(0, 2).has_number(15))
        self.assertTrue(quixo.piece_at(1, 2).has_number(24))
        self.assertTrue(quixo.piece_at(2, 2).has_number(25))
        self.assertTrue(quixo.piece_at(3, 2).has_number(20))
        self.assertTrue(quixo.piece_at(4, 2).has_number(7))

        self.assertTrue(quixo.piece_at(0, 3).has_number(14))
        self.assertTrue(quixo.piece_at(1, 3).has_number(23))
        self.assertTrue(quixo.piece_at(2, 3).has_number(22))
        self.assertTrue(quixo.piece_at(3, 3).has_number(21))
        self.assertTrue(quixo.piece_at(4, 3).has_number(8))

        self.assertTrue(quixo.piece_at(0, 4).has_number(13))
        self.assertTrue(quixo.piece_at(1, 4).has_number(12))
        self.assertTrue(quixo.piece_at(2, 4).has_number(11))
        self.assertTrue(quixo.piece_at(3, 4).has_number(10))
        self.assertTrue(quixo.piece_at(4, 4).has_number(9))

    def test_pieces_switch_row_from_left_to_right(self):
        """
        Pieces are switched correctly.
        """
        quixo = QuixoBoard()
        quixo.switch_pieces(1, 5, Piece.PLAYER_TOKEN)

        self.assertTrue(quixo.piece_at(0, 0).has_number(2))
        self.assertTrue(quixo.piece_at(1, 0).has_number(3))
        self.assertTrue(quixo.piece_at(2, 0).has_number(4))
        self.assertTrue(quixo.piece_at(3, 0).has_number(5))
        self.assertTrue(quixo.piece_at(4, 0).has_number(1))

        self.assertTrue(quixo.piece_at(4, 0).has_token(Piece.PLAYER_TOKEN))

    def test_pieces_switch_row_from_right_to_left(self):
        """
        Pieces are switched correctly.
        """
        quixo = QuixoBoard()
        quixo.switch_pieces(5, 1, Piece.PLAYER_TOKEN)

        self.assertTrue(quixo.piece_at(0, 0).has_number(5))
        self.assertTrue(quixo.piece_at(1, 0).has_number(1))
        self.assertTrue(quixo.piece_at(2, 0).has_number(2))
        self.assertTrue(quixo.piece_at(3, 0).has_number(3))
        self.assertTrue(quixo.piece_at(4, 0).has_number(4))

        self.assertTrue(quixo.piece_at(0, 0).has_token(Piece.PLAYER_TOKEN))

    def test_pieces_switch_row_from_top_to_bottom(self):
        """
        Pieces are switched correctly.
        """
        quixo = QuixoBoard()
        quixo.switch_pieces(1, 13, Piece.PLAYER_TOKEN)

        self.assertTrue(quixo.piece_at(0, 0).has_number(16))
        self.assertTrue(quixo.piece_at(0, 1).has_number(15))
        self.assertTrue(quixo.piece_at(0, 2).has_number(14))
        self.assertTrue(quixo.piece_at(0, 3).has_number(13))
        self.assertTrue(quixo.piece_at(0, 4).has_number(1))

        self.assertTrue(quixo.piece_at(0, 4).has_token(Piece.PLAYER_TOKEN))

    def test_pieces_switch_row_from_bottom_to_top(self):
        """
        Pieces are switched correctly.
        """
        quixo = QuixoBoard()
        quixo.switch_pieces(13, 1, Piece.PLAYER_TOKEN)

        self.assertTrue(quixo.piece_at(0, 0).has_number(13))
        self.assertTrue(quixo.piece_at(0, 1).has_number(1))
        self.assertTrue(quixo.piece_at(0, 2).has_number(16))
        self.assertTrue(quixo.piece_at(0, 3).has_number(15))
        self.assertTrue(quixo.piece_at(0, 4).has_number(14))

        self.assertTrue(quixo.piece_at(0, 0).has_token(Piece.PLAYER_TOKEN))

    def test_pieces_switch_on_pieces_that_are_not_on_the_same_column_or_row(self):
        """
        An error is raised.
        """
        quixo = QuixoBoard()

        with self.assertRaises(BaseException):
            quixo.switch_pieces(1, 9, Piece.PLAYER_TOKEN)

    def test_pieces_switch_on_pieces_that_are_from_the_opponent(self):
        """
        An error is raised.
        """
        quixo = QuixoBoard()
        quixo.switch_pieces(1, 13, Piece.PLAYER_TOKEN)

        with self.assertRaises(BaseException):
            quixo.switch_pieces(1, 9, Piece.OPPONENT_TOKEN)

    def test_pieces_switch_on_positions_that_are_not_on_the_board_limits(self):
        """
        An error is raised.
        """
        quixo = QuixoBoard()

        with self.assertRaises(BaseException):
            quixo.switch_pieces(17, 24, Piece.PLAYER_TOKEN)

    def test_game_over_on_column(self):
        """
        True when any column has all the same symbols.
        """
        quixo = QuixoBoard()

        quixo.switch_pieces(1, 13, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(16, 1, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(15, 16, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(14, 15, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(13, 14, Piece.PLAYER_TOKEN)

        self.assertTrue(quixo.is_finished())

    def test_game_over_on_row(self):
        """
        True when any row has all the same symbols.
        """
        quixo = QuixoBoard()

        quixo.switch_pieces(1, 5, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(2, 1, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(3, 2, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(4, 3, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(5, 4, Piece.PLAYER_TOKEN)

        self.assertTrue(quixo.is_finished())

    def test_game_over_on_diagonal_from_left_to_right(self):
        """
        True when any diagonal has all the same symbols.
        """
        quixo = QuixoBoard()

        quixo.switch_pieces(5, 1, Piece.PLAYER_TOKEN)

        quixo.switch_pieces(6, 16, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(19, 6, Piece.PLAYER_TOKEN)

        quixo.switch_pieces(7, 15, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(20, 7, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(25, 20, Piece.PLAYER_TOKEN)

        quixo.switch_pieces(8, 14, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(21, 8, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(22, 21, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(23, 22, Piece.PLAYER_TOKEN)

        quixo.switch_pieces(13, 9, Piece.PLAYER_TOKEN)

        self.assertTrue(quixo.is_finished())

    def test_game_over_on_diagonal_from_right_to_left(self):
        """
        True when any diagonal has all the same symbols.
        """
        quixo = QuixoBoard()

        quixo.switch_pieces(1, 5, Piece.PLAYER_TOKEN)

        quixo.switch_pieces(16, 6, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(17, 16, Piece.PLAYER_TOKEN)

        quixo.switch_pieces(15, 7, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(24, 15, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(25, 24, Piece.PLAYER_TOKEN)

        quixo.switch_pieces(14, 8, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(23, 14, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(22, 23, Piece.PLAYER_TOKEN)
        quixo.switch_pieces(21, 22, Piece.PLAYER_TOKEN)

        quixo.switch_pieces(9, 13, Piece.PLAYER_TOKEN)

        self.assertTrue(quixo.is_finished())

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