import numpy as np
import pandas as pd
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch.optim as optim
from copy import deepcopy

from .network import TwoLayerNetwork, ThreeLayerNetwork

from . import LEARNING_RATE

class Evaluator:
    def __init__(self, sizes=None):
        if sizes is not None:
            if len(sizes) == 3:
                self.net = TwoLayerNetwork(*sizes)
            elif len(sizes) == 4:
                self.net = ThreeLayerNetwork(*sizes)
            elif len(sizes) == 5:
                self.net = FourLayerNetwork(*sizes)
            else:
                raise Error("Unexpected number of layers.")

            self.optimizer = optim.SGD(
                self.net.parameters(), 
                lr=LEARNING_RATE, 
                momentum=0.9,
                weight_decay=0.0001
                )
        self.mseLossF = torch.nn.MSELoss()
        self.ceLossF = torch.nn.CrossEntropyLoss()
        # self.ceLossF = torch.nn.NLLLoss()

    
    def train(self, inputs, prob_labels, value_labels):
        x = Variable(torch.Tensor(inputs).float())
        y1 = Variable(torch.Tensor(prob_labels).float())
        y2 = Variable(torch.Tensor(value_labels.T[0]).long())

        outputs = self.net(x)
        p = torch.stack((outputs[:, -1], 1 - outputs[:, -1]), 1)
        loss1 = self.ceLossF(p, y2)
        print("--state--")
        print(inputs[0])
        print("--value--")
        print(p[0].data)
        print(y2[0].data)
        loss2 = self.mseLossF(outputs[:,:-1], y1)
        print("--probs--")
        print(outputs[0,:-1].data)
        print(y1[0].data)
        total_loss = loss1 + loss2
        print("Total Loss: ", total_loss.data)

        self.optimizer.zero_grad()
        total_loss.backward()
        self.optimizer.step()

    def evaluate(self, inputs):
        x = Variable(torch.Tensor(inputs).unsqueeze(0).float())
        outputs = self.net(x)
        out = outputs.data.numpy()[0]

        p, v = out[:-1], out[-1]
        return p, v

    def copy(self):
        e = Evaluator()
        e.net = deepcopy(self.net)
        e.optimizer = optim.SGD(
                e.net.parameters(), 
                lr=LEARNING_RATE, 
                momentum=0.9,
                weight_decay=0.001
                )
        return e
