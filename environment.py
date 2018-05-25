from abc import ABC, abstractmethod

class Environment(ABC):
    @abstractmethod
    def playout(self, action):
        pass

    @abstractmethod
    def valid_actions(self):
        pass

    @abstractmethod
    def state(self):
        pass

    @abstractmethod
    def is_complete(self):
        pass

    @abstractmethod
    def winner(self):
        pass
        
    @abstractmethod
    def copy(self):
        pass