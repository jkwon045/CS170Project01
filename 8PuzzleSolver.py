# 8PuzzleSolver.py
# Jasmine Kwong
# SID: 862053634
# An 8 puzzle solver that uses A* search to solve a sliding 8 puzzle
import copy

GOALSTATE = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]
INITIALSTATE = [['8', '7', '1'], ['6', ' ', '2'], ['5', '4', '3']]
EXPANDEDSTATES = list()
NUMEXPANSIONS = 0
MAXQUEUESIZE = 0
DIMENSIONS = 3
EXPANDFLAG = False

#A class to define a point on the puzzle
class Point:
    _x = 0
    _y = 0
    def __init__ ( self, x = 0, y = 0 ):
        self._x = x
        self._y = y
    def set( self, x = None, y = None ):
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
    def getX ( self ):
        return self._x
    def getY ( self ):
        return self._y
    def disp ( self ):
        print( self._x, self._y )

#A class to define the 8 puzzle itself, or any arbitrary puzzle if needed
class Puzzle:
    #init should be a 2d array 
    def __init__( self, dim = DIMENSIONS, init = INITIALSTATE ):
        self._state = list(init)
        for i in range(dim):
            for j in range(dim):
                if ( init[i][j] == ' ' ):
                    self._blank = Point(i, j)
    #Checks if one puzzle state is equal to another
    def __eq__( self, other ):
        if ( self._blank != other._blank ):
            return False
        for i in range ( DIMENSIONS ):
            for j in range ( DIMENSIONS ):
                if ( self._state[i][j] != other._state[i][j] ):
                    return False
        return True
    def getState( self ):
        return self._state
    def getBlank( self ):
        return (self._blank.getX(), self._blank.getY())
    #Moves the location of the blank left
    def moveBlankLeft( self ):
        cX = self._blank.getX() #the current X
        cY = self._blank.getY() #the current Y
        newState = list(self._state)
        if ( cY > 0 ):
            newState[cX][cY], newState[cX][cY-1] = newState[cX][cY-1], newState[cX][cY]
            self._blank.set( x = cX, y = (cY - 1 ))
    #Moves the location of the blank Right
    def moveBlankRight( self ):
        cX = self._blank.getX() #the current X
        cY = self._blank.getY() #the current Y
        newState = list(self._state)
        if ( cY < DIMENSIONS-1 ):
            newState[cX][cY], newState[cX][cY+1] = newState[cX][cY+1], newState[cX][cY]
            self._blank.set( y = (cY + 1) )
    def moveBlankUp( self ):
        cX = self._blank.getX() #the current X
        cY = self._blank.getY() #the current Y
        if ( cX > 0 ):
            self._state[cX][cY], self._state[cX-1][cY] = self._state[cX-1][cY], self._state[cX][cY]
            self._blank.set( x = (cX - 1) )
    def moveBlankDown( self ):
        cX = self._blank.getX() #the current X
        cY = self._blank.getY() #the current Y
        if ( cX < DIMENSIONS-1 ):
            self._state[cX][cY], self._state[cX+1][cY] = self._state[cX+1][cY], self._state[cX][cY]
            self._blank.set( x = (cX + 1) )
    def disp( self ):
        for i in self._state:
            print(i, '\n')

#use copy.deepcopy in order to create new instances of class :)
class Node:
    def __init__(self, state, g_n = 0):
        self._state = copy.deepcopy(state)
        self._g_n = g_n
        self._f_n = g_n

    def __eq__ ( self, other ):
        return self._state == other._state

    def getState(self):
        return self._state.getState()

    def getNumMoves(self):
        return self._g_n

    def getWeight(self):
        return self._f_n

    def setWeight(self, val):
        self._f_n = val
    
    def setPrevState( self, state ):
        self._prevState = copy.deepcopy(state)

    def moveBlankRight( self ):
        self._state.moveBlankRight()
        self._g_n += 1
        return self

    def moveBlankLeft( self ):
        self._state.moveBlankLeft()
        self._g_n += 1
        return self

    def moveBlankUp( self ):
        self._state.moveBlankUp()
        self._g_n += 1
        return self

    def moveBlankDown(self ):
        self._state.moveBlankDown()
        self._g_n += 1
        return self

    def goalTest( self ):
        return self._state.getState() == GOALSTATE

    def disp( self ):
        self._state.disp()

def hasBeenExpanded(node):
    for i in range(len(EXPANDEDSTATES)):
        if ( node.getState() == EXPANDEDSTATES[i].getState() ):
            return True
    EXPANDEDSTATES.append(copy.deepcopy(node))
    return False

def dequeue( nodesList ):
    minWeight = nodesList[0].getWeight()
    minloc = 0
    for i in range ( 1, len( nodesList )):
        if( nodesList[i].getWeight() < minWeight ):
            minloc = i
            mingn = nodesList[i].getNumMoves()
    return minloc
        
