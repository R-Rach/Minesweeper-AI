"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

from tkinter import *

from Heuristic_1 import heuristic1
from Heuristic_2 import heuristic2
from HillClimbing import hill_climbing
from MineGenerator import *
from Node import Node
from Pruning import pruning
from State import State


def iniGrid():
    global n
    global m
    n = int(e1.get())
    m = int(e2.get())

    global mineCoord
    mineCoord = mineToXYcoord(mineGenerator(n, m), n)

    windowRoomEnvGUI = Tk()
    windowRoomEnvGUI.title('Initial Room Environment')

    global finalGrid
    finalGrid = [[100 for x in range(n)] for y in range(n)]

    mineGrid = [[Label(windowRoomEnvGUI, width=2, height=1, borderwidth=1, relief='solid') for x in range(n)] for y in range(n)]

    for p in range(0, n):
        for q in range(0, n):
            mineGrid[p][q].grid(row=p, column=q)

    for x in mineCoord:
        finalGrid[x[0]][x[1]] = -1
        mineGrid[x[0]][x[1]].config(bg='red', text = "-1")

    for i in range(n):
        for j in range(n):
            finalGrid[i][j] = countAdjMines(mineCoord, i, j, n)
            mineGrid[i][j].config(text = finalGrid[i][j])

    windowRoomEnvGUI.mainloop()



def hillCHutility(clickType, H):


    global startnode
    x = hill_climbing(finalGrid, startnode, n, clickType, H)
    print('----heuristic value of last move---')
    print(x.heuristic)
    print('-------')
    startnode = x

    clicksArray.append(startnode.click)

    if (len(startnode.state.boundaryCoord) + len(startnode.state.zeroCoord)) == (n * n - m):

        for x in startnode.state.boundaryCoord:
            mineGrid[x[0]][x[1]].config(bg='green', text=finalGrid[x[0]][x[1]])
        for x in startnode.state.zeroCoord:
            mineGrid[x[0]][x[1]].config(bg='green', text=finalGrid[x[0]][x[1]])
        for x in clicksArray:
            mineGrid[x[0]][x[1]].config(bg='blue', text=finalGrid[x[0]][x[1]])

        won = Tk()
        wonlable = Label(won, text='WON!!!')
        wonlable.pack()
        b.config(state=DISABLED)
        won.mainloop()

        return

    if(finalGrid[startnode.click[0]][startnode.click[1]] == -1):
        mineGrid[startnode.click[0]][startnode.click[1]].config(bg='red')
        lost = Tk()
        l1 = Label(lost, text='MINE WAS CLICKED, close all window and again click from starting')
        l1.pack()
        b.config(state = DISABLED)
        lost.mainloop()
        return



    for x in startnode.state.boundaryCoord:
        mineGrid[x[0]][x[1]].config(bg='green', text = finalGrid[x[0]][x[1]])
    for x in startnode.state.zeroCoord:
        mineGrid[x[0]][x[1]].config(bg='green', text=finalGrid[x[0]][x[1]])
    for x in clicksArray:
        mineGrid[x[0]][x[1]].config(bg = 'blue', text = finalGrid[x[0]][x[1]])


def forH1():
    global clickType
    clickType = str(b3.get())
    hillCHutility(clickType, 'h1')


def forH2():
    global clickType
    clickType = str(b3.get())
    hillCHutility(clickType, 'h2')


