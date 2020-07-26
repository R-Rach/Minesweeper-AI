"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

import random

from Heuristic_1 import heuristic1
from NextState import nextState
from Node import Node
from State import State


def hill_climbing(finalGrid, parentNode, n, clickTypeH1, strH):

    childNodes = nextState(finalGrid, parentNode, n, clickTypeH1, strH)
    print('----branching factor of last move---')
    print(len(childNodes))
    print('-------')
    if childNodes[0].heuristic != childNodes[1].heuristic:
        return childNodes[0]
    else:
        i = 0
        while (i < (len(childNodes) - 1) and childNodes[i].heuristic == childNodes[i + 1].heuristic):
            i += 1
        randomNode = random.randint(0, i)

        return childNodes[randomNode]