""" Created by James Parker May 25th
    Defines board for kalaha
"""

class Board:
    def __init__(self, stones, width):
        self.state = ([stones] * width + [0]) * 2
        self.width = width

    # returns the swapped representation of the board
    def get_swap(self): 
        return self.state[self.width + 1:] + self.state[:self.width + 1] 

    def __str__(self):
        str_state = ["{:2}".format(n) for n in self.state]
        
        output = "   |" + \
                "|".join(
                    str_state[self.width + 1: 
                              2*self.width + 1][::-1]) +\
                "|\n" + \
                str_state[-1] + \
                " |" + ("-" * (self.width * 3 - 1)) + "|" + \
                str_state[self.width] + "\n" +\
                "   |" + "|".join(str_state[:self.width]) + "|"

        return output

