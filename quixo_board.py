class Piece:
    NO_TOKEN = ' '
    PLAYER_TOKEN = 'O'
    OPPONENT_TOKEN = 'X'

    def __init__(self, number):
        self.number = number
        self.token = Piece.NO_TOKEN

    def __repr__(self):
        return "[ " + str(self.number) + ": '" + self.token + "' ]"

    def has_number(self, number):
        return self.number == number

    def has_token(self, token):
        return self.token == token    

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

    def is_finished(self):
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
    def valid_moves(self, token):
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

    def __search_coordinates_for_piece(self, piece_number_being_searched):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if piece.has_number(piece_number_being_searched):
                    return (x, y)

    def __replace_in_row(self, selected_piece_coordinates, piece_to_replace_coordinates, token):
        row_index = selected_piece_coordinates[1]
        selected_piece_column_index = selected_piece_coordinates[0]
        piece_to_replace_column_index = piece_to_replace_coordinates[0]

        if self.__index_is_not_in_the_limits(selected_piece_column_index):
            raise BaseException("Invalid move: You can only choose from pieces that are on the borders")

        row = self.board[row_index]
        self.__move_piece_from_to(row, selected_piece_column_index, piece_to_replace_column_index, token)
    
        self.board[row_index] = row           

    def __replace_in_column(self, selected_piece_coordinates, piece_to_replace_coordinates, token):
        column_index = selected_piece_coordinates[0]
        selected_piece_row_index = selected_piece_coordinates[1]
        piece_to_replace_row_index = piece_to_replace_coordinates[1]

        if self.__index_is_not_in_the_limits(selected_piece_row_index):
            raise BaseException("Invalid move: You can only choose from pieces that are on the borders")

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