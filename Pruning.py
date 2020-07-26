"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

from State import State


def pruning(finalGrid, state, n):

    s = state.boundaryCoord
    for i in state.zeroCoord:
        s.append(i)

    s = sorted(s, key = lambda k:[k[0],k[1]])
    grid = [[0 for x in range(n)] for y in range(n)]

    for i in s:
        grid[i[0]][i[1]] = [i[0],i[1]]

    encount = 0

    for x in range(n):

        for i in range(n):
            if grid[x][i] == 0 and encount == 0:
                continue
            if grid[x][i] != 0:
                encount += 1
                continue
            if grid[x][i] == 0 and encount>0:
                temp = i+1
                for p in range(temp,n):
                    grid[x][p] = 0
                break

        encount = 0

    encount =0

    for y in range(n):

        for i in range(n):
            if grid[i][y] == 0 and encount == 0:
                continue
            if grid[i][y] != 0:
                encount += 1
                continue
            if grid[i][y] == 0 and encount > 0:
                temp = i+1
                for p in range(temp,n):
                    grid[p][y] = 0
                break
        encount = 0


    arr = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                arr.append(grid[i][j])


    boundaryarr = []
    zeroarr = []
    for i in arr:
        if finalGrid[i[0]][i[1]] == 0:
            zeroarr.append(i)
        else:
            boundaryarr.append(i)

    newState = State(boundaryarr,zeroarr)

    return newState