import copy
import random
from itertools import chain
from math import inf

###############################################################

def flatten(listOfLists):
    return chain.from_iterable(listOfLists)

###############################################################

class Piece:
    NO_TOKEN = ' '
    PLAYER_TOKEN = 'O'
    OPPONENT_TOKEN = 'X'

    def __init__(self, number):
        self.number = number
        self.token = Piece.NO_TOKEN

    def __repr__(self):
        return str(self.number) + ": '" + self.token + "'"

    def has_number(self, number):
        return self.number == number

    def has_token(self, token):
        return self.token == token

    def is_not_taken(self):
        return self.token == Piece.NO_TOKEN

###############################################################

class QuixoBoard:
    def __init__(self):
        self.board = [
            [Piece(1),  Piece(2),  Piece(3),  Piece(4),  Piece(5)],
            [Piece(16), Piece(17), Piece(18), Piece(19), Piece(6)],
            [Piece(15), Piece(24), Piece(25), Piece(20), Piece(7)],
            [Piece(14), Piece(23), Piece(22), Piece(21), Piece(8)],
            [Piece(13), Piece(12), Piece(11), Piece(10), Piece(9)]
        ]

    def __repr__(self):
        return '\n'.join(str(row) for row in self.board)

    def piece_at(self, x, y):
        return self.board[y][x]

    def switch_pieces(self, selected_piece_number, piece_number_to_replace, token):
        selected_piece_coordinates = self.__search_coordinates_for_piece(selected_piece_number)
        piece_to_replace_coordinates = self.__search_coordinates_for_piece(piece_number_to_replace)

        has_to_replace_in_column = selected_piece_coordinates[0] == piece_to_replace_coordinates[0]
        has_to_replace_in_row = selected_piece_coordinates[1] == piece_to_replace_coordinates[1]

        if has_to_replace_in_row:
            self.__replace_in_row(selected_piece_coordinates, piece_to_replace_coordinates, token)
        elif has_to_replace_in_column:
            self.__replace_in_column(selected_piece_coordinates, piece_to_replace_coordinates, token)
        else:
            raise BaseException("Invalid move: You can only move pieces on the same row or column")

    def has_any_player_won(self):
        for column_index, _ in enumerate(self.board):
            tokens = list(map(lambda piece: piece.token, self.__column_on_index(column_index)))
            game_over = all(token == Piece.PLAYER_TOKEN for token in tokens) or all(token == Piece.OPPONENT_TOKEN for token in tokens)
            if game_over:
                return game_over

        for row in self.board:
            tokens = list(map(lambda piece: piece.token, row))
            game_over = all(token == Piece.PLAYER_TOKEN for token in tokens) or all(token == Piece.OPPONENT_TOKEN for token in tokens)
            if game_over:
                return game_over

        tokens = [row[i].token for i, row in enumerate(self.board)]
        game_over = all(token == Piece.PLAYER_TOKEN for token in tokens) or all(token == Piece.OPPONENT_TOKEN for token in tokens)
        if game_over:
            return game_over

        tokens = [row[i].token for i, row in enumerate(reversed(self.board))]
        game_over = all(token == Piece.PLAYER_TOKEN for token in tokens) or all(token == Piece.OPPONENT_TOKEN for token in tokens)
        if game_over:
            return game_over    

        return False

    # Testear. D:
    def valid_moves_for_player(self, token):
        moves = []
        
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if(piece.token == token or piece.token == Piece.NO_TOKEN):
                    if(y == 0):
                        moves.append((piece.number, self.board[4][x].number))
                        moves.append((piece.number, self.board[0][0].number))
                        moves.append((piece.number, self.board[0][4].number))
                    if(y == 4):
                        moves.append((piece.number, self.board[0][x].number))
                        moves.append((piece.number, self.board[4][0].number))                   
                        moves.append((piece.number, self.board[4][4].number))
                    if(x == 0):
                        moves.append((piece.number, row[4].number))
                        moves.append((piece.number, self.board[0][0].number))
                        moves.append((piece.number, self.board[4][0].number))
                    if(x == 4):
                        moves.append((piece.number, row[0].number))
                        moves.append((piece.number, self.board[0][4].number))
                        moves.append((piece.number, self.board[4][4].number))

        return list(filter(lambda move: move[0] != move[1], list(dict.fromkeys(moves)))) # Lista de tuplas

    def player_has_four_pieces_in_row_or_column(self, player):
        return self.__player_has_n_pieces_in_row_or_column(player, 4)

    def player_has_three_pieces_in_row_or_column(self, player):
        return self.__player_has_n_pieces_in_row_or_column(player, 3)

    def player_has_two_pieces_in_row_or_column(self, player):
        return self.__player_has_n_pieces_in_row_or_column(player, 2)

    def is_center_piece_free(self):
        center_piece = self.piece_at(2, 2)
        return center_piece.is_not_taken()

    def has_a_corner_free(self):
        corner_pieces = [self.piece_at(0, 0), self.piece_at(0, 4), self.piece_at(4, 0), self.piece_at(4, 4)]
        return any(corner_piece.is_not_taken() for corner_piece in corner_pieces)

    def __player_has_n_pieces_in_row_or_column(self, player, count):
        player_has_n_pieces_in_row = any(len(list(filter(lambda piece: piece == player, row))) == count for row in self.board)
        player_has_n_pieces_in_column = any(len(list(filter(lambda piece: piece == player, self.__column_on_index(y)))) == count for y, row in enumerate(self.board))
        return player_has_n_pieces_in_row or player_has_n_pieces_in_column

    def __search_coordinates_for_piece(self, piece_number_being_searched):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if piece.has_number(piece_number_being_searched):
                    return (x, y)

    def __replace_in_row(self, selected_piece_coordinates, piece_to_replace_coordinates, token):
        row_index = selected_piece_coordinates[1]
        selected_piece_column_index = selected_piece_coordinates[0]
        piece_to_replace_column_index = piece_to_replace_coordinates[0]

