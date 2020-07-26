"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

class State:

    def __init__(self, boundaryCoord, zeroCoord):
        self.boundaryCoord = boundaryCoord
        self.zeroCoord = zeroCoord

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "Boundary - " + str(self.boundaryCoord) + " zeros - " + str(self.zeroCoord)