""" Created by James Parker May 25th
    Defines board for kalaha
"""

class Board:
    def __init__(self, stones, width):
        self.state = ([stones] * width + [0]) * 2
        self.width = width
        return

    def __str__(self):
        str_state = ["{:2}".format(n) for n in self.state]
        
        output = "   |" + "|".join(str_state[:self.width]) + "|\n"
        output += str_state[self.width] + \
              " |" + ("-" * (self.width * 3 - 1)) + "|" + \
              str_state[-1] + "\n"
        output += "   |" + "|".join(str_state[self.width + 1: 2*self.width + 1]) + "|"

        return output