def hillCH(args):
    randNo = random.randrange(1,n*n+1,1)  
    if randNo % n == 0:
        coord = [randNo // n - 1, n - 1]
    else:
        coord = [randNo // n, randNo % n - 1]

    global clicksArray
    clicksArray = []
    clicksArray.append(coord)

    global gameGui
    gameGui = Tk()
    gameGui.title('game')

    global mineGrid
    mineGrid = [[Label(gameGui, width=2, height=1, borderwidth=1, relief='solid') for x in range(n)] for y in
                range(n)]

    for p in range(0, n):
        for q in range(0, n):
            mineGrid[p][q].grid(row=p, column=q)

    openArr = []
    zeroarr = []
    extra = []

    openArr, zeroarr = openShape(openArr, zeroarr, extra, finalGrid, coord[0], coord[1], n)

    firstState = State(openArr, zeroarr)
    firstState = pruning(finalGrid, firstState, n)
    openArr = firstState.boundaryCoord
    zeroarr = firstState.zeroCoord
    if len(zeroarr) != 0:
        tempRandom = random.randint(0,len(zeroarr)-1)
        clicksArray[0] = zeroarr[tempRandom]
    firstH = heuristic1(finalGrid, firstState, n)
    print('----heuristic value of last move---')
    print(firstH)
    print('-------')
    x = Node(firstState, firstH, clicksArray[0])
    global startnode
    startnode = x

    if len(openArr) == 0:
        mineGrid[coord[0]][coord[1]].config(bg='red')
        lost = Tk()
        l1 = Label(lost, text='MINE WAS CLICKED, close all window and again click from Starting')
        l1.pack()
        lost.mainloop()
        return

    for x in openArr:
        mineGrid[x[0]][x[1]].config(bg='green', text = finalGrid[x[0]][x[1]])
    for x in zeroarr:
        mineGrid[x[0]][x[1]].config(bg='green', text=finalGrid[x[0]][x[1]])
    for x in clicksArray:
        mineGrid[x[0]][x[1]].config(bg = 'blue')

    if args == 'h1':
        global b
        b = Button(gameGui, text = 'Next Move', command = forH1)
        b.pack()
        b.grid(row=p+1, columnspan = n)

    elif args == 'h2':
        b = Button(gameGui, text='Next Move', command=forH2)
        b.pack()
        b.grid(row=p + 1, columnspan=n)

    gameGui.mainloop()


def methodTransfer():
    hillCH('h1')


def methodTransfer2():
    hillCH('h2')


if __name__ == '__main__':
    global startnode

    window = Tk()
    window.title('AI Assignment 2')
    window.geometry('800x700')

    b1 = Button(window, width=29, text='Option 1 - Initial Mine Environment', command=iniGrid)
    b1.pack()
    b1.place(x=290, y=10)

    b2 = Button(window, width=15, height =4, text='Option 2 - Hill Climbing with H1', command=methodTransfer)
    b2.pack()
    b2.place(x=250, y=50)

    b3 = Entry(window, width=15)
    b3.insert(END, 'Enter n/r')
    b3.pack()
    b3.place(x=450, y=110)

    b4 = Button(window, width=15, height =4, text='Option 3 - Hill Climbing with H2', command=methodTransfer2)
    b4.pack()
    b4.place(x=250, y=120)

    e1 = Entry(window, width=35)
    e1.insert(END, 'Erase it and enter integer N value')
    e1.pack()
    e1.place(x=270, y=210)

    e2 = Entry(window, width=35)
    e2.insert(END, 'Erase it and enter M value')
    e2.pack()
    e2.place(x=270, y=240)

    l1 = Label(window, relief=GROOVE, wraplength =900, justify =LEFT, text = '***********HOW TO USE***********\n1.  In edit box -\"Erase it and enter integer N value\"-- Enter square matrix size\n2.  in edit box-\"Erase it and enter M value\"--- Enter number of mines\n3.  In edit box-\"Enter n/r\"-- Enter if AI agent has to check and click on current state neighbouring(n) tiles or\nanwhere randomly(r) on unopned tile\n4. Enter all the values and click on Option 1, it\'ll generate mine environment\n5.  Then chose any of the Option 2 or 3\n\n###WARNING###\n--Clicking on Option 1 again and again will generate new environment,\nonly the latest environment generated will be take by option 2 and 3.\n--Once any of option 2 or 3 is clicked, do\'nt change values of N and M\n--If want to explore option 2 and 3 for neighbour or random clicks (4 combination) for same mine environment\nDo like this\n------enter N, M values and specify n/r, then click on option 1\n------then click on option 2 and use next move to go along till end until next move button is diabled\n------then click on option 3 and use next move till end until next move button is diabled,\n------then change the value ONLY of n/r and repeat')
    l1.pack()
    l1.place(x=53,y=280)

    window.mainloop()




