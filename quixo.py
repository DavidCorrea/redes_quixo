def alphabeta(node, depth, alpha, beta, player):
    if depth == 0 or game_over(node):
        return h(node)
    if player == MAX :
        value = - inf
        for move in valid_moves(node):
            child = play(node, move)
            value = max(value, alphabeta(child, depth - 1, alpha, beta, -player))
            alpha = max(alpha, value)
            if alpha >= beta :
                break # Beta cut - off
        return value
    else:
        value = inf
        for move in valid_moves(node):
            child = play(node, move)
            value = min(value, alphabeta(child, depth - 1, alpha, beta, -player))
            beta = min ( beta , value )
            if alpha >= beta :
                break # Alpha cut - off
        return value

def new_tile(index):
    return { 'index': index, 'content': Quixo.NO_TOKEN }

class Quixo:
    # Tablero de 5 x 5
    # Jugadas -> Tuplas entre 1 y 20 - (en_que_posicion_se_remueve, en_que_posicion_se_agrega)

    NO_TOKEN = ' '
    PLAYER_TOKEN = '0'
    OPPONENT_TOKEN = 'X'

    def __init__(self):
        self.board = [
            [new_tile(1),  new_tile(2),  new_tile(3),  new_tile(4),  new_tile(5)],
            [new_tile(16), new_tile(17), new_tile(18), new_tile(19), new_tile(6)],
            [new_tile(15), new_tile(24), new_tile(25), new_tile(20), new_tile(7)],
            [new_tile(14), new_tile(23), new_tile(22), new_tile(21), new_tile(8)],
            [new_tile(13), new_tile(12), new_tile(11), new_tile(10), new_tile(9)]
        ]

    def playerPlay(self):
        print('Actualizar Tablero')
        (0, 0) # Jugada valida que da .alphabeta

    # play es una tupla: (en_que_posicion_se_remueve, en_que_posicion_se_agrega)
    def opponentPlay(self, play):
        tile_to_remove = play[0]
        tile_to_add = play[1]

        # Inicialización coordenadas
        tile_to_remove_coordinate = (0, 0)
        tile_to_add_coordinate = (0, 0)

        # Busco en que coordenadas estan las fichas
        for y, row in enumerate(self.board):
            for x, column in enumerate(row):
                if column['index'] == tile_to_remove:
                    tile_to_remove_coordinate = (x, y)
                if column['index'] == tile_to_add:
                    tile_to_add_coordinate = (x, y)

        # Identificar el tipo de movimiento (Invalido, debo mover columna, debo mover fila)
        has_to_move_column = tile_to_add_coordinate[0] == tile_to_remove_coordinate[0]
        has_to_move_row = tile_to_add_coordinate[1] == tile_to_remove_coordinate[1]
        is_invalid_play = not has_to_move_column and not has_to_move_row

        print('Has to move Column: ' + str(has_to_move_column))
        print('Has to move Row: ' + str(has_to_move_row))
        print('Invalid Play: ' + str(is_invalid_play))

quixo = Quixo()
quixo.opponentPlay(( 5, 9 ))