if __name__ == "__main__":
    Enviroment = object
    from board import Board
    O = "O"
    X = "X"
else:
    from ..enviroment import Enviroment
    from .board import Board
    from . import O, X

P1 = False
P2 = True

class TicTacToe(Enviroment):
    def __init__(self):
        self.board = Board()
        self.turn = P1

    def playout(self, action):
        my_symbol = O if self.turn == P1 else X
        self.board.state[action] = my_symbol
        self.turn = not self.turn

    def state(self):
        if self.turn == P1:
            return self.board.state
        else:
            return self.board.get_swap()

    def valid_actions(self):
        return [i for i, s in enumerate(self.board.state) if s is None]

    def is_complete(self):
        return (not None in self.board.state) or self.winner() is not None

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

        return None

    def __str__(self):
        return str(self.board)

