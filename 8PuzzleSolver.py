# 8PuzzleSolver.py
# Jasmine Kwong
# SID: 862053634
# An 8 puzzle solver that uses A* search to solve a sliding 8 puzzle
import copy

GOALSTATE = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]
INITIALSTATE = [['1', '2', '3'], ['4', ' ', '6'], ['7', '5', '8']]
DIMENSIONS = 3

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
            print(self._blank, other._blank)
            return False
        for i in range ( DIMENSIONS ):
            for j in range ( DIMENSIONS ):
                print(self._state[i][j], other._state[i][j] )
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
        b = Puzzle(DIMENSIONS, newState)
        return b
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

def main():
    a = Puzzle()
    b = copy.deepcopy(a)
    a.disp()
    b.disp()
    b.moveBlankRight()
    a.disp()
    b.disp()

main()
