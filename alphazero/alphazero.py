### implementation of alphazero by James Parker. May 25th

def AlphaZero:
    @abstractmethod
    def get_action(self, state):
        pass

    @abstractmethod
    def feed_reward(self, reward):
        pass