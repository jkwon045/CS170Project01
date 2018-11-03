# 8PuzzleSolver.py
# Jasmine Kwong
# SID: 862053634
# An 8 puzzle solver that uses A* search to solve a sliding 8 puzzle

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
    _state = list()
    _blank = Point(-1, -1)
    #init should be a 2d array 
    def __init__( self, dim = DIMENSIONS, init = None ):
        if( init == None):
            init = INITIALSTATE
        for i in range(dim):
            self._state.append(init[i])
        for i in range(dim):
            for j in range(dim):
                if ( init[i][j] == ' ' ):
                    self._blank.set( x = i, y = j )
    #Checks if one puzzle state is equal to another
    def __eq__( self, other ):
        if ( self._blank != other._blank ):
            return False
        for i in range ( DIMENSIONS ):
            for j in range ( DIMENSIONS ):
                if ( self._state[i][j] != other._state[i][j] ):
                    return False
        return True
    #Moves the location of the blank left
    def moveBlankLeft( self ):
        cX = self._blank.getX() #the current X
        cY = self._blank.getY() #the current Y
        if ( cY != 0 ):
            self._state[cX][cY], self._state[cX][cY-1] = self._state[cX][cY-1], self._state[cX][cY]
            self._blank.set( y = (cY - 1 ))
    #Moves the location of the blank Right
    def moveBlankRight( self ):
        cX = self._blank.getX() #the current X
        cY = self._blank.getY() #the current Y
        if ( cY != DIMENSIONS-1 ):
            self._state[cX][cY], self._state[cX][cY+1] = self._state[cX][cY+1], self._state[cX][cY]
            self._blank.set( y = (cY + 1) )
    def moveBlankUp( self ):
        cX = self._blank.getX() #the current X
        cY = self._blank.getY() #the current Y
        if ( cX != 0 ):
            self._state[cX][cY], self._state[cX-1][cY] = self._state[cX-1][cY], self._state[cX][cY]
            self._blank.set( x = (cX - 1) )
    def moveBlankDown( self ):
        cX = self._blank.getX() #the current X
        cY = self._blank.getY() #the current Y
        if ( cX != DIMENSIONS-1 ):
            self._state[cX][cY], self._state[cX+1][cY] = self._state[cX+1][cY], self._state[cX][cY]
            self._blank.set( x = (cX + 1) )
    def disp( self ):
        for i in self._state:
            print(i, '\n')

def main():
    a = Puzzle()
    a.disp()
    a.moveBlankUp()
    a.disp()
    a.moveBlankDown()
    a.disp()
    a.moveBlankLeft()
    a.disp()
    a.moveBlankRight()
    a.disp()
    b = Puzzle()
    print ( a == b )

main()
