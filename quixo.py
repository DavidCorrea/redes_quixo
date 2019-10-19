import copy
from quixo_board import QuixoBoard, Piece
from math import inf

class Quixo:
    MAX = 1

    def __init__(self):
        self.board = QuixoBoard()

    def player_play(self):
        board = copy.deepcopy(self.board)
        my_play, _ = self.__alphabeta(board, 1, -inf, inf, 1)

        print("Player Plays " + str(my_play))
        self.board.switch_pieces(my_play[0], my_play[1], Piece.PLAYER_TOKEN)

    def opponent_play(self, play):
        print("Opponent Plays " + str(play))
        self.board.switch_pieces(play[0], play[1], Piece.OPPONENT_TOKEN)

    def __game_over(self, current_board):
        return current_board.is_finished()

    def __valid_moves(self, current_board):
        return current_board.valid_moves(Piece.PLAYER_TOKEN)

    def __play(self, current_board, valid_move):
        board = copy.deepcopy(current_board)
        board.switch_pieces(valid_move[0], valid_move[1], Piece.PLAYER_TOKEN)
        return board
        
    def __h(self, current_board): # Heuristica
        return 1

    def __alphabeta(self, node, depth, alpha, beta, player):
        if depth == 0 or self.__game_over(node):
            return None, self.__h(node)
        if player == Quixo.MAX:
            value = -inf
            best_move = None
            for move in self.__valid_moves(node):
                child = self.__play(node, move)
                best_move = move
                value = max(value, self.__alphabeta(child, depth - 1, alpha, beta, -player)[1])
                alpha = max(alpha, value)
                if alpha >= beta:
                    break # Beta cut-off
            return best_move, value
        else:
            value = inf
            best_move = None
            for move in self.__valid_moves(node):
                child = self.__play(node , move)
                best_move = move
                value = min(value, self.__alphabeta(child , depth - 1, alpha, beta , -player)[1])
                beta  = min(beta , value)
                if alpha >= beta:
                    break # Alpha cut-off
            return best_move, value          