#        if self.__index_is_not_in_the_limits(row_index):
#            raise BaseException("Invalid move: You can only choose from pieces that are on the borders")

        row = self.board[row_index]
        self.__move_piece_from_to(row, selected_piece_column_index, piece_to_replace_column_index, token)
    
        self.board[row_index] = row           

    def __replace_in_column(self, selected_piece_coordinates, piece_to_replace_coordinates, token):
        column_index = selected_piece_coordinates[0]
        selected_piece_row_index = selected_piece_coordinates[1]
        piece_to_replace_row_index = piece_to_replace_coordinates[1]

#        if self.__index_is_not_in_the_limits(column_index):
#            raise BaseException("Invalid move: You can only choose from pieces that are on the borders")

        column = list(self.__column_on_index(column_index))
        self.__move_piece_from_to(column, selected_piece_row_index, piece_to_replace_row_index, token)
        
        for index, row in enumerate(self.board):
            row[column_index] = column[index]

    def __index_is_not_in_the_limits(self, index):
        return index != 0 and index != 4 # Hack-ish.

    def __move_piece_from_to(self, list, from_index, to_index, token):
        piece_to_move = list[from_index]

        if piece_to_move.token == Piece.NO_TOKEN or token == piece_to_move.token:
            piece_to_move.token = token
            list.remove(piece_to_move)
            list.insert(to_index, piece_to_move)
        else:
            raise BaseException("Invalid Move: You can only move empty pieces or your own pieces!")

    def __column_on_index(self, index):
        return map(lambda row: row[index], self.board)

###############################################################

class Quixo:
    def __init__(self):
        self.board = QuixoBoard()
    
    def playerPlay(self):
        player_move, _ = self.__alphabeta(self.board, 1, -inf, inf, Piece.PLAYER_TOKEN)
        print("Player Move: " + str(player_move))
        self.__move_for_player(self.board, player_move, Piece.PLAYER_TOKEN)
        self.__check_victory(Piece.PLAYER_TOKEN)
        return player_move

    def opponentPlay(self, move):
        print("Opponent Play: " + str(move))
        self.__move_for_player(self.board, move, Piece.OPPONENT_TOKEN)
        self.__check_victory(Piece.OPPONENT_TOKEN)

    def play(self, time):
        return self.playerPlay()

    def update(self, move):
        self.opponentPlay(move)

    def __check_victory(self, token):
        if(self.__game_over(self.board)):
            print(self.board)
            raise BaseException(token + "'s won!")    
    
    def __game_over(self, board):
        return board.has_any_player_won()

    def __valid_moves(self, board, player_token):
        return board.valid_moves_for_player(player_token)

    def __move_for_player(self, board, move, player_token):
        move_from = move[0]
        move_to = move[1]
        board.switch_pieces(move_from, move_to, player_token)

    def __play(self, board, valid_move, player_token):
        board_copy = copy.deepcopy(board)
        self.__move_for_player(board_copy, valid_move, player_token)
        return board_copy
        
    def __h(self, board, player):
        if board.player_has_four_pieces_in_row_or_column(player):
            return 10
        if(board.player_has_three_pieces_in_row_or_column(player)):
            return 9
        if(board.player_has_two_pieces_in_row_or_column(player)):
            return 8
        if(board.is_center_piece_free()):
            return 7
        if(board.has_a_corner_free()):
            return 6
        return int(random.uniform(0, 0.5) * 10)

    def __alphabeta(self, node, depth, alpha, beta, player):
        if depth == 0 or self.__game_over(node):
            return None, self.__h(node, player)
        if player == Piece.PLAYER_TOKEN:
            value = -inf
            best_move = None
            for move in self.__valid_moves(node, Piece.PLAYER_TOKEN):
                child = self.__play(node, move, Piece.PLAYER_TOKEN)
                _, deep_value = self.__alphabeta(child , depth - 1, alpha, beta , Piece.OPPONENT_TOKEN)

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
            for move in self.__valid_moves(node, Piece.OPPONENT_TOKEN):
                child = self.__play(node, move, Piece.OPPONENT_TOKEN)
                _, deep_value = self.__alphabeta(child , depth - 1, alpha, beta , Piece.PLAYER_TOKEN)

                if(deep_value < value):
                    best_move = move

                value = min(value, deep_value)
                beta  = min(beta , value)
                if alpha >= beta:
                    break # Alpha cut-off
            return best_move, value

###############################################################

# def main():
#     quixo = Quixo()

#     while(True):
#         quixo.playerPlay()
#         print(quixo.board)

#         from_input = int(input("From: "))
#         to_input = int(input("To: "))
#         quixo.opponentPlay((from_input, to_input))
#         print(quixo.board)

# main()