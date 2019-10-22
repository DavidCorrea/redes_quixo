import copy
import random
from math import inf
from quixo_board import QuixoBoard, Piece

###############################################################

###############################################################

def __game_over(board):
    return board.has_any_player_won()

def __valid_moves(board, player_token):
    return board.valid_moves_for_player(player_token)

def __move_for_player(board, move, player_token):
    move_from = move[0]
    move_to = move[1]
    board.switch_pieces(move_from, move_to, player_token)

def __play(board, valid_move, player_token):
    board_copy = copy.deepcopy(board)
    __move_for_player(board_copy, valid_move, player_token)
    return board_copy
    
def __h(board, player):
    if board.player_has_four_pieces_together(player):
        return 10
    if(board.player_has_three_pieces_together(player)):
        return 9
    if(board.player_has_two_pieces_together(player)):
        return 8
    if(board.is_center_piece_free()):
        return 7
    if(board.has_a_corner_free()):
        return 6
    return int(random.uniform(0, 0.5) * 10)    

def __alphabeta(node, depth, alpha, beta, player):
    if depth == 0 or __game_over(node):
        return None, __h(node, player)
    if player == Piece.PLAYER_TOKEN:
        value = -inf
        best_move = None
        for move in __valid_moves(node, Piece.PLAYER_TOKEN):
            child = __play(node, move, Piece.PLAYER_TOKEN)
            _, deep_value = __alphabeta(child , depth - 1, alpha, beta , Piece.OPPONENT_TOKEN)

            if(deep_value > value):
                best_move = move

            value = max(value, deep_value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break # Beta cut-off
        return best_move, value
    else:
        value = inf
        best_move = None
        for move in __valid_moves(node, Piece.OPPONENT_TOKEN):
            child = __play(node, move, Piece.OPPONENT_TOKEN)
            _, deep_value = __alphabeta(child , depth - 1, alpha, beta , Piece.PLAYER_TOKEN)

            if(deep_value < value):
                best_move = move

            value = min(value, deep_value)
            beta  = min(beta , value)
            if alpha >= beta:
                break # Alpha cut-off
        return best_move, value

###############################################################

_board = QuixoBoard()

def __check_victory(token):
    if(__game_over(_board)):
        print(_board)
        raise BaseException(token + "'s won!")

def player_play():
    player_move, _ = __alphabeta(_board, 1, -inf, inf, Piece.PLAYER_TOKEN)
    print("Player Move: " + str(player_move))
    __move_for_player(_board, player_move, Piece.PLAYER_TOKEN)
    __check_victory(Piece.PLAYER_TOKEN)
    return player_move

def opponent_play(opponent_move):
    print("Opponent Play: " + str(opponent_move))
    __move_for_player(_board, opponent_move, Piece.OPPONENT_TOKEN)
    __check_victory(Piece.OPPONENT_TOKEN)

###############################################################

def main():
    while(True):
        player_play()
        print(_board)

        from_input = int(input("From: "))
        to_input = int(input("To: "))
        opponent_play((from_input, to_input))
        print(_board)

main()