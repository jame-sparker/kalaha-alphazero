### implementation of alphazero by James Parker. May 25th
import numpy as np

from ..agent import Agent
from .evaluator import Evaluator
from .mctree import MCTree
from .queue import Queue

from . import ITERATIONS, BATCH_SIZE

def AlphaZero(Agent):

    def __init__(player, sizes, env):
        self.player = player
        self.env = env
        self.evaluator = Evaluator(sizes)
        self.history = queue
        self.mctree = None
        self.game_states = None

    def init_new_game(self):
        # stores a tuple of (state, action_prob, turn)
        self.game_states = [] 
        self.mctree = MCTree(self.env, self.evaluator, ITERATIONS)
        
    def get_action(self, state):
        self.mctree.search(self.env.copy(), self.player)

        pi = self.mctree.get_action_probabilities(1, self.env.get_action_size())
        # p = self.mctree.root.children_evalutions
        state = self.env.get_state()
        turn = self.env.get_turn()

        a = self.mctree.select_action_and_update(0)

        self.game_states.append((state, pi, turn))

        return a

    def update(self, winner):
        for state, pi, p, turn in self.game_states:
            if winner == turn:
                player_reward = winner
            else 
                player_reward = -winner
            x = state + [turn]
            y1 = pi
            y2 = [player_reward]
            self.history.add((x, y1, y2))

    def train(self):
        data_points = self.history.random_samples(BATCH_SIZE)
        x, y1, y2 = list(zip(*data_points))
        x = np.array(x)
        y1 = np.array(x)
        y2 = np.array(x)
        self.evaluator.train(x, y1, y2)