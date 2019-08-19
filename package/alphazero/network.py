import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable


class TwoLayerNetwork(nn.Module):
    def __init__(self, n_input, n_h1, n_output):
        super(TwoLayerNetwork, self).__init__()
    
        self.h1 = torch.nn.Linear(n_input, n_h1)
        self.out = torch.nn.Linear(n_h1, n_output)

    def forward(self, x):
        
        x = F.relu(self.h1(x))
        x = F.tanh(self.out(x))

        return x


class ThreeLayerNetwork(nn.Module):
    def __init__(self, n_input, n_h1, n_h2, n_output):
        super(ThreeLayerNetwork, self).__init__()
    
        self.h1 = torch.nn.Linear(n_input, n_h1)
        self.h2 = torch.nn.Linear(n_h1, n_h2)
        self.out = torch.nn.Linear(n_h2, n_output)

    def forward(self, x):
        
        x = F.relu(self.h1(x))
        x = F.relu(self.h2(x))
        x = F.tanh(self.out(x))

        return x


class FourLayerNetwork(nn.Module):
    def __init__(self, n_input, n_h1, n_h2, n_h3, n_output):
        super(ThreeLayerNetwork, self).__init__()
    
        self.h1 = torch.nn.Linear(n_input, n_h1)
        self.h2 = torch.nn.Linear(n_h1, n_h2)
        self.h3 = torch.nn.Linear(n_h2, n_h3)
        self.out = torch.nn.Linear(n_h3, n_output)

    def forward(self, x):
        
        x = F.relu(self.h1(x))
        x = F.relu(self.h2(x))
        x = F.relu(self.h3(x))
        x = F.tanh(self.out(x))

        return x