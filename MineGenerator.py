"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

import random

def mineGenerator(n, m):
    minePos = random.sample(range(1,(n*n)),m)
    return minePos

def mineToXYcoord(minePos, n):
    mineXY = []
    for x in minePos:
        if x % n == 0:
            mineXY.append([x // n - 1, n - 1])
        else:
            mineXY.append([x // n, x % n - 1])
    return mineXY

def isValid(row, col, n):
    if row < 0 or row > n-1:
        return False
    if col < 0 or col > n-1:
        return False
    return True

def countAdjMines(minePos, row, col, n):
    count = 0
    if minePos.__contains__([row,col]):
        return -1
    if isValid(row-1, col, n):
        if minePos.__contains__([row-1,col]):
            count += 1
    if isValid(row+1, col, n):
        if minePos.__contains__([row+1,col]):
            count += 1
    if isValid(row, col-1, n):
        if minePos.__contains__([row,col-1]):
            count += 1
    if isValid(row, col+1, n):
        if minePos.__contains__([row,col+1]):
            count += 1
    if isValid(row-1, col-1, n):
        if minePos.__contains__([row-1,col-1]):
            count += 1
    if isValid(row-1, col+1, n):
        if minePos.__contains__([row-1,col+1]):
            count += 1
    if isValid(row+1, col-1, n):
        if minePos.__contains__([row+1,col-1]):
            count += 1
    if isValid(row+1, col+1, n):
        if minePos.__contains__([row+1,col+1]):
            count += 1

    return count

def openShape(arr, zeroarr, visitarr, finalGrid, row, col, n):

    if finalGrid[row][col] == -1:
        return arr, zeroarr
    elif finalGrid[row][col] > 0:
        if not arr.__contains__([row, col]):
            arr.append([row, col])
        return arr, zeroarr
    elif finalGrid[row][col] == 0:
        if not zeroarr.__contains__([row,col]):
            zeroarr.append([row,col])
        if isValid(row - 1, col, n) and not zeroarr.__contains__([row-1,col]):
            arr, zeroarr = openShape(arr, zeroarr,visitarr, finalGrid, row-1, col,n)
        if isValid(row + 1, col, n) and not zeroarr.__contains__([row+1,col]):
            arr, zeroarr = openShape(arr, zeroarr,visitarr, finalGrid, row+1, col,n)
        if isValid(row, col - 1, n) and not zeroarr.__contains__([row,col-1]):
            arr, zeroarr = openShape(arr, zeroarr,visitarr, finalGrid, row, col-1,n)
        if isValid(row, col + 1, n) and not zeroarr.__contains__([row,col+1]):
            arr, zeroarr = openShape(arr,zeroarr,visitarr, finalGrid, row, col+1,n)
        if isValid(row - 1, col - 1, n) and not zeroarr.__contains__([row-1,col-1]):
            arr, zeroarr = openShape(arr,zeroarr,visitarr, finalGrid, row-1, col-1,n)
        if isValid(row - 1, col + 1, n) and not zeroarr.__contains__([row-1,col+1]):
            arr, zeroarr = openShape(arr, zeroarr,visitarr, finalGrid, row-1, col+1,n)
        if isValid(row + 1, col - 1, n) and not zeroarr.__contains__([row+1,col-1]):
            arr, zeroarr = openShape(arr,zeroarr,visitarr, finalGrid, row+1, col-1,n)
        if isValid(row + 1, col + 1, n) and not zeroarr.__contains__([row+1,col+1]):
            arr, zeroarr = openShape(arr, zeroarr,visitarr, finalGrid, row+1, col+1,n)

    return arr,zeroarr