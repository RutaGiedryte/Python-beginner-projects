import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square, try again. ')
        return val
    
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf } # we want this to increase
        else:
            best = {'position': None, 'score': math.inf } # we want this to decrease

        for possible_move in state.available_moves():
            # 1. try the spot
            state.make_move(possible_move, player)

            # 2. simulate the game after this move recursively
            simulated_score = self.minimax(state, other_player)

            # 3. undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            simulated_score['position'] = possible_move

            # 4. possibly update the dictionary
            if player == max_player:
                if simulated_score['score'] > best['score']:
                    best = simulated_score
            else:
                if simulated_score['score'] < best['score']:
                    best = simulated_score
        return best

