### implementation of alphazero by James Parker. May 25th
import numpy as np

from ..agent import Agent
from .evaluator import Evaluator
from .mctree import MCTree
from .queue import Queue

from . import ITERATIONS, BATCH_SIZE, HISTORY_SIZE

class AlphaZero(Agent):

    def __init__(self, sizes=None, env=None, history=None):
        self.player = None
        self.env = env

        if sizes is not None:
            self.evaluator = Evaluator(sizes)

        if history is None:
            self.history = Queue(HISTORY_SIZE)
        else:
            self.history = history

        self.mctree = None
        self.game_states = None

    def init_new_game(self):
        # stores a tuple of (state, action_prob)
        self.game_states = [] 
        self.mctree = MCTree(self.env, self.evaluator, ITERATIONS)

    def set_player(self, player):
        self.player = player
        
    def get_action(self):
        self.mctree.search(self.env.copy(), self.player)

        pi = self.mctree.get_action_probabilities(1, self.env.get_action_size())
        # p = self.mctree.root.children_evalutions
        state = self.env.get_state()

        a = self.mctree.select_action_and_update(0)

        self.game_states.append((state, pi))

        return a

    def feed_op_action(self, a):
        # update internal knowldege with opponent's action
        self.mctree.update(a, self.env)


    def update(self, winner):
        for state, pi in self.game_states:
            turn = state[-1]
            if winner == turn:
                player_reward = winner
            else:
                player_reward = -winner
            x = state
            y1 = pi
            y2 = [(player_reward + 1) / 2]
            self.history.add((x, y1, y2))

    def train(self):
        data_points = self.history.random_samples(BATCH_SIZE)
        x, y1, y2 = list(zip(*data_points))
        x = np.array(x)
        y1 = np.array(y1)
        y2 = np.array(y2)
        self.evaluator.train(x, y1, y2)

    def evaluate(self, env):
        return self.evaluator.evaluate(env.get_state())

    def copy(self):
        az = AlphaZero()
        az.player = self.player
        az.env = self.env
        az.evaluator = self.evaluator.copy()
        az.history = self.history.copy()
        return az