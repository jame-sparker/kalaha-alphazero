if __name__ == "__main__":
    Enviroment = object
    STONES = 6
    SIDE = STONES + 1
    WIDTH = 6
    from board import Board


else:
    from ..enviroment import Enviroment
    from . import STONES, WIDTH, SIDE
    from .board import Board


P1 = False
P2 = True

class Kalaha(Enviroment):
    bmod = SIDE * 2 # board modulo

    def __init__(self):
        self.turn = P1
        self.board = Board(STONES, WIDTH)

    def playout(self, action):
        bmod = Kalaha.bmod
        selection = None # selected stone position

        if self.turn == P1:
            selection = action
        else:
            selection = action + SIDE

        dist_stones = self.board.state[selection]
        self.board.state[selection] = 0
        for i in range(selection + 1, selection + 1 + dist_stones):
            index = i % bmod
            self.board.state[index] += 1
            # print(self)
            # print()

        # special case when the turn does not flip
        last_ind = (selection + dist_stones) % bmod
        my_store = ((self.turn + 1) * SIDE) - 1
        if last_ind != my_store:
            opp = WIDTH * 2 - last_ind
            if self.board.state[last_ind] == 1 and \
                last_ind // SIDE == self.turn and \
                self.board.state[opp] > 0: 
                # landed on the empty house on your side
                capture = (self.board.state[last_ind] + 
                           self.board.state[opp])
                self.board.state[last_ind] = 0
                self.board.state[opp] = 0
                self.board.state[my_store] += capture
            
            self.turn = not self.turn

        return self.state

    def state(self):
        if self.turn == P1:
            return self.board.state
        else:
            return self.board.get_swap()

    # returns a set of valid actions
    def valid_actions(self):
        if self.turn == P1:
            stones = self.board.state[:WIDTH]
        else:
            stones = self.board.state[SIDE: -1]
        return [i for i, s in enumerate(stones) if s > 0]

    def is_complete(self):
        return sum(self.board.state[:WIDTH]) == 0 or \
               sum(self.board.state[WIDTH - 1: -1]) == 0

    def winner(self):
        if not is_complete:
            return None
        return P1 if self.board.state[WIDTH] > self.board.state[-1] else P2

    def __str__(self):
        return str(self.board)
