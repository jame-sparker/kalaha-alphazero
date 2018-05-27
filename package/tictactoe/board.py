""" Written by James Parker 25th May
"""
try:
    from . import O, X
except:
    O = "O"
    X = "X"

class Board:
    def __init__(self, state=None):
        if state is None:
            self.state = [None] * 9
        else:
            self.state = state

    def copy(self):
        board_copy = Board(self.state[:])
        return board_copy

    def get_swap(self):
        def flip(s):
            if s == O:
                return X
            elif s == X:
                return O
            return s

        return [flip(e) for e in self.state]

    def __str__(self):
        str_state = [(" " if e is None else e) for e in self.state]
        output = "|".join(str_state[:3]) + "\n" +\
                 "-" * 5 + "\n" +\
                 "|".join(str_state[3:6])+ "\n" +\
                 "-" * 5 + "\n" +\
                 "|".join(str_state[6:])
        return output
