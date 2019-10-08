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

class Tile:
    def __init__(self):
        

class Quixo:
    # Tablero de 5 x 5
    # Jugadas -> Tuplas entre 1 y 20 - (en_que_posicion_se_remueve, en_que_posicion_se_agrega)

    NO_TOKEN = ' '
    PLAYER_TOKEN = 'O'
    OPPONENT_TOKEN = 'X'

    def __init__(self):
        self.board = [
            [{ 'index': 1, 'content': ''}, ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]

    def playerPlay(self):
        print('Actualizar Tablero')
        (0, 0) # Jugada valida que da .alphabeta

    def opponentPlay(self, play):
        tile_to_remove = 15
        tile_to_add = 7
        play = (tile_to_remove, tile_to_add)

        self.board = [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', 'X', ' ', ' ', ' ']
        ]

        print('Actualizar Tablero')
        

quixo = Quixo()