def expand( node ):
    possibleMoves = list()

    if(EXPANDFLAG):
        print("\nNow we are expanding: ")
        node.disp()
        print("It has a value of g(n): ", node.getNumMoves(), "and h(n): ", node.getWeight() - node.getNumMoves())

    global NUMEXPANSIONS

    up = copy.deepcopy(node).moveBlankUp()
    down = copy.deepcopy(node).moveBlankDown()
    left = copy.deepcopy(node).moveBlankLeft()
    right = copy.deepcopy(node).moveBlankRight()

    possibleMoves.append(up)
    possibleMoves.append(down)
    possibleMoves.append(left)
    possibleMoves.append(right)

    indexToRemove = list()
    for i in range(len(possibleMoves)):
        appended = False
        if (possibleMoves[i].getState() == node.getState()):
            indexToRemove.append(i)
        elif ( hasBeenExpanded(possibleMoves[i]) ):
            indexToRemove.append(i)
        possibleMoves[i].setPrevState(node.getState())
        
    #sort indices and reverse in order to remove all values
    if(len(indexToRemove) > 0):
        indexToRemove.reverse()
        for i in range( len( indexToRemove ) ):
            del possibleMoves[indexToRemove[i]]

    if(len(possibleMoves) > 0):
        NUMEXPANSIONS+=1
    return possibleMoves

def queueingFunction( nodesToEnqueue, index, nodesList , heurestic ):
    global MAXQUEUESIZE
    if ( nodesList is None ):
        nodesList = list()
    for i in range(len(nodesToEnqueue)):
        nodesToEnqueue[i].setWeight(nodesToEnqueue[i].getNumMoves() + heurestic(nodesToEnqueue[i]))
        nodesList.insert(index, nodesToEnqueue[i])
        index+=1

    if( len(nodesList) > MAXQUEUESIZE ):
        MAXQUEUESIZE = len(nodesList)
    return nodesList

#queueing function is the heurestic
def generalSearch( problem, heurestic):
    nodes = list()
    nodes.append(Node(state = problem))
    while( True ):
        if( len(nodes) == 0 ):
            print('fail')
            return None
        index = dequeue(nodes)
        a = copy.deepcopy(nodes.pop(index))
        if ( a.goalTest() ):
            print("Goal!")
            return a
        expanded = expand(a)
        nodes = queueingFunction(expanded, index, nodes, heurestic)
        
def uniformSearchHeuristic( problem ):
    return 0
        
def misplacedTilesHeuristic( problem ):
    misplacedTiles = 0
    check = problem.getState()

    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            if ( check[i][j] != GOALSTATE[i][j] and GOALSTATE[i][j] != ' '):
                    misplacedTiles+=1
 
    return misplacedTiles
            
def absVal( a ):
    if( a < 0 ):
        a *= -1
    return a

def manhattanDistanceHeuristic( problem ):
    totalDistance = 0
    check = problem.getState()

    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):            
            if( check[i][j] != ' ' ):
                goalX = (int(check[i][j])-1) % DIMENSIONS
                goalY = (int(check[i][j])-1) // DIMENSIONS

                distX = absVal(goalX - j)
                distY = absVal(goalY - i)

                totalDistance+= (distX + distY)
    
    return absVal(totalDistance)

def choosePuzzle():
    response = -1 
    while( response > 2 or response < 0 ):
        response = int(input("Press 1 to use the default puzzle, or 2 to create your own\n"))
        if( response > 2 or response < 0):
            print(response, " is an invalid option\n")

    if( response == 1 ):
        return Puzzle()
    else:
        inputs = list()

        print("Please use spaces to separate each value, and use 0 as your blank")
        inputs.append(input("Please input the first row\t"))
        inputs.append(input("Please input the second row\t"))
        inputs.append(input("Please input the third row\t"))

        puzzInit = list()
        for i in inputs:
            check = i.split()
            if ( '0' in check ):
                blankLoc = check.index('0')
                check[blankLoc] = ' '
            puzzInit.append(check)
        
        return Puzzle( DIMENSIONS, puzzInit )

def chooseHeuristic():
    print("Please choose your heuristic")
    print(" 1. Uniform Search Hueristic (WARNING: MAY TAKE A LONG TIME)")
    print(" 2. Misplaced Tiles Heuristic")
    print(" 3. Manhattan Distance Heuristic")

    response = -1
    while(response < 0 or response > 3):
        response = int(input("Please enter your choice: "))
        if( response > 3 or response < 0):
            print(response, " is an invalid option\n")

    if (response == 1):
        return uniformSearchHeuristic
    elif (response == 2):
        return misplacedTilesHeuristic
    else:
        return manhattanDistanceHeuristic

def setExpand():
    val = int(input("Enter 1 to display the node that is expanding, otherwise press 2\n"))
    global EXPANDFLAG
    if( val == 1 ):
        EXPANDFLAG = True
    else:
        EXPANDFLAG = False

def main():
    problem = choosePuzzle()
    h = chooseHeuristic()
    setExpand()
    a = generalSearch(problem, h)

    if( a is not None):
        print("\nTo solve this problem, the search algorithm expanded nodes", NUMEXPANSIONS, "times")
        print("The max number of nodes in the queue at any time was", MAXQUEUESIZE )
        print("The depth of the goal node was", a.getNumMoves())
main()
