"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

import random

from Heuristic_1 import *
from Heuristic_2 import heuristic2
from Node import *
from State import *
import copy

def nextState(finalGrid, node, n, clickTypeH1, strH):

    if clickTypeH1 == 'n':
        clickArr = extendedBoundaryOfState(node.state, n)
    elif clickTypeH1 == 'r':
        clickArr  = unopenedtiles(node.state, n)

    childs = []
    click =[]
    for x in clickArr:
        click = x
        newState = openNewArea(finalGrid, node.state, x[0], x[1], n)

        if strH == 'h1':
            heuristic = heuristic1(finalGrid, newState, n)
        elif strH == 'h2':
            heuristic = heuristic2(finalGrid, newState, n)
        nodenew = Node(newState, heuristic, click)
        childs.append(nodenew)

    childs.sort(key = compareH, reverse=True)

    return childs

def compareH(node):
    return node.heuristic




def openNewArea(finalGrid,currstate, row, col, n):

    state = copy.deepcopy(currstate)
    if finalGrid[row][col] == -1:
        return state
    elif finalGrid[row][col] > 0:
        if not state.boundaryCoord.__contains__([row, col]):
            state.boundaryCoord.append([row, col])
        return state
    elif finalGrid[row][col] == 0:
        if not state.zeroCoord.__contains__([row, col]):
            state.zeroCoord.append([row, col])
        if isValid(row - 1, col, n) and not state.zeroCoord.__contains__([row - 1, col]) and not state.boundaryCoord.__contains__([row - 1, col]):
            state = openNewArea(finalGrid, state, row - 1, col, n)
        if isValid(row + 1, col, n) and not state.zeroCoord.__contains__([row + 1, col]) and not state.boundaryCoord.__contains__([row + 1, col]):
            state = openNewArea(finalGrid, state, row + 1, col, n)
        if isValid(row, col - 1, n) and not state.zeroCoord.__contains__([row, col - 1]) and not state.boundaryCoord.__contains__([row, col - 1]):
            state = openNewArea(finalGrid, state, row, col - 1, n)
        if isValid(row, col + 1, n) and not state.zeroCoord.__contains__([row, col + 1]) and not state.boundaryCoord.__contains__([row, col+1]):
            state = openNewArea(finalGrid, state, row, col + 1, n)
        if isValid(row - 1, col - 1, n) and not state.zeroCoord.__contains__([row - 1, col - 1]) and not state.boundaryCoord.__contains__([row-1, col-1]):
            state = openNewArea(finalGrid, state, row - 1, col - 1, n)
        if isValid(row - 1, col + 1, n) and not state.zeroCoord.__contains__([row - 1, col + 1]) and not state.boundaryCoord.__contains__([row-1, col+1]):
            state = openNewArea(finalGrid, state, row - 1, col + 1, n)
        if isValid(row + 1, col - 1, n) and not state.zeroCoord.__contains__([row + 1, col - 1]) and not state.boundaryCoord.__contains__([row + 1, col-1]):
            state = openNewArea(finalGrid, state, row + 1, col - 1, n)
        if isValid(row + 1, col + 1, n) and not state.zeroCoord.__contains__([row + 1, col + 1]) and not state.boundaryCoord.__contains__([row + 1, col+1]):
            state = openNewArea(finalGrid, state, row + 1, col + 1, n)

        return state


def extendedBoundaryOfState(state, n):

    res = []

    for x in state.boundaryCoord:

        if isValid(x[0] - 1, x[1], n) and ([x[0] - 1, x[1]] not in state.boundaryCoord) and ([x[0] - 1, x[1]] not in state.zeroCoord):
            if not res.__contains__([x[0] - 1, x[1]]):
                res.append([x[0] - 1, x[1]])
        if isValid(x[0] + 1, x[1], n) and ([x[0] + 1, x[1]] not in state.boundaryCoord) and ([x[0] + 1, x[1]] not in state.zeroCoord):
            if not res.__contains__([x[0] + 1, x[1]]):
                res.append([x[0] + 1, x[1]])
        if isValid(x[0], x[1] - 1, n) and ([x[0], x[1] - 1] not in state.boundaryCoord) and ([x[0], x[1] - 1] not in state.zeroCoord):
            if not res.__contains__([x[0], x[1] - 1]):
                res.append([x[0], x[1] - 1])
        if isValid(x[0], x[1] + 1, n) and ([x[0], x[1] + 1] not in state.boundaryCoord) and ([x[0], x[1] + 1] not in state.zeroCoord):
            if not res.__contains__([x[0], x[1] + 1]):
                res.append([x[0], x[1] + 1])
        if isValid(x[0] - 1, x[1] - 1, n) and ([x[0] - 1, x[1] - 1] not in state.boundaryCoord) and ([x[0] - 1, x[1] - 1] not in state.zeroCoord):
            if not res.__contains__([x[0] - 1, x[1] - 1]):
                res.append([x[0] - 1, x[1] - 1])
        if isValid(x[0] - 1, x[1] + 1, n) and ([x[0] - 1, x[1] + 1] not in state.boundaryCoord) and ([x[0] - 1, x[1] + 1] not in state.zeroCoord):
            if not res.__contains__([x[0] - 1, x[1] + 1]):
                res.append([x[0] - 1, x[1] + 1])
        if isValid(x[0] + 1, x[1] + 1, n) and ([x[0] + 1, x[1] + 1] not in state.boundaryCoord) and ([x[0] + 1, x[1] + 1] not in state.zeroCoord):
            if not res.__contains__([x[0] + 1, x[1] + 1]):
                res.append([x[0] + 1, x[1] + 1])
        if isValid(x[0] + 1, x[1] - 1, n) and ([x[0] + 1, x[1] - 1] not in state.boundaryCoord) and ([x[0] + 1, x[1] - 1] not in state.zeroCoord):
            if not res.__contains__([x[0] + 1, x[1] - 1]):
                res.append([x[0] + 1, x[1] - 1])

    return res


def unopenedtiles(state, n):
    res = []

    for i in range(n):
        for j in range(n):
            if not state.boundaryCoord.__contains__([i,j]) and not state.zeroCoord.__contains__([i,j]):
                res.append([i,j])
    return res

def isValid(row, col, n):
    if row < 0 or row > n-1:
        return False
    if col < 0 or col > n-1:
        return False
    return True
