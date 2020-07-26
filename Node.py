"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

class Node:

    def __init__(self, state, heuristic,click):
        self.state = state
        self.heuristic = heuristic
        self.click = click

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "State - " + str(self.state) + " heuristic - " + str(self.heuristic) + " click - " + str(self.click)