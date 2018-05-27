from abc import ABC, abstractmethod
P1 = 1
P2 = -1

class Environment(ABC):

    @abstractmethod
    def get_turn(self):
        pass

    @abstractmethod
    def get_action_size(self):
        pass

    @abstractmethod
    def playout(self, action):
        pass

    @abstractmethod
    def valid_actions(self):
        pass

    @abstractmethod
    def get_state_size(self):
        pass
        
    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def is_complete(self):
        pass

    @abstractmethod
    def winner(self):
        pass
        
    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def reset(self):
        pass