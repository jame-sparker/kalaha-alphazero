from abc import ABC, abstractmethod

class Agent(ABC):

    @abstractmethod
    def get_action(self, state):
        pass

    @abstractmethod
    def feed_reward(self, reward):
        pass