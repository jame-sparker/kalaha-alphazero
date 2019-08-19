from ..agent import Agent
infinity = 1000

class Minimax(Agent):
    def __init__(self, depth, env):
        self.d = depth
        self.env = env

    def set_player(self, *args):
        pass

    def init_new_game(self, *args):
        pass

    def feed_op_action(self, *args):
        pass

    # implementation taken from http://aima.cs.berkeley.edu/python/games.html
    def get_action(self, *args):
        """Search game to determine best action; use alpha-beta pruning.
        This version cuts off search and uses an evaluation function."""
        env = self.env
        player = env.get_turn()

        def max_value(env, alpha, beta, depth):
            if depth == self.d or env.is_complete():
                return eval_fn(env)
            v = -infinity
            for a in env.valid_actions():
                env_copy = env.copy()
                env_copy.playout(a)
                v = max(v, min_value(env_copy, alpha, beta, depth+1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def min_value(env, alpha, beta, depth):
            if depth == self.d or env.is_complete():
                return eval_fn(env)
            v = infinity
            for a in env.valid_actions():
                env_copy = env.copy()
                env_copy.playout(a)
                v = min(v, max_value(env_copy, alpha, beta, depth+1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        def eval_fn(env):
            if env.is_complete():
                if env.winner() == player:
                    return 100
                else:
                    return -100
            return env.heuristic(player)
        # Body of alphabeta_search starts here:
        # The default test cuts off at depth d or at a terminal state

        action_value_pair = []
        for a in env.valid_actions():
            env_copy = env.copy()
            env_copy.playout(a)
            v = min_value(env_copy, -infinity, infinity, 0)
            action_value_pair.append((a, v))

        action = max(action_value_pair, key=lambda x: x[1])[0]
        return action

        