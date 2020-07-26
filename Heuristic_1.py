"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

from State import *


def heuristic1(finalGrid, state, n):

    dictNeighbour = {}
    dictValues = {}

    boundaryarr = state.boundaryCoord

    count = 0

    for i in boundaryarr:
        dictNeighbour[coordToNo(i[0],i[1],n)] = tileNeighbour(state,i[0],i[1],n)
        dictValues[coordToNo(i[0],i[1],n)] = finalGrid[i[0]][i[1]]

    keyList = []
    for i in dictNeighbour:
        keyList.append(i)


    for i in keyList:

        if i in dictNeighbour.keys():

            value = dictValues[i]
            tempList = []

            count = count + value

            for j in range(value):
                tempList.append(dictNeighbour[i][j])
            del dictNeighbour[i]
            del dictValues[i]

            for l in tempList:
                for k in keyList:
                    if k in dictNeighbour.keys():
                        if dictNeighbour[k].__contains__(l):
                            dictNeighbour[k].remove(l)
                            dictValues[k] -= 1
                            if dictValues[k] == 0:
                                del dictNeighbour[k]
                                del dictValues[k]

    return count




def tileNeighbour(state,x,y,n):
    res=[]
    if isValid(x - 1, y,n) and ([x-1, y] not in state.boundaryCoord) and ([x-1, y] not in state.zeroCoord):
        res.append(coordToNo(x-1, y, n))
    if isValid(x+1, y,n) and ([x+1, y] not in state.boundaryCoord) and ([x+1, y] not in state.zeroCoord):
        res.append(coordToNo(x+1, y, n))
    if isValid(x, y-1,n) and ([x, y-1] not in state.boundaryCoord) and ([x, y-1] not in state.zeroCoord):
        res.append(coordToNo(x, y-1, n))
    if isValid(x, y+1,n) and ([x, y+1] not in state.boundaryCoord) and ([x, y+1] not in state.zeroCoord):
        res.append(coordToNo(x, y+1, n))
    if isValid(x-1, y-1,n) and ([x-1, y-1] not in state.boundaryCoord) and ([x-1, y-1] not in state.zeroCoord):
        res.append(coordToNo(x-1, y-1, n))
    if isValid(x-1, y+1,n) and ([x-1, y+1] not in state.boundaryCoord) and ([x-1, y+1] not in state.zeroCoord):
        res.append(coordToNo(x-1, y+1, n))
    if isValid(x+1, y+1,n) and ([x+1, y+1] not in state.boundaryCoord) and ([x+1, y+1] not in state.zeroCoord):
        res.append(coordToNo(x+1, y+1, n))
    if isValid(x+1, y-1,n) and ([x+1, y-1] not in state.boundaryCoord) and ([x+1, y-1] not in state.zeroCoord):
        res.append(coordToNo(x+1, y-1, n))
    return res

def isValid(row, col, n):
    if row < 0 or row > n-1:
        return False
    if col < 0 or col > n-1:
        return False
    return True

def coordToNo(x,y,n):
    return x*n + y + 1