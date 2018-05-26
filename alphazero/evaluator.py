import numpy as np
import pandas as pd
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch.optim as optim

from .network import TwoLayerNetwork, ThreeLayerNetwork

learning_rate = 0.01

class Evaluator:
    def __init__(self, sizes):
        
        if len(sizes) == 2:
            self.net = TwoLayerNetwork(*sizes)
        elif len(size) == 3:
            self.net = ThreeLayerNetwork(*sizes)
        else:
            raise Error("Unexpected number of layers.")

        print("-- Network Initialized --")
        print(self.net)

        self.optimizer = optim.SGD(
            self.net.parameters(), 
            lr=learning_rate, 
            momentum=0.9,
            weight_decay=0.001 # check later
            )
        self.mseLossF = torch.nn.MSELoss()
        self.ceLossF = torch.nn.CrossEntropyLoss()
    
    def train(self, inputs, prob_labels, value_labels):
        x = Variable(torch.Tensor(inputs).float())
        y1 = Variable(torch.Tensor(prob_labels).float())
        y2 = Variable(torch.Tensor(value_labels).float())

        outputs = self.net(x)
        print(outputs)
        
        loss1 = self.mseLossF(output[:-1], y1)
        loss2 = self.ceLossF(output[-1], y2)
        total_loss = loss1 + loss2

        self.optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

    def evaluate(self, inputs):
        x = Variable(torch.Tensor(inputs).float())
        outputs = self.net(inputs.unsqueeze(0))
        print("NN output", outputs)
        p, v = outputs[:-1].data.numpy(), outputs[-1].data.numpy()
