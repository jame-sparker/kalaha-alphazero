from . import CPUCT
import random

class MCTree:
    def __init__(self, iterations):
        self.root = Node()
        self.iterations = iterations

    # iterative implementation instead of recursion for efficiency.
    def search(env_copy, player):
        """ Performs MCTS for self.iterations number of times
        """
        # requires a copy of the environment to simulate playout
        for _ in range(self.iterations):
            current_state = env_copy.copy()
            current_node = self.node
            visited_nodes = [current_node]

            while not current_state.is_complete():
                current_node = current_node.select_child(current_state)
                visited_nodes.append(current_node)

            result = current_state.evaluate(player)

            for node in visited_nodes[::-1]:
                node.update_stats(result)

    def select_action_and_update(self, T):
        a = self.select_action(T)
        self.root = self.root.children[a]
        return a

    def select_action(self, T):
        # select action with probability of 
        # N(s_0, a) ^ (1 / T) / (sum_b N(s_0, b)) ^ (1 / T)
        # set denominator to 1 if T is 0 for greedy search.
        if T == 0:
            action_child_count_pair = []
            for action, child in self.root.children.items():
                action_child_count_pair.append((action, child.n))

            selected_action = max(action_child_count_pair, key=lambda x : x[1])[0]
            return selected_action

        else:
            r = random.random()
            denominator = self.root.n ** (1 / T)

            action_prob_pair = []
            prob_sum = 0 
            for action, child in self.root.children.items():
                prob_sum += child.n ** (1/T) / denominator
                if prob_sum >= r:
                    return action

class Node:
    def __init__(self, actions):
        self.children = {}
        self.actions = actions
        self.n = 0 # visit count
        self.w = 0 # total action value
        self.q = 0 # mean action value

    def select_child(self, env):
        # select child using PUCT algorithm
        prior = 1 / len(self.actions)
        sqrt_n = self.n ** 0.5

        def get_uct_score(action):
            child = self.children.get(action, None)
            if child is None:
                return CPUCT * sqrt_n * prior
            else:
                return child.q + CPUCT * sqrt_n * prior / (1 + child.n)

        best_a = None
        best_value = -10
        value_action_pair = [(get_uct_score(a), a) for a in self.actions]
        selected_action = max(value_action_pair, key=lambda x : x[0])[1]

        env.playout(selected_action)

        if selected_action not in self.children:
            self.children[selected_action] = Node(env.valid_actions())

        return self.children[selected_action]

    def update_stats(self, score):
        self.n += 1
        self.w += score
        self.q = self.w / self.n

