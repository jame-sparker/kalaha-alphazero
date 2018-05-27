if __name__ == "__main__":
    Enviroment = object
    from board import Board
    O = "O"
    X = "X"
    P1 = 1
    P2 = -1
else:
    from ..environment import Environment, P1, P2
    from .board import Board
    from . import O, X


class TicTacToe(Environment):
    def __init__(self, board = None):
        if board is None:
            self.board = Board()
        else:
            self.board = board
        self.turn = P1

    def get_turn(self):
        return self.turn

    def get_action_size(self):
        return 9

    def playout(self, action):
        my_symbol = O if self.turn == P1 else X
        self.board.state[action] = my_symbol
        self.turn = -self.turn

    def get_state_size(self):
        return len(self.board.state) + 1

    def get_state(self):
        def to_number(s):
            if s == O:
                return 1
            elif s == X:
                return -1
            else:
                return 0
        
        return [to_number(s) for s in self.board.state] + [self.get_turn()]

    def valid_actions(self):
        return [i for i, s in enumerate(self.board.state) if s is None]

    def is_complete(self):
        return (None not in self.board.state) or self.winner() is not None

    def winner(self):

        def player(s):
            if s == O:
                return P1
            else:
                return P2

        s = self.board.state
        for i in range(0,3): # horizontal
            j = i * 3
            if s[j] is not None and s[j] == s[j + 1] and s[j] == s[j + 2]:
                return player(s[j])

        for i in range(0,3): # verticle
            if s[i] is not None and s[i] == s[i + 3] and s[i] == s[i + 6]:
                return player(s[i])

        # diagonal
        if s[0] is not None and s[0] == s[4] and s[0] == s[8]:
            return player(s[0])

        if s[2] is not None and s[2] == s[4] and s[2] == s[6]:
            return player(s[2])

        if None not in self.board.state:
            return 0
        return None # still playable
        
    # score in respect to the player
    def evaluate(self, player):
        winner = self.winner()
        if winner == player:
            return 1
        elif winner == -player:
            return -1
        else:
            return winner # 0 or None

    def copy(self):
        env_copy = TicTacToe(self.board.copy())
        env_copy.turn = self.turn
        return env_copy

    def __str__(self):
        return str(self.board)

    def reset(self):
        self.board = Board()