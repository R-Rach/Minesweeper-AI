"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

def heuristic2(finalgrid, state, n):
    h = 0
    h = len(state.boundaryCoord) + len(state.zeroCoord)
    return h