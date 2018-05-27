if __name__ == "__main__":
    Enviroment = object
    STONES = 6
    SIDE = STONES + 1
    WIDTH = 6
    P1 = 1
    P2 = -1
    from board import Board

else:
    from ..environment import Environment, P1, P2
    from . import STONES, WIDTH, SIDE
    from .board import Board


P1_bool = False
P2_bool = True

class Kalaha(Environment):
    bmod = SIDE * 2 # board modulo

    def __init__(self, board = None):
        self.action_size = SIDE
        self.turn = P1_bool
        if board is None:
            self.board = Board(STONES, WIDTH)
        else:
            self.board = board

    def get_turn(self):
        return P2 if self.turn else P1

    def get_action_size(self):
        return self.action_size

    def playout(self, action):
        bmod = Kalaha.bmod
        selection = None # selected stone position

        if self.turn == P1_bool:
            selection = action
        else:
            selection = action + SIDE

        dist_stones = self.board.state[selection]
        self.board.state[selection] = 0
        for i in range(selection + 1, selection + 1 + dist_stones):
            index = i % bmod
            self.board.state[index] += 1

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


    def get_state_size(self):
        return len(self.board.state) + 1

    def get_state(self):
        return self.board.state[:] + [self.get_turn()]
        
    # returns a set of valid actions
    def valid_actions(self):
        if self.turn == P1_bool:
            stones = self.board.state[:WIDTH]
        else:
            stones = self.board.state[SIDE: -1]
        return [i for i, s in enumerate(stones) if s > 0]

    def is_complete(self):
        return sum(self.board.state[:WIDTH]) == 0 or \
               sum(self.board.state[WIDTH + 1: -1]) == 0

    def winner(self):
        if not self.is_complete():
            return None

        P1_score = sum(self.board.state[:SIDE])
        P2_score = sum(self.board.state[SIDE:])
        if P1_score > P2_score:
            return P1
        elif P1_score < P2_score:
            return P2
        else:
            return 0

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
        env_copy = Kalaha(self.board.copy())
        env_copy.turn = self.turn
        return env_copy

    def __str__(self):
        return str(self.board)

    def reset(self):
        self.board = Board(STONES, WIDTH)