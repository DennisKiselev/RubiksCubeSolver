import random #For scramble generation
import statistics #For meanMoves function

#Resets the cube to its default state.
def cubeReset():
    #The cube needs to be modified throughout all the functions, so it must be global.
    global greenFace,blueFace,redFace,orangeFace,whiteFace,yellowFace
    #The cube is represented in six 3x3 arrays which represents each face.
    #The default state is a single solid colour.
    greenFace = [["green","green","green"],["green","green","green"],["green","green","green"]]
    blueFace = [["blue","blue","blue"],["blue","blue","blue"],["blue","blue","blue"]]
    redFace = [["red","red","red"],["red","red","red"],["red","red","red"]]
    orangeFace = [["orange","orange","orange"],["orange","orange","orange"],["orange","orange","orange"]]
    whiteFace = [["white","white","white"],["white","white","white"],["white","white","white"]]
    yellowFace = [["yellow","yellow","yellow"],["yellow","yellow","yellow"],["yellow","yellow","yellow"]]

#Outputs the current state of the cube as text
def printCube():
    print('greenFace =',greenFace)
    print('blueFace =',blueFace)
    print('redFace =',redFace)
    print('orangeFace =',orangeFace)
    print('whiteFace =',whiteFace)
    print('yellowFace =',yellowFace)

#Generates a random 20 move length scramble.
def scrambleGen():
    #This dictionary contains every possible move and the name of the function it corresponds to.
    moveList = {'U':U,'D':D,'F':F,'B':B,'R':R,'L':L,'U2':U2,'D2':D2,'F2':F2,'B2':B2,'R2':R2,'L2':L2,"U'":UP,"D'":DP,"F'":FP,"B'":BP,"R'":RP,"L'":LP}
    scramble = []
    for i in range(20):
        #A random move is selected from the list of the keys of the moveList dictionary.
        current = random.choice(list(moveList))
        try:
            #Whenever a move has the same base as either of the two before it, a new one is generated until a valid one is found.
            while current[0] == scramble[i-1][0] or current[0] == scramble[i-2][0]:
                current = random.choice(list(moveList))
        except:
            #The except is necessary for when the first move is checked, as there is no move before it to compare it to.
            pass
        #The move is then added to the scramble.
        scramble.append(current)
    #The complete scramble is outputted to the user.
    print(" ".join(scramble))
    #The cube needs to be in its default state before being scrambled.
    cubeReset()
    #The dictionary is used to cycle through the scramble and perform the function corresponding to each move.
    for move in scramble:
        moveList[move]()

#Receives a custom scramble input and performs it.
def scrambleInput():
    #This dictionary contains every possible move and the name of the function it corresponds to.
    moveList = {'U':U,'D':D,'F':F,'B':B,'R':R,'L':L,'U2':U2,'D2':D2,'F2':F2,'B2':B2,'R2':R2,'L2':L2,"U'":UP,"D'":DP,"F'":FP,"B'":BP,"R'":RP,"L'":LP}
    scramble = input('Input your custom scramble: ')
    #The input is split into a list to be performed.
    scramble = scramble.split()
    #The cube needs to be in its default state before being scrambled.
    cubeReset()
    #The dictionary is used to cycle through the scramble and perform the function corresponding to each move.
    for move in scramble:
        moveList[move]()

#Performs a U move.
def U():
    #The state of the cube is copied to temporary lists which remain unchanged for the duration of the function.
    #This is needed because otherwise the original colours would be written over and lost, while still being needed.
    tempGreenFace = [i[:] for i in greenFace]
    tempBlueFace = [i[:] for i in blueFace]
    tempRedFace = [i[:] for i in redFace]
    tempOrangeFace = [i[:] for i in orangeFace]
    tempYellowFace = [i[:] for i in yellowFace]
    #This list of transformations replicates what turning the U face would do to a cube.
    greenFace[0][0] = tempOrangeFace[0][0]
    greenFace[0][1] = tempOrangeFace[0][1]
    greenFace[0][2] = tempOrangeFace[0][2]
    redFace[0][0] = tempGreenFace[0][0]
    redFace[0][1] = tempGreenFace[0][1]
    redFace[0][2] = tempGreenFace[0][2]
    blueFace[0][0] = tempRedFace[0][0]
    blueFace[0][1] = tempRedFace[0][1]
    blueFace[0][2] = tempRedFace[0][2]
    orangeFace[0][0] = tempBlueFace[0][0]
    orangeFace[0][1] = tempBlueFace[0][1]
    orangeFace[0][2] = tempBlueFace[0][2]
    yellowFace[0][0] = tempYellowFace[2][0]
    yellowFace[0][1] = tempYellowFace[1][0]
    yellowFace[0][2] = tempYellowFace[0][0]
    yellowFace[1][2] = tempYellowFace[0][1]
    yellowFace[2][2] = tempYellowFace[0][2]
    yellowFace[2][1] = tempYellowFace[1][2]
    yellowFace[2][0] = tempYellowFace[2][2]
    yellowFace[1][0] = tempYellowFace[2][1]

#Performs a U2 move.
def U2():
    #U2 is equivalent to 2 U moves.
    [U() for i in range(2)]

#Performs a U' move.
def UP():
    #U' is equivalent to 3 U moves.
    [U() for i in range(3)]

#Performs a D move.
def D():
    tempGreenFace = [i[:] for i in greenFace]
    tempBlueFace = [i[:] for i in blueFace]
    tempRedFace = [i[:] for i in redFace]
    tempOrangeFace = [i[:] for i in orangeFace]
    tempWhiteFace = [i[:] for i in whiteFace]
    greenFace[2][0] = tempRedFace[2][0]
    greenFace[2][1] = tempRedFace[2][1]
    greenFace[2][2] = tempRedFace[2][2]
    redFace[2][0] = tempBlueFace[2][0]
    redFace[2][1] = tempBlueFace[2][1]
    redFace[2][2] = tempBlueFace[2][2]
    blueFace[2][0] = tempOrangeFace[2][0]
    blueFace[2][1] = tempOrangeFace[2][1]
    blueFace[2][2] = tempOrangeFace[2][2]
    orangeFace[2][0] = tempGreenFace[2][0]
    orangeFace[2][1] = tempGreenFace[2][1]
    orangeFace[2][2] = tempGreenFace[2][2]
    whiteFace[0][0] = tempWhiteFace[2][0]
    whiteFace[0][1] = tempWhiteFace[1][0]
    whiteFace[0][2] = tempWhiteFace[0][0]
    whiteFace[1][2] = tempWhiteFace[0][1]
    whiteFace[2][2] = tempWhiteFace[0][2]
    whiteFace[2][1] = tempWhiteFace[1][2]
    whiteFace[2][0] = tempWhiteFace[2][2]
    whiteFace[1][0] = tempWhiteFace[2][1]

#Performs a D2 move.
def D2():
    [D() for i in range(2)]

#Performs a D' move.
def DP():
    [D() for i in range(3)]

#Performs an F move.
def F():
    tempGreenFace = [i[:] for i in greenFace]
    tempRedFace = [i[:] for i in redFace]
    tempOrangeFace = [i[:] for i in orangeFace]
    tempWhiteFace = [i[:] for i in whiteFace]
    tempYellowFace = [i[:] for i in yellowFace]
    yellowFace[2][0] = tempRedFace[2][2]
    yellowFace[2][1] = tempRedFace[1][2]
    yellowFace[2][2] = tempRedFace[0][2]
    redFace[0][2] = tempWhiteFace[0][0]
    redFace[1][2] = tempWhiteFace[0][1]
    redFace[2][2] = tempWhiteFace[0][2]
    whiteFace[0][0] = tempOrangeFace[2][0]
    whiteFace[0][1] = tempOrangeFace[1][0]
    whiteFace[0][2] = tempOrangeFace[0][0]
    orangeFace[0][0] = tempYellowFace[2][0]
    orangeFace[1][0] = tempYellowFace[2][1]
    orangeFace[2][0] = tempYellowFace[2][2]
    greenFace[0][0] = tempGreenFace[2][0]
    greenFace[0][1] = tempGreenFace[1][0]
    greenFace[0][2] = tempGreenFace[0][0]
    greenFace[1][2] = tempGreenFace[0][1]
    greenFace[2][2] = tempGreenFace[0][2]
    greenFace[2][1] = tempGreenFace[1][2]
    greenFace[2][0] = tempGreenFace[2][2]
    greenFace[1][0] = tempGreenFace[2][1]

#Performs an F2 move.
def F2():
    [F() for i in range(2)]

#Performs an F' move.
def FP():
    [F() for i in range(3)]

#Performs a B move.
def B():
    tempBlueFace = [i[:] for i in blueFace]
    tempRedFace = [i[:] for i in redFace]
    tempOrangeFace = [i[:] for i in orangeFace]
    tempWhiteFace = [i[:] for i in whiteFace]
    tempYellowFace = [i[:] for i in yellowFace]
    yellowFace[0][0] = tempOrangeFace[0][2]
    yellowFace[0][1] = tempOrangeFace[1][2]
    yellowFace[0][2] = tempOrangeFace[2][2]
    redFace[0][0] = tempYellowFace[0][2]
    redFace[1][0] = tempYellowFace[0][1]
    redFace[2][0] = tempYellowFace[0][0]
    whiteFace[2][0] = tempRedFace[0][0]
    whiteFace[2][1] = tempRedFace[1][0]
    whiteFace[2][2] = tempRedFace[2][0]
    orangeFace[0][2] = tempWhiteFace[2][2]
    orangeFace[1][2] = tempWhiteFace[2][1]
    orangeFace[2][2] = tempWhiteFace[2][0]
    blueFace[0][0] = tempBlueFace[2][0]
    blueFace[0][1] = tempBlueFace[1][0]
    blueFace[0][2] = tempBlueFace[0][0]
    blueFace[1][2] = tempBlueFace[0][1]
    blueFace[2][2] = tempBlueFace[0][2]
    blueFace[2][1] = tempBlueFace[1][2]
    blueFace[2][0] = tempBlueFace[2][2]
    blueFace[1][0] = tempBlueFace[2][1]

#Performs a B2 move.
def B2():
    [B() for i in range(2)]

#Performs a B' move.
def BP():
    [B() for i in range(3)]

#Performs an R move.
def R():
    tempGreenFace = [i[:] for i in greenFace]
    tempBlueFace = [i[:] for i in blueFace]
    tempOrangeFace = [i[:] for i in orangeFace]
    tempWhiteFace = [i[:] for i in whiteFace]
    tempYellowFace = [i[:] for i in yellowFace]
    greenFace[0][2] = tempWhiteFace[0][2]
    greenFace[1][2] = tempWhiteFace[1][2]
    greenFace[2][2] = tempWhiteFace[2][2]
    yellowFace[0][2] = tempGreenFace[0][2]
    yellowFace[1][2] = tempGreenFace[1][2]
    yellowFace[2][2] = tempGreenFace[2][2]
    blueFace[0][0] = tempYellowFace[2][2]
    blueFace[1][0] = tempYellowFace[1][2]
    blueFace[2][0] = tempYellowFace[0][2]
    whiteFace[0][2] = tempBlueFace[2][0]
    whiteFace[1][2] = tempBlueFace[1][0]
    whiteFace[2][2] = tempBlueFace[0][0]
    orangeFace[0][0] = tempOrangeFace[2][0]
    orangeFace[0][1] = tempOrangeFace[1][0]
    orangeFace[0][2] = tempOrangeFace[0][0]
    orangeFace[1][2] = tempOrangeFace[0][1]
    orangeFace[2][2] = tempOrangeFace[0][2]
    orangeFace[2][1] = tempOrangeFace[1][2]
    orangeFace[2][0] = tempOrangeFace[2][2]
    orangeFace[1][0] = tempOrangeFace[2][1]

#Performs an R2 move.
def R2():
    [R() for i in range(2)]

#Performs an R' move.
def RP():
    [R() for i in range(3)]

#Performs an L move.
def L():
    tempGreenFace = [i[:] for i in greenFace]
    tempBlueFace = [i[:] for i in blueFace]
    tempRedFace = [i[:] for i in redFace]
    tempWhiteFace = [i[:] for i in whiteFace]
    tempYellowFace = [i[:] for i in yellowFace]
    greenFace[0][0] = tempYellowFace[0][0]
    greenFace[1][0] = tempYellowFace[1][0]
    greenFace[2][0] = tempYellowFace[2][0]
    yellowFace[0][0] = tempBlueFace[2][2]
    yellowFace[1][0] = tempBlueFace[1][2]
    yellowFace[2][0] = tempBlueFace[0][2]
    blueFace[0][2] = tempWhiteFace[2][0]
    blueFace[1][2] = tempWhiteFace[1][0]
    blueFace[2][2] = tempWhiteFace[0][0]
    whiteFace[0][0] = tempGreenFace[0][0]
    whiteFace[1][0] = tempGreenFace[1][0]
    whiteFace[2][0] = tempGreenFace[2][0]
    redFace[0][0] = tempRedFace[2][0]
    redFace[0][1] = tempRedFace[1][0]
    redFace[0][2] = tempRedFace[0][0]
    redFace[1][2] = tempRedFace[0][1]
    redFace[2][2] = tempRedFace[0][2]
    redFace[2][1] = tempRedFace[1][2]
    redFace[2][0] = tempRedFace[2][2]
    redFace[1][0] = tempRedFace[2][1]

#Performs an L2 move.
def L2():
    [L() for i in range(2)]

#Performs an L' move.
def LP():
    [L() for i in range(3)]

def colourConversion():
    colourChoice = input("Enter the colour for the cross that you wish to construct: ")
    cubeState = []
    cubeState.extend([greenFace,blueFace,redFace,orangeFace,whiteFace,yellowFace])
    #conversionColours = {'green':['white','yellow','red','orange','blue','green'],'blue':['yellow','white','orange','red','blue','green'],'red':['green','blue','white','yellow','orange','red'],'orange':['green','blue','yellow','white','red','orange'],'white':['green','blue','red','orange','white','yellow'],'yellow':['green','blue','orange','red','yellow','white']}
    #for face in range(6):
    #    for row in range(3):
    #        for column in range(3):
    #            cubeState[face][row][column] = conversionColours[colourChoice][conversionColours['white'].index(cubeState[face][row][column])]
    #print(cubeState)

    tempCubeState = [i[:] for i in cubeState]
    if colourChoice == 'green':
        cubeState[0] = tempCubeState[5]
        cubeState[1] = [[tempCubeState[4][2][2],tempCubeState[4][2][1],tempCubeState[4][2][0]],[tempCubeState[4][1][2],tempCubeState[4][1][1],tempCubeState[4][1][0]],[tempCubeState[4][0][2],tempCubeState[4][0][1],tempCubeState[4][0][0]]]
        cubeState[2] = [[tempCubeState[2][2][0],tempCubeState[2][1][0],tempCubeState[2][0][0]],[tempCubeState[2][2][1],tempCubeState[2][1][1],tempCubeState[2][0][1]],[tempCubeState[2][2][2],tempCubeState[2][1][2],tempCubeState[2][0][2]]]
        cubeState[3] = [[tempCubeState[3][0][2],tempCubeState[3][1][2],tempCubeState[3][2][2]],[tempCubeState[3][0][1],tempCubeState[3][1][1],tempCubeState[3][2][1]],[tempCubeState[3][0][0],tempCubeState[3][1][0],tempCubeState[3][2][0]]]
        cubeState[4] = tempCubeState[0]
        cubeState[5] = [[tempCubeState[1][2][2],tempCubeState[1][2][1],tempCubeState[1][2][0]],[tempCubeState[1][1][2],tempCubeState[1][1][1],tempCubeState[1][1][0]],[tempCubeState[1][0][2],tempCubeState[1][0][1],tempCubeState[1][0][0]]]
    print(cubeState)

#Compares whether one list contains variables that are all contained in another list, but not necessarily in the same order.
#Takes two lists as an input, outputs a boolean variable.
def compareList(list1,list2):
    for element in list1:
        if not element in list2:
            return False
    return True

#Validates the cube for everything other than permutation parity.
def validation():
    cubeState = []
    #cubeState is a 2D array made up of 18 sublists which contain every row on the cube.
    #It is useful for counting the number of a certain colour in a few lines of code.
    cubeState.extend([greenFace,blueFace,redFace,orangeFace,whiteFace,yellowFace])
    #These integer variables keep track of how many of a certain colour has been found.
    #A proper input should have 9 of each colour. If this is not the case, the input must be wrong, and the user is notified.
    greenCount = 0
    blueCount = 0
    redCount = 0
    orangeCount = 0
    whiteCount = 0
    yellowCount = 0
    for row in cubeState:
        for colour in row:
            #For every colour in every row, every colour is checked and added to the count.
            greenCount = greenCount + colour.count("green")
            blueCount = blueCount + colour.count("blue")
            redCount = redCount + colour.count("red")
            orangeCount = orangeCount + colour.count("orange")
            whiteCount = whiteCount + colour.count("white")
            yellowCount = yellowCount + colour.count("yellow")
    #If the number times a certain colour appears is not 9, the user is told which colour it is, how many there are, and how many there should be.
    if greenCount != 9:
        print("The cube is invalid. The number of green coloured pieces is "+str(greenCount)+", but it should be 9.")
    if blueCount != 9:
        print("The cube is invalid. The number of blue coloured pieces is "+str(blueCount)+", but it should be 9.")
    if redCount != 9:
        print("The cube is invalid. The number of red coloured pieces is "+str(redCount)+", but it should be 9.")
    if orangeCount != 9:
        print("The cube is invalid. The number of orange coloured pieces is "+str(orangeCount)+", but it should be 9.")
    if whiteCount != 9:
        print("The cube is invalid. The number of white coloured pieces is "+str(whiteCount)+", but it should be 9.")
    if yellowCount != 9:
        print("The cube is invalid. The number of yellow coloured pieces is "+str(yellowCount)+", but it should be 9.")
    
    #The cube needs to be checked for whether it has exactly one of each possible corner type.
    #cornerList is a 2D tuple which contains lists of every possible combination of colours on a corner.
    cornerList = (['yellow','red','green'],['yellow','orange','green'],['yellow','orange','blue'],['yellow','red','blue'],['white','red','green'],['white','orange','green'],['white','orange','blue'],['white','red','blue'])
    #corners is a 2D array which contains information on what the colours of the corners of the cube that has been given are.
    corners = [[yellowFace[2][0],redFace[0][2],greenFace[0][0]],[yellowFace[2][2],orangeFace[0][0],greenFace[0][2]],[yellowFace[0][2],orangeFace[0][2],blueFace[0][0]],[yellowFace[0][0],redFace[0][0],blueFace[0][2]],[whiteFace[0][0],redFace[2][2],greenFace[2][0]],[whiteFace[0][2],orangeFace[2][0],greenFace[2][2]],[whiteFace[2][2],orangeFace[2][2],blueFace[2][0]],[whiteFace[2][0],redFace[2][0],blueFace[2][2]]]
    #cornerCheck is a list which says False 8 times. It keeps track of which corners have been found to be valid.
    cornerCheck = [False for i in range(8)]
    for i in range (8):
        for j in range (8):
            #For every corner in the list 'corners', the list 'cornerList' is searched for whether it contains a list with the same colours, in any order.
            if compareList(cornerList[i],corners[j]) == True:
                #If such a list is found, cornerCheck is updated to say True for that index, meaning that corner has been found.
                cornerCheck[i] = True
    for i in range (8):
        #After validating, if False is anywhere in cornerCheck, then that corner must not have been found, so the user is notified which corner is missing.
        if cornerCheck[i] == False:
            print("The cube is missing a corner with the colours "+cornerList[i][0]+", "+cornerList[i][1]+", and "+cornerList[i][2]+".")

    #Edge validation is done in exactly the same manner as corner validation, with a longer list.
    edgeList = (['yellow','green'],['yellow','orange'],['yellow','blue'],['yellow','red'],['green','orange'],['orange','blue'],['blue','red'],['red','green'],['white','green'],['white','orange'],['white','blue'],['white','red'])
    edges = [[yellowFace[2][1],greenFace[0][1]],[yellowFace[1][2],orangeFace[0][1]],[yellowFace[0][1],blueFace[0][1]],[yellowFace[1][0],redFace[0][1]],[greenFace[1][2],orangeFace[1][0]],[orangeFace[1][2],blueFace[1][0]],[blueFace[1][2],redFace[1][0]],[redFace[1][2],greenFace[1][0]],[whiteFace[0][1],greenFace[2][1]],[whiteFace[1][2],orangeFace[2][1]],[whiteFace[2][1],blueFace[2][1]],[whiteFace[1][0],redFace[2][1]]]
    edgeCheck = [False for i in range(12)]
    for i in range (12):
        for j in range (12):
            if compareList(edgeList[i],edges[j]) == True:
                edgeCheck[i] = True
    for i in range (12):
        if edgeCheck[i] == False:
            print("The cube is missing an edge with the colours "+cornerList[i][0]+" and "+cornerList[i][1]+".")
    
    #The center pieces has to be validated for whether the way that they are orientated relative to one another is possible.
    #This dictionary contains every single possible way that the cube could be oriented, and how the rest of the center pieces would have to be positioned.
    orientationList = {('green','yellow','orange'):['blue','white','red'],('green','red','yellow'):['blue','orange','white'],('green','white','red'):['blue','yellow','orange'],('green','orange','white'):['blue','red','yellow'],('blue','yellow','red'):['green','white','orange'],('blue','orange','yellow'):['green','red','white'],('blue','white','orange'):['green','yellow','red'],('blue','red','white'):['green','orange','yellow'],('red','yellow','green'):['orange','white','blue'],('red','blue','yellow'):['orange','green','white'],('red','white','blue'):['orange','yellow','green'],('red','green','white'):['orange','blue','yellow'],('orange','yellow','blue'):['red','white','green'],('orange','green','yellow'):['red','blue','white'],('orange','white','green'):['red','yellow','blue'],('orange','blue','white'):['red','green','yellow'],('white','green','orange'):['yellow','blue','red'],('white','red','green'):['yellow','orange','blue'],('white','blue','red'):['yellow','green','orange'],('white','orange','blue'):['yellow','red','green'],('yellow','green','red'):['white','blue','orange'],('yellow','orange','green'):['white','red','blue'],('yellow','blue','orange'):['white','green','red'],('yellow','red','blue'):['white','orange','green']}
    #currentOrientation acts as the key for the dictionary which corresponds to the cube that has been input.
    currentOrientation = (greenFace[1][1],yellowFace[1][1],orangeFace[1][1])
    try:
        #If the rest of the center pieces are not as defined by the dictionary, then the the cube is invalid and the user is notified.
        if [blueFace[1][1],whiteFace[1][1],redFace[1][1]] != orientationList[currentOrientation]:
            print('The cube is invalid. Please check whether you have entered the centre pieces correctly.')
    except:
        #This try-except is required in the case that the input does not have a center orientation that works as a key to the dictionary.
        #If this is the case, then the cube is invalid and the user is notified.
        print('The cube is invalid. Please check whether you have entered the centre pieces correctly.')

    #The corner twist validation works by a mathematical method, explained in the design.
    orientedCount = 0
    for colour in [greenFace[0][2],redFace[0][2],blueFace[0][2],orangeFace[0][2],greenFace[2][0],redFace[2][0],blueFace[2][0],orangeFace[2][0]]:
        #For each yellow or white colour in a position that is one clockwise turn away from being oriented on every corner, orientedCount is increased by 1.
        if colour == 'white' or colour == 'yellow':
            orientedCount = orientedCount + 1
    for colour in [greenFace[0][0],redFace[0][0],blueFace[0][0],orangeFace[0][0],greenFace[2][2],redFace[2][2],blueFace[2][2],orangeFace[2][2]]:
        #For each yellow or white colour in a position that is one anticlockwise turn away from being oriented on every corner, orientedCount is increased by 2.
        if colour == 'white' or colour == 'yellow':
            orientedCount = orientedCount + 2
    #If this orientedCount is not divisible by 3, a corner is twisted, and the user is notified.
    if orientedCount % 3 != 0:
        print('The cube has a twisted corner. Check that you have entered the corners correctly, or else they may be twisted.')

    #The edge twist validation works by a mathematical method, explained in the design.
    orientedCount = 0
    for edge in [[yellowFace[2][1],greenFace[0][1]],[yellowFace[1][2],orangeFace[0][1]],[yellowFace[0][1],blueFace[0][1]],[yellowFace[1][0],redFace[0][1]],[greenFace[1][2],orangeFace[1][0]],[blueFace[1][0],orangeFace[1][2]],[blueFace[1][2],redFace[1][0]],[greenFace[1][0],redFace[1][2]],[whiteFace[0][1],greenFace[2][1]],[whiteFace[1][2],orangeFace[2][1]],[whiteFace[2][1],blueFace[2][1]],[whiteFace[1][0],redFace[2][1]]]:
        #Every edge is checked for whether it has a yellow or a white in an oriented position. If it does, orientedCount is increased by 1.
        if edge[0] in ['yellow','white']:
            orientedCount = orientedCount + 1
        #Every edge that does not contain yellow or white is checked for whether it has a blue or a green in an oriented position. If it does, orientedCount is increased by 1.
        if edge[0] in ['blue','green'] and edge[1] in ['red','orange']:
            orientedCount = orientedCount + 1
    #If orientedCount is not divisible by 2, an edge is twisted, and the user is notified.
    if orientedCount % 2 != 0:
        print('The cube has a twisted edge. Check that you have entered the edges correctly, or else they may be twisted.')
    
    #Permutation parity is checked later in the solve, it's just much easier to program that way.

def solve():
    global solveMoves
    #This dictionary contains every possible move and the name of the function it corresponds to.
    moveList = {'U':U,'D':D,'F':F,'B':B,'R':R,'L':L,'U2':U2,'D2':D2,'F2':F2,'B2':B2,'R2':R2,'L2':L2,"U'":UP,"D'":DP,"F'":FP,"B'":BP,"R'":RP,"L'":LP}
    #-=-=-=-=-=-=-=-=-=-=-=WHITE CROSS=-=-=-=-=-=-=-=-=-=-=-
    #solveMoves is a list that keeps track of what moves have to be done to solve the cube.
    solveMoves = []
    #First it checks for which pieces have already been solved.
    #whiteCrossSolved is a list that keeps track of which pieces of the white cross are solved.
    whiteCrossSolved = [False,False,False,False]
    #A loop is used to make the program continuously search and solve the cross until it is complete.
    while whiteCrossSolved != [True,True,True,True]:
        #Each white cross piece is solved only if it is in the correct position, and the other colour lines up with the right colour face.
        #The index 0 keeps track of whether the green side white piece is solved.
        if whiteFace[0][1] == 'white' and greenFace[2][1] == 'green':
            whiteCrossSolved[0] = True
        #The index 1 keeps track of whether the red side white piece is solved.
        if whiteFace[1][0] == 'white' and redFace[2][1] == 'red':
            whiteCrossSolved[1] = True
        #The index 2 keeps track of whether the blue side white piece is solved.
        if whiteFace[2][1] == 'white' and blueFace[2][1] == 'blue':
            whiteCrossSolved[2] = True
        #The index 3 keeps track of whether the orange side white piece is solved.
        if whiteFace[1][2] == 'white' and orangeFace[2][1] == 'orange':
            whiteCrossSolved[3] = True

        #The program now searches through every single possible position where a white edge could be, and performs an algorithm to insert it.
        #Solving the side face bottom slice.
        if greenFace[2][1] == 'white':
            #possibleMoves is a dictionary which contains different algorithms with colours as keys.
            possibleMoves = {'green':["F'",'D',"R'","D'"],'red':['F','L'],'blue':["F'","D'","R'",'D'],'orange':["F'","R'"]}
            #Depending on the other colour on the edge piece, a certain algorithm is selected.
            requiredMoves = possibleMoves[whiteFace[0][1]]
            #This algorithm is then performed and added to the final solve move list.
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        #The same procedure is used for every position, with different algorithms.
        if redFace[2][1] == 'white':
            possibleMoves = {'green':["L'","F'"],'red':["L'",'D',"F'","D'"],'blue':['L','B'],'orange':["L'","D'","F'",'D']}
            requiredMoves = possibleMoves[whiteFace[1][0]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if blueFace[2][1] == 'white':
            possibleMoves = {'green':["B'",'D',"L'","D'"],'red':["B'","L'"],'blue':["B'","D'","L'",'D'],'orange':['B','R']}
            requiredMoves = possibleMoves[whiteFace[2][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if orangeFace[2][1] == 'white':
            possibleMoves = {'green':['R','F'],'red':["R'","D'","B'",'D'],'blue':["R'","B'"],'orange':["R'",'D',"B'","D'"]}
            requiredMoves = possibleMoves[whiteFace[1][2]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        #Solving the up face.
        if yellowFace[2][1] == 'white':
            possibleMoves = {'green':['F2'],'red':['U','L2'],'blue':['U2','B2'],'orange':["U'",'R2']}
            requiredMoves = possibleMoves[greenFace[0][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if yellowFace[1][0] == 'white':
            possibleMoves = {'green':["U'",'F2'],'red':['L2'],'blue':['U','B2'],'orange':['U2','R2']}
            requiredMoves = possibleMoves[redFace[0][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if yellowFace[0][1] == 'white':
            possibleMoves = {'green':['U2','F2'],'red':["U'",'L2'],'blue':['B2'],'orange':['U','R2']}
            requiredMoves = possibleMoves[blueFace[0][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if yellowFace[1][2] == 'white':
            possibleMoves = {'green':['U','F2'],'red':['U2','L2'],'blue':["U'",'B2'],'orange':['R2']}
            requiredMoves = possibleMoves[orangeFace[0][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()
        
        #Solving the down face.
        if greenFace[2][1] != 'green' and whiteFace[0][1] == 'white':
            possibleMoves = {'red':['F2','U','L2'],'blue':['F2','U2','B2'],'orange':['F2',"U'",'R2']}
            requiredMoves = possibleMoves[greenFace[2][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if redFace[2][1] != 'red' and whiteCrossSolved[1] == False and whiteFace[1][0] == 'white':
            possibleMoves = {'green':['L2',"U'",'F2'],'blue':['L2','U','B2'],'orange':['L2','U2','R2']}
            requiredMoves = possibleMoves[redFace[2][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if blueFace[2][1] != 'blue' and whiteCrossSolved[2] == False and whiteFace[2][1] == 'white':
            possibleMoves = {'green':['B2','U2','F2'],'red':['B2',"U'",'L2'],'orange':['B2','U','R2']}
            requiredMoves = possibleMoves[blueFace[2][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if orangeFace[2][1] != 'orange' and whiteCrossSolved[3] == False and whiteFace[1][2] == 'white':
            possibleMoves = {'green':['R2','U','F2'],'red':['R2','U2','L2'],'blue':['R2',"U'",'B2']}
            requiredMoves = possibleMoves[orangeFace[2][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        #Solving the side face top slice.
        if greenFace[0][1] == 'white':
            possibleMoves = {'green':["U'","R'",'F','R'],'red':["F'",'L','F'],'blue':["U'",'R',"B'","R'"],'orange':['F',"R'","F'"]}
            requiredMoves = possibleMoves[yellowFace[2][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if redFace[0][1] == 'white':
            possibleMoves = {'green':['L',"F'","L'"],'red':["U'","F'",'L','F'],'blue':["L'",'B','L'],'orange':["U'",'F',"R'","F'"]}
            requiredMoves = possibleMoves[yellowFace[1][0]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if blueFace[0][1] == 'white':
            possibleMoves = {'green':["U'",'L',"F'","L'"],'red':['B',"L'","B'"],'blue':["U'","L'",'B','L'],'orange':["B'",'R','B']}
            requiredMoves = possibleMoves[yellowFace[0][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if orangeFace[0][1] == 'white':
            possibleMoves = {'green':["R'",'F','R'],'red':['U',"F'",'L','F'],'blue':['R',"B'","R'"],'orange':['U','F',"R'","F'"]}
            requiredMoves = possibleMoves[yellowFace[1][2]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        #Solving the side face middle slice.
        if greenFace[1][2] == 'white':
            possibleMoves = {'green':['D',"R'","D'"],'red':['D2',"R'",'D2'],'blue':["D'","R'",'D'],'orange':["R'"]}
            requiredMoves = possibleMoves[orangeFace[1][0]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if greenFace[1][0] == 'white':
            possibleMoves = {'green':["D'",'L','D'],'red':['L'],'blue':['D','L',"D'"],'orange':['D2','L','D2']}
            requiredMoves = possibleMoves[redFace[1][2]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()
        
        if redFace[1][2] == 'white':
            possibleMoves = {'green':["F'"],'red':['D',"F'","D'"],'blue':['D2',"F'",'D2'],'orange':["D'","F'",'D']}
            requiredMoves = possibleMoves[greenFace[1][0]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if redFace[1][0] == 'white':
            possibleMoves = {'green':['D2','B','D2'],'red':["D'",'B','D'],'blue':['B'],'orange':['D','B',"D'"]}
            requiredMoves = possibleMoves[blueFace[1][2]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if blueFace[1][2] == 'white':
            possibleMoves = {'green':["D'","L'",'D'],'red':["L'"],'blue':['D',"L'","D'"],'orange':['D2',"L'",'D2']}
            requiredMoves = possibleMoves[redFace[1][0]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if blueFace[1][0] == 'white':
            possibleMoves = {'green':['D','R',"D'"],'red':['D2','R','D2'],'blue':["D'",'R','D'],'orange':['R']}
            requiredMoves = possibleMoves[orangeFace[1][2]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if orangeFace[1][2] == 'white':
            possibleMoves = {'green':['D2',"B'",'D2'],'red':["D'","B'",'D'],'blue':["B'"],'orange':['D',"B'","D'"]}
            requiredMoves = possibleMoves[blueFace[1][0]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

        if orangeFace[1][0] == 'white':
            possibleMoves = {'green':['F'],'red':['D','F',"D'"],'blue':['D2','F','D2'],'orange':["D'",'F','D']}
            requiredMoves = possibleMoves[greenFace[1][2]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

    #-=-=-=-=-=-=-=-=-=-=-=F2L=-=-=-=-=-=-=-=-=-=-=-
    #First it checks for which pairs have already been solved.
    F2Lsolved = [False,False,False,False]
    while F2Lsolved != [True,True,True,True]:
        requiredMoves = []
        #Check if green-red-white pair is solved.
        if greenFace[1][0] == 'green' and greenFace[2][0] == 'green' and redFace[1][2] == 'red' and redFace[2][2] == 'red' and whiteFace[0][0] == 'white':
            F2Lsolved[0] = True
        #Check if blue-red-white pair is solved.
        if redFace[1][0] == 'red' and redFace[2][0] == 'red' and blueFace[1][2] == 'blue' and blueFace[2][2] == 'blue' and whiteFace[2][0] == 'white':
            F2Lsolved[1] = True
        #Check if blue-orange-white pair is solved.
        if blueFace[1][0] == 'blue' and blueFace[2][0] == 'blue' and orangeFace[1][2] == 'orange' and orangeFace[2][2] == 'orange' and whiteFace[2][2] == 'white':
            F2Lsolved[2] = True
        #Check if green-orange-white pair is solved.
        if orangeFace[1][0] == 'orange' and orangeFace[2][0] == 'orange' and greenFace[1][2] == 'green' and greenFace[2][2] == 'green' and whiteFace[0][2] == 'white':
            F2Lsolved[3] = True

        #This 2D array contains every edge in the middle horizontal slice.
        horizontalEdgeList = [[greenFace[1][0],redFace[1][2]],[redFace[1][0],blueFace[1][2]],[blueFace[1][0],orangeFace[1][2]],[orangeFace[1][0],greenFace[1][2]]]
        #This 2D array holds the colours of the faces that correspond to the 2D array above.
        edgeFaceList = [['green','red'],['blue','red'],['blue','orange'],['green','orange']]
        #These will be useful when searching for an edge piece in the middle slice later on.

        cornerEdgeReady = False
        #First, a corner must be located on the top layer and a corresponding edge piece must be brought up to the top layer.
        #For the case when there is an unsolved corner in the green-red-yellow corner:
        if 'white' in [greenFace[0][0],redFace[0][2],yellowFace[2][0]] and cornerEdgeReady == False:
            #The two non-white colours are stored to be used to find the matching edge.
            edgeColours = [greenFace[0][0],redFace[0][2],yellowFace[2][0]]
            edgeColours.pop(edgeColours.index('white'))
            #Search for the edge corresponding to this corner in the middle slice.
            for i in range(len(horizontalEdgeList)):
                if compareList(edgeColours,horizontalEdgeList[i]) == True:
                    #If the edge is already positioned correctly, nothing has to be done.
                    if compareList(edgeFaceList[i],edgeColours) == False:
                        #Depending on which position the edge is found, these are the moves required.
                        if i == 0:
                            requiredMoves = ["L'",'U','L']
                        elif i == 1:
                            requiredMoves = ['L',"U'","L'"]
                        elif i == 2:
                            requiredMoves = ["R'",'U','R']
                        elif i == 3:
                            requiredMoves = ['R','U',"R'"]
                        for i in range(len(requiredMoves)):
                            solveMoves.append(requiredMoves[i])
                            moveList[requiredMoves[i]]()
                        break
            #The result should be that the edge and corner pieces are both in the top layer.
            cornerEdgeReady = True
        
        #For the case when there is an unsolved corner in the blue-red-yellow corner:
        if 'white' in [blueFace[0][2],redFace[0][0],yellowFace[0][0]] and cornerEdgeReady == False:
            #The two non-white colours are stored to be used to find the matching edge.
            edgeColours = [blueFace[0][2],redFace[0][0],yellowFace[0][0]]
            edgeColours.pop(edgeColours.index('white'))
            #Search for the edge corresponding to this corner in the middle slice.
            for i in range(len(horizontalEdgeList)):
                if compareList(edgeColours,horizontalEdgeList[i]) == True:
                    #If the edge is already positioned correctly, nothing has to be done.
                    if compareList(edgeFaceList[i],edgeColours) == False:
                        #Depending on which position the edge is found, these are the moves required.
                        if i == 0:
                            requiredMoves = ["L'","U'",'L']
                        elif i == 1:
                            requiredMoves = ['L',"U'","L'"]
                        elif i == 2:
                            requiredMoves = ["R'","U'",'R']
                        elif i == 3:
                            requiredMoves = ['R',"U'","R'"]
                        for i in range(len(requiredMoves)):
                            solveMoves.append(requiredMoves[i])
                            moveList[requiredMoves[i]]()
                        break
            #The result should be that the edge and corner pieces are both in the top layer.
            cornerEdgeReady = True

        #For the case when there is an unsolved corner in the blue-orange-yellow corner:
        if 'white' in [blueFace[0][0],orangeFace[0][2],yellowFace[0][2]] and cornerEdgeReady == False:
            #The two non-white colours are stored to be used to find the matching edge.
            edgeColours = [blueFace[0][0],orangeFace[0][2],yellowFace[0][2]]
            edgeColours.pop(edgeColours.index('white'))
            #Search for the edge corresponding to this corner in the middle slice.
            for i in range(len(horizontalEdgeList)):
                if compareList(edgeColours,horizontalEdgeList[i]) == True:
                    #If the edge is already positioned correctly, nothing has to be done.
                    if compareList(edgeFaceList[i],edgeColours) == False:
                        #Depending on which position the edge is found, these are the moves required.
                        if i == 0:
                            requiredMoves = ["L'","U'",'L']
                        elif i == 1:
                            requiredMoves = ['L','U',"L'"]
                        elif i == 2:
                            requiredMoves = ["R'",'U','R']
                        elif i == 3:
                            requiredMoves = ['R',"U'","R'"]
                        for i in range(len(requiredMoves)):
                            solveMoves.append(requiredMoves[i])
                            moveList[requiredMoves[i]]()
                        break
            #The result should be that the edge and corner pieces are both in the top layer.
            cornerEdgeReady = True

        #For the case when there is an unsolved corner in the green-orange-yellow corner:
        if 'white' in [greenFace[0][2],orangeFace[0][0],yellowFace[2][2]] and cornerEdgeReady == False:
            #The two non-white colours are stored to be used to find the matching edge.
            edgeColours = [greenFace[0][2],orangeFace[0][0],yellowFace[2][2]]
            edgeColours.pop(edgeColours.index('white'))
            #Search for the edge corresponding to this corner in the middle slice.
            for i in range(len(horizontalEdgeList)):
                if compareList(edgeColours,horizontalEdgeList[i]) == True:
                    #If the edge is already positioned correctly, nothing has to be done.
                    if compareList(edgeFaceList[i],edgeColours) == False:
                        #Depending on which position the edge is found, these are the moves required.
                        if i == 0:
                            requiredMoves = ["L'","U'",'L']
                        elif i == 1:
                            requiredMoves = ['L',"U'","L'"]
                        elif i == 2:
                            requiredMoves = ["R'",'U','R']
                        elif i == 3:
                            requiredMoves = ['R',"U'","R'"]
                        for i in range(len(requiredMoves)):
                            solveMoves.append(requiredMoves[i])
                            moveList[requiredMoves[i]]()
                        break
            #The result should be that the edge and corner pieces are both in the top layer.
            cornerEdgeReady = True

        #When there is no unsolved corner in the top layer, a bottom layer corner needs to be brought up to the top layer along with a corresponding edge piece.
        #For the case when there is an unsolved corner in the green-red-white corner:
        if 'white' in [greenFace[2][0],redFace[2][2],whiteFace[0][0]] and F2Lsolved[0] == False and cornerEdgeReady == False:
            #The two non-white colours are stored to be used to find the matching edge.
            edgeColours = [greenFace[2][0],redFace[2][2],whiteFace[0][0]]
            edgeColours.pop(edgeColours.index('white'))
            #If the two non-white colours match the colours of the faces it is between, then the corner is already positioned correctly.
            if compareList(['green','red'],edgeColours) == True:
                pass
            else:
                #Three moves required to take the corner out.
                requiredMoves = ["L'","U'",'L']
                for i in range(len(requiredMoves)):
                    solveMoves.append(requiredMoves[i])
                    moveList[requiredMoves[i]]()
            #Search for the edge corresponding to this corner in the middle slice.
            for i in range(len(horizontalEdgeList)):
                if compareList(edgeColours,horizontalEdgeList[i]) == True:
                    #If the edge is already positioned correctly, nothing has to be done.
                    if compareList(edgeFaceList[i],edgeColours) == False:
                        #Depending on which position the edge is found, these are the moves required.
                        if i == 0:
                            requiredMoves = ["L'","U'",'L']
                        elif i == 1:
                            requiredMoves = ['L',"U'","L'"]
                        elif i == 2:
                            requiredMoves = ["R'",'U','R']
                        elif i == 3:
                            requiredMoves = ['R',"U'","R'"]
                        for i in range(len(requiredMoves)):
                            solveMoves.append(requiredMoves[i])
                            moveList[requiredMoves[i]]()
                        break
            #The result should be that the edge and corner pieces are both in the top layer.
            cornerEdgeReady = True

        #For the case when there is an unsolved corner in the blue-red-white corner:
        if 'white' in [blueFace[2][2],redFace[2][0],whiteFace[2][0]] and F2Lsolved[1] == False and cornerEdgeReady == False:
            #The two non-white colours are stored to be used to find the matching edge.
            edgeColours = [blueFace[2][2],redFace[2][0],whiteFace[2][0]]
            edgeColours.pop(edgeColours.index('white'))
            #If the two non-white colours match the colours of the faces it is between, then the corner is already positioned correctly.
            if compareList(['blue','red'],edgeColours) == True:
                pass
            else:
                #Three moves required to take the corner out.
                requiredMoves = ['L','U',"L'"]
                for i in range(len(requiredMoves)):
                    solveMoves.append(requiredMoves[i])
                    moveList[requiredMoves[i]]()
            #Search for the edge corresponding to this corner in the middle slice.
            for i in range(len(horizontalEdgeList)):
                if compareList(edgeColours,horizontalEdgeList[i]) == True:
                    #If the edge is already positioned correctly, nothing has to be done.
                    if compareList(edgeFaceList[i],edgeColours) == False:
                        #Depending on which position the edge is found, these are the moves required.
                        if i == 0:
                            requiredMoves = ["L'","U'",'L']
                        elif i == 1:
                            requiredMoves = ['L','U',"L'"]
                        elif i == 2:
                            requiredMoves = ["R'",'U','R']
                        elif i == 3:
                            requiredMoves = ['R',"U'","R'"]
                        for i in range(len(requiredMoves)):
                            solveMoves.append(requiredMoves[i])
                            moveList[requiredMoves[i]]()
                        break
            #The result should be that the edge and corner pieces are both in the top layer.
            cornerEdgeReady = True

        #For the case when there is an unsolved corner in the blue-orange-white corner:
        if 'white' in [blueFace[2][0],orangeFace[2][2],whiteFace[2][2]] and F2Lsolved[2] == False and cornerEdgeReady == False:
            #The two non-white colours are stored to be used to find the matching edge.
            edgeColours = [blueFace[2][0],orangeFace[2][2],whiteFace[2][2]]
            edgeColours.pop(edgeColours.index('white'))
            #If the two non-white colours match the colours of the faces it is between, then the corner is already positioned correctly.
            if compareList(['blue','orange'],edgeColours) == True:
                pass
            else:
                #Three moves required to take the corner out.
                requiredMoves = ["R'","U'",'R']
                for i in range(len(requiredMoves)):
                    solveMoves.append(requiredMoves[i])
                    moveList[requiredMoves[i]]()
            #Search for the edge corresponding to this corner in the middle slice.
            for i in range(len(horizontalEdgeList)):
                if compareList(edgeColours,horizontalEdgeList[i]) == True:
                    #If the edge is already positioned correctly, nothing has to be done.
                    if compareList(edgeFaceList[i],edgeColours) == False:
                        #Depending on which position the edge is found, these are the moves required.
                        if i == 0:
                            requiredMoves = ["L'","U'",'L']
                        elif i == 1:
                            requiredMoves = ['L',"U'","L'"]
                        elif i == 2:
                            requiredMoves = ["R'",'U','R']
                        elif i == 3:
                            requiredMoves = ['R',"U'","R'"]
                        for i in range(len(requiredMoves)):
                            solveMoves.append(requiredMoves[i])
                            moveList[requiredMoves[i]]()
                        break
            #The result should be that the edge and corner pieces are both in the top layer.
            cornerEdgeReady = True

        #For the case when there is an unsolved corner in the green-orange-white corner:
        if 'white' in [greenFace[2][2],orangeFace[2][0],whiteFace[0][2]] and F2Lsolved[3] == False and cornerEdgeReady == False:
            #The two non-white colours are stored to be used to find the matching edge.
            edgeColours = [greenFace[2][2],orangeFace[2][0],whiteFace[0][2]]
            edgeColours.pop(edgeColours.index('white'))
            #If the two non-white colours match the colours of the faces it is between, then the corner is already positioned correctly.
            if compareList(['green','orange'],edgeColours) == True:
                pass
            else:
                #Three moves required to take the corner out.
                requiredMoves = ['R','U',"R'"]
                for i in range(len(requiredMoves)):
                    solveMoves.append(requiredMoves[i])
                    moveList[requiredMoves[i]]()
            #Search for the edge corresponding to this corner in the middle slice.
            for i in range(len(horizontalEdgeList)):
                if compareList(edgeColours,horizontalEdgeList[i]) == True:
                    #If the edge is already positioned correctly, nothing has to be done.
                    if compareList(edgeFaceList[i],edgeColours) == False:
                        #Depending on which position the edge is found, these are the moves required.
                        if i == 0:
                            requiredMoves = ["L'",'U','L']
                        elif i == 1:
                            requiredMoves = ['L',"U'","L'"]
                        elif i == 2:
                            requiredMoves = ["R'",'U','R']
                        elif i == 3:
                            requiredMoves = ['R','U',"R'"]
                        for i in range(len(requiredMoves)):
                            solveMoves.append(requiredMoves[i])
                            moveList[requiredMoves[i]]()
                        break
            #The result should be that the edge and corner pieces are both in the top layer.
            cornerEdgeReady = True

        #A corner is positioned to be solved if it is in the top layer.
        #White is added to the edgeColours list, so that it can be compared to a corner.
        edgeColours.append('white')
        #For the case when it is in the green-red-yellow corner:
        if compareList(edgeColours,[greenFace[0][0],redFace[0][2],yellowFace[2][0]]) == True:
            #White has to be removed from edgeColours to find where the corner has to be placed.
            edgeColours.pop(edgeColours.index('white'))
            for i in range (len(edgeFaceList)):
                #The index of the two non-white colours in the list edgeFaceList is used to work out how many U turns have to be done.
                if compareList(edgeFaceList[i],edgeColours) == True:
                    for _ in range(i):
                        solveMoves.append('U')
                        U()
                    break
        #For the case when it is in the blue-red-yellow corner:
        elif compareList(edgeColours,[blueFace[0][2],redFace[0][0],yellowFace[0][0]]) == True:
            edgeColours.pop(edgeColours.index('white'))
            for i in range (len(edgeFaceList)):
                if compareList(edgeFaceList[i],edgeColours) == True:
                    if i - 1 < 0:
                        i = i + 4
                    for _ in range(i-1):
                        solveMoves.append('U')
                        U()
                    break
        #For the case when it is in the blue-orange-yellow corner:
        elif compareList(edgeColours,[blueFace[0][0],orangeFace[0][2],yellowFace[0][2]]) == True:
            edgeColours.pop(edgeColours.index('white'))
            for i in range (len(edgeFaceList)):
                if compareList(edgeFaceList[i],edgeColours) == True:
                    if i - 2 < 0:
                        i = i + 4
                    for _ in range(i-2):
                        solveMoves.append('U')
                        U()
                    break
        #For the case when it is in the green-orange-yellow corner:
        elif compareList(edgeColours,[greenFace[0][2],orangeFace[0][0],yellowFace[2][2]]) == True:
            edgeColours.pop(edgeColours.index('white'))
            for i in range (len(edgeFaceList)):
                if compareList(edgeFaceList[i],edgeColours) == True:
                    if i - 3 < 0:
                        i = i + 4
                    for _ in range(i-3):
                        solveMoves.append('U')
                        U()
                    break
        else:
            #If the corner is not in the top layer, nothing has to be done, and white can be removed from edgeColours.
            edgeColours.pop(edgeColours.index('white'))
        
        #Now an algorithm can be performed, from http://algdb.net/puzzle/333/f2l.
        #When solving for the green-red corner:
        if compareList(['green','red'],edgeColours) == True:
            if compareList(['white',edgeColours[0],edgeColours[1]],[whiteFace[0][0],redFace[2][2],greenFace[2][0]]) == True:
                #Positioning the edge piece:
                if redFace[0][1] == 'green' and yellowFace[1][0] == 'red':
                    solveMoves.append("U'")
                    UP()
                elif greenFace[0][1] == 'red' and yellowFace[2][1] == 'green':
                    solveMoves.append('U')
                    U()
                elif orangeFace[0][1] == 'red' and yellowFace[1][2] == 'green':
                    solveMoves.append('U2')
                    U2()
                elif orangeFace[0][1] == 'green' and yellowFace[1][2] == 'red':
                    solveMoves.append('U')
                    U()
                elif blueFace[0][1] == 'green' and yellowFace[0][1] == 'red':
                    solveMoves.append('U2')
                    U2()
                elif blueFace[0][1] == 'red' and yellowFace[0][1] == 'green':
                    solveMoves.append("U'")
                    UP()
            if redFace[0][2] == 'white' and compareList(edgeColours,[yellowFace[2][0],greenFace[0][0]]) == True:
                #F2L 1
                if greenFace[0][1] == 'green' and yellowFace[2][1] == 'red':
                    requiredMoves = ['U','F',"U'","F'"]
                #F2L 3
                elif blueFace[0][1] == 'red' and yellowFace[0][1] == 'green':
                    requiredMoves = ["L'","U'",'L']
                #F2L 5
                elif orangeFace[0][1] == 'green' and yellowFace[1][2] == 'red':
                    requiredMoves = ["U'",'F','U',"F'",'U2','F',"U'","F'"]
                #F2L 7
                elif blueFace[0][1] == 'green' and yellowFace[0][1] == 'red':
                    requiredMoves = ["U'",'F','U2',"F'",'U2','F',"U'","F'"]
                #F2L 9
                elif orangeFace[0][1] == 'red' and yellowFace[1][2] == 'green':
                    requiredMoves = ["U'",'F',"U'","F'",'U',"L'","U'",'L']
                #F2L 11
                elif greenFace[0][1] == 'red' and yellowFace[2][1] == 'green':
                    requiredMoves = ["U'",'F','U2',"F'",'U',"L'","U'",'L']
                #F2L 13
                elif redFace[0][1] == 'red' and yellowFace[1][0] == 'green':
                    requiredMoves = ['U',"L'",'U','L',"U'","L'","U'",'L']
                #F2L 15
                elif redFace[0][1] == 'green' and yellowFace[1][0] == 'red':
                    requiredMoves = ["L'",'U','L','U2','F','U',"F'"]
                #F2L 33
                elif greenFace[1][0] == 'green' and redFace[1][2] == 'red':
                    requiredMoves = ["U'",'F',"U'","F'",'U2','F',"U'","F'"]
                #F2L 35
                elif greenFace[1][0] == 'red' and redFace[1][2] == 'green':
                    requiredMoves = ["U'",'F','U',"F'",'U',"L'","U'",'L']
            elif greenFace[0][0] == 'white' and compareList(edgeColours,[yellowFace[2][0],redFace[0][2]]) == True:
                #F2L 2
                if redFace[0][1] == 'red' and yellowFace[1][0] == 'green':
                    requiredMoves = ["U'","L'",'U','L']
                #F2L 4
                elif orangeFace[0][1] == 'green' and yellowFace[1][2] == 'red':
                    requiredMoves = ["L'","U'",'L']
                #F2L 6
                elif blueFace[0][1] == 'red' and yellowFace[0][1] == 'green':
                    requiredMoves = ['U',"L'","U'",'L','U2',"L'",'U','L']
                #F2L 8
                elif orangeFace[0][1] == 'red' and yellowFace[1][2] == 'green':
                    requiredMoves = ['U',"L'",'U2','L','U2',"L'",'U','L']
                #F2L 10
                elif blueFace[0][1] == 'green' and yellowFace[0][1] == 'red':
                    requiredMoves = ['U',"L'",'U','L',"U'",'F','U',"F'"]
                #F2L 12
                elif redFace[0][1] == 'green' and yellowFace[1][0] == 'red':
                    requiredMoves = ['U',"L'",'U2','L',"U'",'F','U',"F'"]
                #F2L 14
                elif greenFace[0][1] == 'green' and yellowFace[2][1] == 'red':
                    requiredMoves = ["U'",'F',"U'","F'",'U','F','U',"F'"]
                #F2L 16
                elif greenFace[0][1] == 'red' and yellowFace[2][1] == 'green':
                    requiredMoves = ['F',"U'","F'",'U2',"L'","U'",'L']
                #F2L 34
                elif greenFace[1][0] == 'green' and redFace[1][2] == 'red':
                    requiredMoves = ['U',"L'",'U','L','U2',"L'",'U','L']
                #F2L 36
                elif greenFace[1][0] == 'red' and redFace[1][2] == 'green':
                    requiredMoves = ['U2',"L'","U'",'L','U','F',"U'","F'"]
            elif yellowFace[2][0] == 'white' and compareList(edgeColours,[redFace[0][2],greenFace[0][0]]) == True:
                #F2L 17
                if greenFace[0][1] == 'green' and yellowFace[2][1] == 'red':
                    requiredMoves = ['F','U2',"F'","U'",'F','U',"F'"]
                #F2L 18
                elif redFace[0][1] == 'red' and yellowFace[1][0] == 'green':
                    requiredMoves = ["L'",'U2','L','U',"L'","U'",'L']
                #F2L 19
                elif orangeFace[0][1] == 'green' and yellowFace[1][2] == 'red':
                    requiredMoves = ['U','F','U2',"F'",'U','F',"U'","F'"]
                #F2L 20
                elif blueFace[0][1] == 'red' and yellowFace[0][1] == 'green':
                    requiredMoves = ["U'","L'",'U2','L',"U'","L'",'U','L']
                #F2L 21
                elif blueFace[0][1] == 'green' and yellowFace[0][1] == 'red':
                    requiredMoves = ['F','R','U2',"R'","F'"]
                #F2L 22
                elif orangeFace[0][1] == 'red' and yellowFace[1][2] == 'green':
                    requiredMoves = ["L'","B'",'U2','B','L']
                #F2L 23
                elif redFace[0][1] == 'green' and yellowFace[1][0] == 'red':
                    requiredMoves = ['L',"F'","L'",'F','U','F','U',"F'"]
                #F2L 24
                elif greenFace[0][1] == 'red' and yellowFace[2][1] == 'green':
                    requiredMoves = ['L','U','F',"U'","F'","L'",'F',"U'","F'"]
                #F2L 31
                elif greenFace[1][0] == 'red' and redFace[1][2] == 'green':
                    requiredMoves = ["L'",'U','L',"U'",'F',"U'","F'"]
                #F2L 32
                elif greenFace[1][0] == 'green' and redFace[1][2] == 'red':
                    requiredMoves = ['F2','U','F2','U','F2','U2','F2']
            elif whiteFace[0][0] == 'white' and compareList(edgeColours,[redFace[2][2],greenFace[2][0]]) == True:
                #F2L 25
                if greenFace[0][1] == 'green' and yellowFace[2][1] == 'red':
                    requiredMoves = ["U'","L'",'U','L','U','F',"U'","F'"]
                #F2L 26
                elif redFace[0][1] == 'red' and yellowFace[1][0] == 'green':
                    requiredMoves = ['U','F',"U'","F'","U'","L'",'U','L']
                #F2L 37
                elif greenFace[1][0] == 'red' and redFace[1][2] == 'green':
                    requiredMoves = ['F2','U2','L','F2',"L'",'U2',"F'",'U',"F'"]
            elif redFace[2][2] == 'white' and compareList(edgeColours,[whiteFace[0][0],greenFace[2][0]]) == True:
                #F2L 27
                if greenFace[0][1] == 'green' and yellowFace[2][1] == 'red':
                    requiredMoves = ['F',"U'","F'",'U','F',"U'","F'"]
                #F2L 29
                elif redFace[0][1] == 'red' and yellowFace[1][0] == 'green':
                    requiredMoves = ["L'","U'",'L','U',"L'","U'",'L']
                #F2L 38
                elif greenFace[1][0] == 'green' and redFace[1][2] == 'red':
                    requiredMoves = ["L'","U'",'L','U2',"L'",'U','L',"U'","L'","U'",'L']
                #F2L 40
                elif greenFace[1][0] == 'red' and redFace[1][2] == 'green':
                    requiredMoves = ["L'","B'",'U2','B','L','F','U',"F'"]
            elif greenFace[2][0] == 'white' and compareList(edgeColours,[redFace[2][2],whiteFace[0][0]]) == True:
                #F2L 28
                if redFace[0][1] == 'red' and yellowFace[1][0] == 'green' :
                    requiredMoves = ["L'",'U','L',"U'","L'",'U','L']
                #F2L 30
                elif greenFace[0][1] == 'green' and yellowFace[2][1] == 'red':
                    requiredMoves = ['F','U',"F'","U'",'F','U',"F'"]
                #F2L 39
                elif greenFace[1][0] == 'green' and redFace[1][2] == 'red':
                    requiredMoves = ['F','U2','F','U',"F'",'U','F','U2','F2']
                #F2L 41
                elif greenFace[1][0] == 'red' and redFace[1][2] == 'green':
                    requiredMoves = ['F',"U'","F'","L'","B'",'U2','B','L']
        #When solving for the blue-red corner:
        elif compareList(['blue','red'],edgeColours) == True:
            if compareList(['white',edgeColours[0],edgeColours[1]],[whiteFace[2][0],blueFace[2][2],redFace[2][0]]) == True:
                #Positioning the edge piece:
                if blueFace[0][1] == 'red' and yellowFace[0][1] == 'blue':
                    solveMoves.append("U'")
                    UP()
                elif redFace[0][1] == 'blue' and yellowFace[1][0] == 'red':
                    solveMoves.append('U')
                    U()
                elif greenFace[0][1] == 'blue' and yellowFace[2][1] == 'red':
                    solveMoves.append('U2')
                    U2()
                elif greenFace[0][1] == 'red' and yellowFace[2][1] == 'blue':
                    solveMoves.append('U')
                    U()
                elif orangeFace[0][1] == 'red' and yellowFace[1][2] == 'blue':
                    solveMoves.append('U2')
                    U2()
                elif orangeFace[0][1] == 'blue' and yellowFace[1][2] == 'red':
                    solveMoves.append("U'")
                    UP()
            if blueFace[0][2] == 'white' and compareList(edgeColours,[yellowFace[0][0],redFace[0][0]]) == True:
                #F2L 1
                if redFace[0][1] == 'red' and yellowFace[1][0] == 'blue':
                    requiredMoves = ['U','L',"U'","L'"]
                #F2L 3
                elif orangeFace[0][1] == 'blue' and yellowFace[1][2] == 'red':
                    requiredMoves = ["B'","U'",'B']
                #F2L 5
                elif greenFace[0][1] == 'red' and yellowFace[2][1] == 'blue':
                    requiredMoves = ["U'",'L','U',"L'",'U2','L',"U'","L'"]
                #F2L 7
                elif orangeFace[0][1] == 'red' and yellowFace[1][2] == 'blue':
                    requiredMoves = ["U'",'L','U2',"L'",'U2','L',"U'","L'"]
                #F2L 9
                elif greenFace[0][1] == 'blue' and yellowFace[2][1] == 'red':
                    requiredMoves = ["U'",'L',"U'","L'",'U',"B'","U'",'B']
                #F2L 11
                elif redFace[0][1] == 'blue' and yellowFace[1][0] == 'red':
                    requiredMoves = ["U'",'L','U2',"L'",'U',"B'","U'",'B']
                #F2L 13
                elif blueFace[0][1] == 'blue' and yellowFace[0][1] == 'red':
                    requiredMoves = ['U',"B'",'U','B',"U'","B'","U'",'B']
                #F2L 15
                elif blueFace[0][1] == 'red' and yellowFace[0][1] == 'blue':
                    requiredMoves = ["B'",'U','B','U2','L','U',"L'"]
                #F2L 33
                elif redFace[1][0] == 'red' and blueFace[1][2] == 'blue':
                    requiredMoves = ["U'",'L',"U'","L'",'U2','L',"U'","L'"]
                #F2L 35
                elif redFace[1][0] == 'blue' and blueFace[1][2] == 'red':
                    requiredMoves = ["U'",'L','U',"L'",'U',"B'","U'",'B']
            elif redFace[0][0] == 'white' and compareList(edgeColours,[yellowFace[0][0],blueFace[0][2]]) == True:
                #F2L 2
                if blueFace[0][1] == 'blue' and yellowFace[0][1] == 'red':
                    requiredMoves = ["U'","B'",'U','B']
                #F2L 4
                elif greenFace[0][1] == 'red' and yellowFace[2][1] == 'blue':
                    requiredMoves = ["B'","U'",'B']
                #F2L 6
                elif orangeFace[0][1] == 'blue' and yellowFace[1][2] == 'red':
                    requiredMoves = ['U',"B'","U'",'B','U2',"B'",'U','B']
                #F2L 8
                elif greenFace[0][1] == 'blue' and yellowFace[2][1] == 'red':
                    requiredMoves = ['U',"B'",'U2','B','U2',"B'",'U','B']
                #F2L 10
                elif orangeFace[0][1] == 'red' and yellowFace[1][2] == 'blue':
                    requiredMoves = ['U',"B'",'U','B',"U'",'L','U',"L'"]
                #F2L 12
                elif blueFace[0][1] == 'red' and yellowFace[0][1] == 'blue':
                    requiredMoves = ['U',"B'",'U2','B',"U'",'L','U',"L'"]
                #F2L 14
                elif redFace[0][1] == 'red' and yellowFace[1][0] == 'blue':
                    requiredMoves = ["U'",'L',"U'","L'",'U','L','U',"L'"]
                #F2L 16
                elif redFace[0][1] == 'blue' and yellowFace[1][0] == 'red':
                    requiredMoves = ['L',"U'","L'",'U2',"B'","U'",'B']
                #F2L 34
                elif redFace[1][0] == 'red' and blueFace[1][2] == 'blue':
                    requiredMoves = ['U',"B'",'U','B','U2',"B'",'U','B']
                #F2L 36
                elif redFace[1][0] == 'blue' and blueFace[1][2] == 'red':
                    requiredMoves = ['U2',"B'","U'",'B','U','L',"U'","L'"]
            elif yellowFace[0][0] == 'white' and compareList(edgeColours,[blueFace[0][2],redFace[0][0]]) == True:
                #F2L 17
                if redFace[0][1] == 'red' and yellowFace[1][0] == 'blue':
                    requiredMoves = ['L','U2',"L'","U'",'L','U',"L'"]
                #F2L 18
                elif blueFace[0][1] == 'blue' and yellowFace[0][1] == 'red':
                    requiredMoves = ["B'",'U2','B','U',"B'","U'",'B']
                #F2L 19
                elif greenFace[0][1] == 'red' and yellowFace[2][1] == 'blue':
                    requiredMoves = ['U','L','U2',"L'",'U','L',"U'","L'"]
                #F2L 20
                elif orangeFace[0][1] == 'blue' and yellowFace[1][2] == 'red':
                    requiredMoves = ["U'","B'",'U2','B',"U'","B'",'U','B']
                #F2L 21
                elif orangeFace[0][1] == 'red' and yellowFace[1][2] == 'blue':
                    requiredMoves = ['L','F','U2',"F'","L'"]
                #F2L 22
                elif greenFace[0][1] == 'blue' and yellowFace[2][1] == 'red':
                    requiredMoves = ["B'","R'",'U2','R','B']
                #F2L 23
                elif blueFace[0][1] == 'red' and yellowFace[0][1] == 'blue':
                    requiredMoves = ['B',"L'","B'",'L','U','L','U',"L'"]
                #F2L 24
                elif redFace[0][1] == 'blue' and yellowFace[1][0] == 'red':
                    requiredMoves = ['B','U','L',"U'","L'","B'",'L',"U'","L'"]
                #F2L 31
                elif redFace[1][0] == 'blue' and blueFace[1][2] == 'red':
                    requiredMoves = ["B'",'U','B',"U'",'L',"U'","L'"]
                #F2L 32
                elif redFace[1][0] == 'red' and blueFace[1][2] == 'blue':
                    requiredMoves = ['L2','U','L2','U','L2','U2','L2']
            elif whiteFace[2][0] == 'white' and compareList(edgeColours,[blueFace[2][2],redFace[2][0]]) == True:
                #F2L 25
                if redFace[0][1] == 'red' and yellowFace[1][0] == 'blue':
                    requiredMoves = ["U'","B'",'U','B','U','L',"U'","L'"]
                #F2L 26
                elif blueFace[0][1] == 'blue' and yellowFace[0][1] == 'red':
                    requiredMoves = ['U','L',"U'","L'","U'","B'",'U','B']
                #F2L 37
                elif redFace[1][0] == 'blue' and blueFace[1][2] == 'red':
                    requiredMoves = ['L2','U2','B','L2',"B'",'U2',"L'",'U',"L'"]
            elif blueFace[2][2] == 'white' and compareList(edgeColours,[whiteFace[2][0],redFace[2][0]]) == True:
                #F2L 27
                if redFace[0][1] == 'red' and yellowFace[1][0] == 'blue':
                    requiredMoves = ['L',"U'","L'",'U','L',"U'","L'"]
                #F2L 29
                elif blueFace[0][1] == 'blue' and yellowFace[0][1] == 'red':
                    requiredMoves = ["B'","U'",'B','U',"B'","U'",'B']
                #F2L 38
                elif redFace[1][0] == 'red' and blueFace[1][2] == 'blue':
                    requiredMoves = ["B'","U'",'B','U2',"B'",'U','B',"U'","B'","U'",'B']
                #F2L 40
                elif redFace[1][0] == 'blue' and blueFace[1][2] == 'red':
                    requiredMoves = ["B'","R'",'U2','R','B','L','U',"L'"]
            elif redFace[2][0] == 'white' and compareList(edgeColours,[blueFace[2][2],whiteFace[2][0]]) == True:
                #F2L 28
                if blueFace[0][1] == 'blue' and yellowFace[0][1] == 'red':
                    requiredMoves = ["B'",'U','B',"U'","B'",'U','B']
                #F2L 30
                elif redFace[0][1] == 'red' and yellowFace[1][0] == 'blue':
                    requiredMoves = ['L','U',"L'","U'",'L','U',"L'"]
                #F2L 39
                elif redFace[1][0] == 'red' and blueFace[1][2] == 'blue':
                    requiredMoves = ['L','U2','L','U',"L'",'U','L','U2','L2']
                #F2L 41
                elif redFace[1][0] == 'blue' and blueFace[1][2] == 'red':
                    requiredMoves = ['L',"U'","L'","B'","R'",'U2','R','B']
        #When solving for the blue-orange corner:
        elif compareList(['blue','orange'],edgeColours) == True:
            if compareList(['white',edgeColours[0],edgeColours[1]],[whiteFace[2][2],orangeFace[2][2],blueFace[2][0]]) == True:
                #Positioning the edge piece:
                if orangeFace[0][1] == 'blue' and yellowFace[1][2] == 'orange':
                    solveMoves.append("U'")
                    UP()
                elif blueFace[0][1] == 'orange' and yellowFace[0][1] == 'blue':
                    solveMoves.append('U')
                    U()
                elif redFace[0][1] == 'orange' and yellowFace[1][0] == 'blue':
                    solveMoves.append('U2')
                    U2()
                elif redFace[0][1] == 'blue' and yellowFace[1][0] == 'orange':
                    solveMoves.append('U')
                    U()
                elif greenFace[0][1] == 'blue' and yellowFace[2][1] == 'orange':
                    solveMoves.append('U2')
                    U2()
                elif greenFace[0][1] == 'orange' and yellowFace[2][1] == 'blue':
                    solveMoves.append("U'")
                    UP()
            if orangeFace[0][2] == 'white' and compareList(edgeColours,[yellowFace[0][2],blueFace[0][0]]) == True:
                #F2L 1
                if blueFace[0][1] == 'blue' and yellowFace[0][1] == 'orange':
                    requiredMoves = ['U','B',"U'","B'"]
                #F2L 3
                elif greenFace[0][1] == 'orange' and yellowFace[2][1] == 'blue':
                    requiredMoves = ["R'","U'",'R']
                #F2L 5
                elif redFace[0][1] == 'blue' and yellowFace[1][0] == 'orange':
                    requiredMoves = ["U'",'B','U',"B'",'U2','B',"U'","B'"]
                #F2L 7
                elif greenFace[0][1] == 'blue' and yellowFace[2][1] == 'orange':
                    requiredMoves = ["U'",'B','U2',"B'",'U2','B',"U'","B'"]
                #F2L 9
                elif redFace[0][1] == 'orange' and yellowFace[1][0] == 'blue':
                    requiredMoves = ["U'",'B',"U'","B'",'U',"R'","U'",'R']
                #F2L 11
                elif blueFace[0][1] == 'orange' and yellowFace[0][1] == 'blue':
                    requiredMoves = ["U'",'B','U2',"B'",'U',"R'","U'",'R']
                #F2L 13
                elif orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'blue':
                    requiredMoves = ['U',"R'",'U','R',"U'","R'","U'",'R']
                #F2L 15
                elif orangeFace[0][1] == 'blue' and yellowFace[1][2] == 'orange':
                    requiredMoves = ["R'",'U','R','U2','B','U',"B'"]
                #F2L 33
                elif blueFace[1][0] == 'blue' and orangeFace[1][2] == 'orange':
                    requiredMoves = ["U'",'B',"U'","B'",'U2','B',"U'","B'"]
                #F2L 35
                elif blueFace[1][0] == 'orange' and orangeFace[1][2] == 'blue':
                    requiredMoves = ["U'",'B','U',"B'",'U',"R'","U'",'R']
            elif blueFace[0][0] == 'white' and compareList(edgeColours,[yellowFace[0][2],orangeFace[0][2]]) == True:
                #F2L 2
                if orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'blue':
                    requiredMoves = ["U'","R'",'U','R']
                #F2L 4
                elif redFace[0][1] == 'blue' and yellowFace[1][0] == 'orange':
                    requiredMoves = ["R'","U'",'R']
                #F2L 6
                elif greenFace[0][1] == 'orange' and yellowFace[2][1] == 'blue':
                    requiredMoves = ['U',"R'","U'",'R','U2',"R'",'U','R']
                #F2L 8
                elif redFace[0][1] == 'orange' and yellowFace[1][0] == 'blue':
                    requiredMoves = ['U',"R'",'U2','R','U2',"R'",'U','R']
                #F2L 10
                elif greenFace[0][1] == 'blue' and yellowFace[2][1] == 'orange':
                    requiredMoves = ['U',"R'",'U','R',"U'",'B','U',"B'"]
                #F2L 12
                elif orangeFace[0][1] == 'blue' and yellowFace[1][2] == 'orange':
                    requiredMoves = ['U',"R'",'U2','R',"U'",'B','U',"B'"]
                #F2L 14
                elif blueFace[0][1] == 'blue' and yellowFace[0][1] == 'orange':
                    requiredMoves = ["U'",'B',"U'","B'",'U','B','U',"B'"]
                #F2L 16
                elif blueFace[0][1] == 'orange' and yellowFace[0][1] == 'blue':
                    requiredMoves = ['B',"U'","B'",'U2',"R'","U'",'R']
                #F2L 34
                elif blueFace[1][0] == 'blue' and orangeFace[1][2] == 'orange':
                    requiredMoves = ['U',"R'",'U','R','U2',"R'",'U','R']
                #F2L 36
                elif blueFace[1][0] == 'orange' and orangeFace[1][2] == 'blue':
                    requiredMoves = ['U2',"R'","U'",'R','U','B',"U'","B'"]
            elif yellowFace[0][2] == 'white' and compareList(edgeColours,[orangeFace[0][2],blueFace[0][0]]) == True:
                #F2L 17
                if blueFace[0][1] == 'blue' and yellowFace[0][1] == 'orange':
                    requiredMoves = ['B','U2',"B'","U'",'B','U',"B'"]
                #F2L 18
                elif orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'blue':
                    requiredMoves = ["R'",'U2','R','U',"R'","U'",'R']
                #F2L 19
                elif redFace[0][1] == 'blue' and yellowFace[1][0] == 'orange':
                    requiredMoves = ['U','B','U2',"B'",'U','B',"U'","B'"]
                #F2L 20
                elif greenFace[0][1] == 'orange' and yellowFace[2][1] == 'blue':
                    requiredMoves = ["U'","R'",'U2','R',"U'","R'",'U','R']
                #F2L 21
                elif greenFace[0][1] == 'blue' and yellowFace[2][1] == 'orange':
                    requiredMoves = ['B','L','U2',"L'","B'"]
                #F2L 22
                elif redFace[0][1] == 'orange' and yellowFace[1][0] == 'blue':
                    requiredMoves = ["R'","F'",'U2','F','R']
                #F2L 23
                elif orangeFace[0][1] == 'blue' and yellowFace[1][2] == 'orange':
                    requiredMoves = ['R',"B'","R'",'B','U','B','U',"B'"]
                #F2L 24
                elif blueFace[0][1] == 'orange' and yellowFace[0][1] == 'blue':
                    requiredMoves = ['R','U','B',"U'","B'","R'",'B',"U'","B'"]
                #F2L 31
                elif blueFace[1][0] == 'orange' and orangeFace[1][2] == 'blue':
                    requiredMoves = ["R'",'U','R',"U'",'B',"U'","B'"]
                #F2L 32
                elif blueFace[1][0] == 'blue' and orangeFace[1][2] == 'orange':
                    requiredMoves = ['B2','U','B2','U','B2','U2','B2']
            elif whiteFace[2][2] == 'white' and compareList(edgeColours,[orangeFace[2][2],blueFace[2][0]]) == True:
                #F2L 25
                if blueFace[0][1] == 'blue' and yellowFace[0][1] == 'orange':
                    requiredMoves = ["U'","R'",'U','R','U','B',"U'","B'"]
                #F2L 26
                elif orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'blue':
                    requiredMoves = ['U','B',"U'","B'","U'","R'",'U','R']
                #F2L 37
                elif blueFace[1][0] == 'orange' and orangeFace[1][2] == 'blue':
                    requiredMoves = ['B2','U2','R','B2',"R'",'U2',"B'",'U',"B'"]
            elif orangeFace[2][2] == 'white' and compareList(edgeColours,[whiteFace[2][2],blueFace[2][0]]) == True:
                #F2L 27
                if blueFace[0][1] == 'blue' and yellowFace[0][1] == 'orange':
                    requiredMoves = ['B',"U'","B'",'U','B',"U'","B'"]
                #F2L 29
                elif orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'blue':
                    requiredMoves = ["R'","U'",'R','U',"R'","U'",'R']
                #F2L 38
                elif blueFace[1][0] == 'blue' and orangeFace[1][2] == 'orange':
                    requiredMoves = ["R'","U'",'R','U2',"R'",'U','R',"U'","R'","U'",'R']
                #F2L 40
                elif blueFace[1][0] == 'orange' and orangeFace[1][2] == 'blue':
                    requiredMoves = ["R'","F'",'U2','F','R','B','U',"B'"]
            elif blueFace[2][0] == 'white' and compareList(edgeColours,[orangeFace[2][2],whiteFace[2][2]]) == True:
                #F2L 28
                if orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'blue':
                    requiredMoves = ["R'",'U','R',"U'","R'",'U','R']
                #F2L 30
                elif blueFace[0][1] == 'blue' and yellowFace[0][1] == 'orange':
                    requiredMoves = ['B','U',"B'","U'",'B','U',"B'"]
                #F2L 39
                elif blueFace[1][0] == 'blue' and orangeFace[1][2] == 'orange':
                    requiredMoves = ['B','U2','B','U',"B'",'U','B','U2','B2']
                #F2L 41
                elif blueFace[1][0] == 'orange' and orangeFace[1][2] == 'blue':
                    requiredMoves = ['B',"U'","B'","R'","F'",'U2','F','R']
        #When solving for the green-orange corner:
        elif compareList(['green','orange'],edgeColours) == True:
            if compareList(['white',edgeColours[0],edgeColours[1]],[whiteFace[0][2],greenFace[2][2],orangeFace[2][0]]) == True:
                #Positioning the edge piece:
                if greenFace[0][1] == 'orange' and yellowFace[2][1] == 'green':
                    solveMoves.append("U'")
                    UP()
                elif orangeFace[0][1] == 'green' and yellowFace[1][2] == 'orange':
                    solveMoves.append('U')
                    U()
                elif blueFace[0][1] == 'green' and yellowFace[0][1] == 'orange':
                    solveMoves.append('U2')
                    U2()
                elif blueFace[0][1] == 'orange' and yellowFace[0][1] == 'green':
                    solveMoves.append('U')
                    U()
                elif redFace[0][1] == 'orange' and yellowFace[1][0] == 'green':
                    solveMoves.append('U2')
                    U2()
                elif redFace[0][1] == 'green' and yellowFace[1][0] == 'orange':
                    solveMoves.append("U'")
                    UP()
            if greenFace[0][2] == 'white' and compareList(edgeColours,[yellowFace[2][2],orangeFace[0][0]]) == True:
                #F2L 1
                if orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'green':
                    requiredMoves = ['U','R',"U'","R'"]
                #F2L 3
                elif redFace[0][1] == 'green' and yellowFace[1][0] == 'orange':
                    requiredMoves = ["F'","U'",'F']
                #F2L 5
                elif blueFace[0][1] == 'orange' and yellowFace[0][1] == 'green':
                    requiredMoves = ["U'",'R','U',"R'",'U2','R',"U'","R'"]
                #F2L 7
                elif redFace[0][1] == 'orange' and yellowFace[1][0] == 'green':
                    requiredMoves = ["U'",'R','U2',"R'",'U2','R',"U'","R'"]
                #F2L 9
                elif blueFace[0][1] == 'green' and yellowFace[0][1] == 'orange':
                    requiredMoves = ["U'",'R',"U'","R'",'U',"F'","U'",'F']
                #F2L 11
                elif orangeFace[0][1] == 'green' and yellowFace[1][2] == 'orange':
                    requiredMoves = ["U'",'R','U2',"R'",'U',"F'","U'",'F']
                #F2L 13
                elif greenFace[0][1] == 'green' and yellowFace[2][1] == 'orange':
                    requiredMoves = ['U',"F'",'U','F',"U'","F'","U'",'F']
                #F2L 15
                elif greenFace[0][1] == 'orange' and yellowFace[2][1] == 'green':
                    requiredMoves = ["F'",'U','F','U2','R','U',"R'"]
                #F2L 33
                elif orangeFace[1][0] == 'orange' and greenFace[1][2] == 'green':
                    requiredMoves = ["U'",'R',"U'","R'",'U2','R',"U'","R'"]
                #F2L 35
                elif orangeFace[1][0] == 'green' and greenFace[1][2] == 'orange':
                    requiredMoves = ["U'",'R','U',"R'",'U',"F'","U'",'F']
            elif orangeFace[0][0] == 'white' and compareList(edgeColours,[yellowFace[2][2],greenFace[0][2]]) == True:
                #F2L 2
                if greenFace[0][1] == 'green' and yellowFace[2][1] == 'orange':
                    requiredMoves = ["U'","F'",'U','F']
                #F2L 4
                elif blueFace[0][1] == 'orange' and yellowFace[0][1] == 'green':
                    requiredMoves = ["F'","U'",'F']
                #F2L 6
                elif redFace[0][1] == 'green' and yellowFace[1][0] == 'orange':
                    requiredMoves = ['U',"F'","U'",'F','U2',"F'",'U','F']
                #F2L 8
                elif blueFace[0][1] == 'green' and yellowFace[0][1] == 'orange':
                    requiredMoves = ['U',"F'",'U2','F','U2',"F'",'U','F']
                #F2L 10
                elif redFace[0][1] == 'orange' and yellowFace[1][0] == 'green':
                    requiredMoves = ['U',"F'",'U','F',"U'",'R','U',"R'"]
                #F2L 12
                elif greenFace[0][1] == 'orange' and yellowFace[2][1] == 'green':
                    requiredMoves = ['U',"F'",'U2','F',"U'",'R','U',"R'"]
                #F2L 14
                elif orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'green':
                    requiredMoves = ["U'",'R',"U'","R'",'U','R','U',"R'"]
                #F2L 16
                elif orangeFace[0][1] == 'green' and yellowFace[1][2] == 'orange':
                    requiredMoves = ['R',"U'","R'",'U2',"F'","U'",'F']
                #F2L 34
                elif orangeFace[1][0] == 'orange' and greenFace[1][2] == 'green':
                    requiredMoves = ['U',"F'",'U','F','U2',"F'",'U','F']
                #F2L 36
                elif orangeFace[1][0] == 'green' and greenFace[1][2] == 'orange':
                    requiredMoves = ['U2',"F'","U'",'F','U','R',"U'","R'"]
            elif yellowFace[2][2] == 'white' and compareList(edgeColours,[greenFace[0][2],orangeFace[0][0]]) == True:
                #F2L 17
                if orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'green':
                    requiredMoves = ['R','U2',"R'","U'",'R','U',"R'"]
                #F2L 18
                elif greenFace[0][1] == 'green' and yellowFace[2][1] == 'orange':
                    requiredMoves = ["F'",'U2','F','U',"F'","U'",'F']
                #F2L 19
                elif blueFace[0][1] == 'orange' and yellowFace[0][1] == 'green':
                    requiredMoves = ['U','R','U2',"R'",'U','R',"U'","R'"]
                #F2L 20
                elif redFace[0][1] == 'green' and yellowFace[1][0] == 'orange':
                    requiredMoves = ["U'","F'",'U2','F',"U'","F'",'U','F']
                #F2L 21
                elif redFace[0][1] == 'orange' and yellowFace[1][0] == 'green':
                    requiredMoves = ['R','B','U2',"B'","R'"]
                #F2L 22
                elif blueFace[0][1] == 'green' and yellowFace[0][1] == 'orange':
                    requiredMoves = ["F'","L'",'U2','L','F']
                #F2L 23
                elif greenFace[0][1] == 'orange' and yellowFace[2][1] == 'green':
                    requiredMoves = ['F',"R'","F'",'R','U','R','U',"R'"]
                #F2L 24
                elif orangeFace[0][1] == 'green' and yellowFace[1][2] == 'orange':
                    requiredMoves = ['F','U','R',"U'","R'","F'",'R',"U'","R'"]
                #F2L 31
                elif orangeFace[1][0] == 'green' and greenFace[1][2] == 'orange':
                    requiredMoves = ["F'",'U','F',"U'",'R',"U'","R'"]
                #F2L 32
                elif orangeFace[1][0] == 'orange' and greenFace[1][2] == 'green':
                    requiredMoves = ['R2','U','R2','U','R2','U2','R2']
            elif whiteFace[0][2] == 'white' and compareList(edgeColours,[greenFace[2][2],orangeFace[2][0]]) == True:
                #F2L 25
                if orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'green':
                    requiredMoves = ["U'","F'",'U','F','U','R',"U'","R'"]
                #F2L 26
                elif greenFace[0][1] == 'green' and yellowFace[2][1] == 'orange':
                    requiredMoves = ['U','R',"U'","R'","U'","F'",'U','F']
                #F2L 37
                elif orangeFace[1][0] == 'green' and greenFace[1][2] == 'orange':
                    requiredMoves = ['R2','U2','F','R2',"F'",'U2',"R'",'U',"R'"]
            elif greenFace[2][2] == 'white' and compareList(edgeColours,[whiteFace[0][2],orangeFace[2][0]]) == True:
                #F2L 27
                if orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'green':
                    requiredMoves = ['R',"U'","R'",'U','R',"U'","R'"]
                #F2L 29
                elif greenFace[0][1] == 'green' and yellowFace[2][1] == 'orange':
                    requiredMoves = ["F'","U'",'F','U',"F'","U'",'F']
                #F2L 38
                elif orangeFace[1][0] == 'orange' and greenFace[1][2] == 'green':
                    requiredMoves = ["F'","U'",'F','U2',"F'",'U','F',"U'","F'","U'",'F']
                #F2L 40
                elif orangeFace[1][0] == 'green' and greenFace[1][2] == 'orange':
                    requiredMoves = ["F'","L'",'U2','L','F','R','U',"R'"]
            elif orangeFace[2][0] == 'white' and compareList(edgeColours,[greenFace[2][2],whiteFace[0][2]]) == True:
                #F2L 28
                if greenFace[0][1] == 'green' and yellowFace[2][1] == 'orange':
                    requiredMoves = ["F'",'U','F',"U'","F'",'U','F']
                #F2L 30
                elif orangeFace[0][1] == 'orange' and yellowFace[1][2] == 'green':
                    requiredMoves = ['R','U',"R'","U'",'R','U',"R'"]
                #F2L 39
                elif orangeFace[1][0] == 'orange' and greenFace[1][2] == 'green':
                    requiredMoves = ['R','U2','R','U',"R'",'U','R','U2','R2']
                #F2L 41
                elif orangeFace[1][0] == 'green' and greenFace[1][2] == 'orange':
                    requiredMoves = ['R',"U'","R'","F'","L'",'U2','L','F']
                    
        for i in range(len(requiredMoves)):
            solveMoves.append(requiredMoves[i])
            moveList[requiredMoves[i]]()

    #-=-=-=-=-=-=-=-=-=-=-=OLL=-=-=-=-=-=-=-=-=-=-=-
    requiredMoves = []
    #If OLL is complete, an algorithm does not need to be performed.
    if yellowFace != [['yellow','yellow','yellow'],['yellow','yellow','yellow'],['yellow','yellow','yellow']]:
        #Through the use of a for loop and U turns, the state of the yellow face can be cycled into every possible positions.
        #This grants the benefit of not needing to program extra algorithms for each orientation of the yellow face.
        for _ in range(4):
            #Now an algorithm can be performed, from http://algdb.net/puzzle/333/oll.
            U()
            solveMoves.append('U')
            #OLL 1
            if [greenFace[0][1],redFace[0][0],redFace[0][1],redFace[0][2],blueFace[0][1],orangeFace[0][0],orangeFace[0][1],orangeFace[0][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U2', 'R2', 'F', 'R', "F'", 'U2', "R'", 'F', 'R', "F'"]
            #Oll 2
            elif [greenFace[0][1],greenFace[0][2],redFace[0][0],redFace[0][1],redFace[0][2],blueFace[0][0],blueFace[0][1],orangeFace[0][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'R', 'U', "R'", "U'", "F'", 'U2', 'F', 'U', 'R', "U'", "R'", "F'"]
            #OLL 3
            elif [greenFace[0][1],greenFace[0][2],redFace[0][1],redFace[0][2],blueFace[0][1],orangeFace[0][1],orangeFace[0][2],yellowFace[0][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'U', 'R', "U'", "R'", "F'", 'U', 'F', 'R', 'U', "R'", "U'", "F'"]
            #OLL 4
            elif [greenFace[0][1],redFace[0][0],redFace[0][1],blueFace[0][0],blueFace[0][1],orangeFace[0][0],orangeFace[0][1],yellowFace[2][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'U', 'R', "U'", "R'", "F'", "U'", 'F', 'R', 'U', "R'", "U'", "F'"]
            #OLL 5
            elif [redFace[0][1],redFace[0][2],blueFace[0][1],blueFace[0][2],orangeFace[0][2],yellowFace[1][2],yellowFace[2][1],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'R', 'U', "R'", "U'", "F'", "U'", 'F', 'R', 'U', "R'", "U'", "F'"]
            #OLL 6
            elif [redFace[0][0],blueFace[0][0],blueFace[0][1],orangeFace[0][0],orangeFace[0][1],yellowFace[1][0],yellowFace[2][0],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', 'R2', 'F', 'R', 'F2', 'U', 'F']
            #OLL 7
            elif [greenFace[0][1],greenFace[0][2],blueFace[0][2],orangeFace[0][1],orangeFace[0][2],yellowFace[0][1],yellowFace[1][0],yellowFace[2][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', "R'", "F'", 'R', 'U2', 'R', 'U2', "R'"]
            #OLL 8
            elif [greenFace[0][0],greenFace[0][1],redFace[0][0],redFace[0][1],blueFace[0][0],yellowFace[0][1],yellowFace[1][2],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U2', "R'", 'U2', "R'", 'F', 'R', "F'"]
            #OLL 9
            elif [greenFace[0][0],greenFace[0][1],redFace[0][0],blueFace[0][0],orangeFace[0][1],yellowFace[0][1],yellowFace[1][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', "R'", "U'", "R'", 'F', 'R2', 'U', "R'", "U'", "F'"]
            #OLL 10
            elif [greenFace[0][2],redFace[0][2],blueFace[0][1],blueFace[0][2],orangeFace[0][1],yellowFace[0][2],yellowFace[1][0],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', "R'", 'U', "R'", 'F', 'R', "F'", 'R', 'U2', "R'"]
            #OLL 11
            elif [greenFace[0][2],redFace[0][2],blueFace[0][1],orangeFace[0][1],orangeFace[0][2],yellowFace[0][0],yellowFace[1][0],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["F'", "L'", "U'", 'L', 'U', 'F', 'U', 'F', 'R', 'U', "R'", "U'", "F'"]
            #OLL 12
            elif [greenFace[0][0],redFace[0][0],redFace[0][1],blueFace[0][1],orangeFace[0][0],yellowFace[0][2],yellowFace[1][2],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'R', 'U', "R'", "U'", "F'", 'U', 'F', 'R', 'U', "R'", "U'", "F'"]
            #OLL 13
            elif [greenFace[0][1],greenFace[0][2],blueFace[0][1],blueFace[0][2],orangeFace[0][2],yellowFace[1][0],yellowFace[1][2],yellowFace[2][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'U', 'R', 'U2', "R'", "U'", 'R', 'U', "R'", "F'"]
            #OLL 14
            elif [greenFace[0][0],greenFace[0][1],redFace[0][0],blueFace[0][0],blueFace[0][1],yellowFace[1][0],yellowFace[1][2],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", 'F', 'R', 'U', "R'", "F'", 'R', 'F', "U'", "F'"]
            #OLL 15
            elif [greenFace[0][1],greenFace[0][2],redFace[0][2],blueFace[0][1],orangeFace[0][2],yellowFace[0][0],yellowFace[1][0],yellowFace[1][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", "F'", 'R', "L'", "U'", 'L', 'U', "R'", 'F', 'R']
            #OLL 16
            elif [greenFace[0][0],greenFace[0][1],redFace[0][0],blueFace[0][1],orangeFace[0][0],yellowFace[0][2],yellowFace[1][0],yellowFace[1][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['L', 'F', "L'", 'R', 'U', "R'", "U'", 'L', "F'", "L'"]
            #OLL 17
            elif [greenFace[0][1],redFace[0][1],redFace[0][2],blueFace[0][0],blueFace[0][1],orangeFace[0][1],yellowFace[0][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', "R'", 'U', "R'", 'F', 'R', "F'", 'U2', "R'", 'F', 'R', "F'"]
            #OLL 18
            elif [greenFace[0][0],greenFace[0][1],greenFace[0][2],redFace[0][1],blueFace[0][1],orangeFace[0][1],yellowFace[0][0],yellowFace[0][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['L', 'F', 'R', 'U2', "R'", 'U2', 'R', 'U2', "R'", "F'", "L'"]
            #OLL 19
            elif [greenFace[0][1],redFace[0][1],redFace[0][2],blueFace[0][1],orangeFace[0][0],orangeFace[0][1],yellowFace[0][0],yellowFace[0][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", 'U2', 'F', 'R', 'U', "R'", "U'", 'F2', 'U2', 'F', 'R']
            #OLL 20
            elif [greenFace[0][1],redFace[0][1],blueFace[0][1],orangeFace[0][1],yellowFace[0][0],yellowFace[0][2],yellowFace[2][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'U', 'R', "U'", "R'", "F'", 'U2', "R'", "U'", "R'", 'F', 'R', "F'", 'U', 'R']
            #OLL 21
            elif [greenFace[0][0],greenFace[0][2],blueFace[0][0],blueFace[0][2],yellowFace[0][1],yellowFace[1][0],yellowFace[1][2],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'R', 'U', "R'", "U'", 'R', 'U', "R'", "U'", 'R', 'U', "R'", "U'", "F'"]
            #OLL 22
            elif [greenFace[0][2],redFace[0][0],redFace[0][2],blueFace[0][0],yellowFace[0][1],yellowFace[1][0],yellowFace[1][2],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U2', 'R2', "U'", 'R2', "U'", 'R2', 'U2', 'R']
            #OLL 23
            elif [greenFace[0][0],greenFace[0][0],yellowFace[0][0],yellowFace[0][1],yellowFace[0][2],yellowFace[1][0],yellowFace[1][2],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R2', 'D', "R'", 'U2', 'R', "D'", "R'", 'U2', "R'"]
            #OLL 24
            elif [greenFace[0][0],blueFace[0][2],yellowFace[0][1],yellowFace[0][2],yellowFace[1][0],yellowFace[1][2],yellowFace[2][1],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['L', 'F', "R'", "F'", "L'", 'F', 'R', "F'"]
            #OLL 25
            elif [greenFace[0][0],orangeFace[0][2],yellowFace[0][0],yellowFace[0][1],yellowFace[1][0],yellowFace[1][2],yellowFace[2][1],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", 'F', 'R', "B'", "R'", "F'", 'R', 'B']
            #OLL 26
            elif [greenFace[0][0],redFace[0][0],orangeFace[0][0],yellowFace[0][1],yellowFace[0][2],yellowFace[1][0],yellowFace[1][2],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U2', "R'", "U'", 'R', "U'", "R'"]
            #OLL 27
            elif [greenFace[0][2],blueFace[0][2],orangeFace[0][2],yellowFace[0][1],yellowFace[1][0],yellowFace[1][2],yellowFace[2][0],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', "R'", 'U', 'R', 'U2', "R'"]
            #OLL 28
            elif [greenFace[0][1],orangeFace[0][1],yellowFace[0][0],yellowFace[0][1],yellowFace[0][2],yellowFace[1][0],yellowFace[2][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'R', 'U', "R'", "U'", 'F2', "L'", "U'", 'L', 'U', 'F']
            #OLL 29
            elif [greenFace[0][0],greenFace[0][1],blueFace[0][2],orangeFace[0][1],yellowFace[0][1],yellowFace[0][2],yellowFace[1][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', "R'", "U'", 'R', "U'", "R'", "F'", "U'", 'F', 'R', 'U', "R'"]
            #OLL 30
            elif [greenFace[0][1],redFace[0][0],orangeFace[0][1],orangeFace[0][2],yellowFace[0][1],yellowFace[1][0],yellowFace[2][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'U', 'R', 'U2', "R'", "U'", 'R', 'U2', "R'", "U'", "F'"]
            #OLL 31
            elif [greenFace[0][0],greenFace[0][1],redFace[0][1],blueFace[0][2],yellowFace[0][1],yellowFace[0][2],yellowFace[1][2],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", "U'", 'F', 'U', 'R', "U'", "R'", "F'", 'R']
            #OLL 32
            elif [redFace[0][0],blueFace[0][1],orangeFace[0][1],orangeFace[0][2],yellowFace[1][0],yellowFace[2][0],yellowFace[2][1],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'U', "R'", "U'", "F'", 'U', 'F', 'R', "F'"]
            #OLL 33
            elif [greenFace[0][0],greenFace[0][1],blueFace[0][1],blueFace[0][2],yellowFace[0][2],yellowFace[1][0],yellowFace[1][2],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', "R'", "U'", "R'", 'F', 'R', "F'"]
            #OLL 34
            elif [greenFace[0][1],redFace[0][0],blueFace[0][1],orangeFace[0][2],yellowFace[1][0],yellowFace[1][2],yellowFace[2][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', 'R2', "U'", "R'", 'F', 'R', 'U', 'R', "U'", "F'"]
            #OLL 35
            elif [greenFace[0][0],redFace[0][1],blueFace[0][1],orangeFace[0][2],yellowFace[0][0],yellowFace[1][2],yellowFace[2][1],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U2', 'R2', 'F', 'R', "F'", 'R', 'U2', "R'"]
            #OLL 36
            elif [greenFace[0][0],blueFace[0][1],orangeFace[0][1],orangeFace[0][2],yellowFace[0][0],yellowFace[1][0],yellowFace[2][1],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', "R'", "U'", "F'", 'U2', 'F', 'U', 'R', 'U', "R'"]
            #OLL 37
            elif [greenFace[0][0],greenFace[0][1],orangeFace[0][1],orangeFace[0][2],yellowFace[0][0],yellowFace[0][1],yellowFace[1][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'R', "U'", "R'", "U'", 'R', 'U', "R'", "F'"]
            #OLL 38
            elif [greenFace[0][1],blueFace[0][2],orangeFace[0][0],orangeFace[0][1],yellowFace[0][1],yellowFace[0][2],yellowFace[1][0],yellowFace[2][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', "R'", 'U', 'R', "U'", "R'", "U'", "R'", 'F', 'R', "F'"]
            #OLL 39
            elif [redFace[0][1],redFace[0][2],blueFace[0][0],orangeFace[0][1],yellowFace[0][0],yellowFace[0][1],yellowFace[2][1],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', "R'", "F'", "U'", 'F', 'U', 'R', "U'", "F'"]
            #OLL 40
            elif [greenFace[0][1],redFace[0][2],blueFace[0][0],blueFace[0][1],yellowFace[0][0],yellowFace[1][0],yellowFace[1][2],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", 'F', 'R', 'U', "R'", "U'", "F'", 'U', 'R']
            #OLL 41
            elif [greenFace[0][1],blueFace[0][0],blueFace[0][2],orangeFace[0][1],yellowFace[0][1],yellowFace[1][0],yellowFace[2][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U', "R'", 'U', 'R', 'U2', "R'", 'F', 'R', 'U', "R'", "U'", "F'"]
            #OLL 42
            elif [greenFace[0][1],redFace[0][1],blueFace[0][0],blueFace[0][2],yellowFace[0][1],yellowFace[1][2],yellowFace[2][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", 'U', 'R', 'U2', "R'", "U'", "F'", 'U', 'F', 'U', 'R']
            #OLL 43
            elif [greenFace[0][0],greenFace[0][1],greenFace[0][2],orangeFace[0][1],yellowFace[0][0],yellowFace[0][1],yellowFace[0][2],yellowFace[1][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", "U'", "F'", 'U', 'F', 'R']
            #OLL 44
            elif [greenFace[0][1],orangeFace[0][0],orangeFace[0][1],orangeFace[0][2],yellowFace[0][0],yellowFace[0][1],yellowFace[1][0],yellowFace[2][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'U', 'R', "U'", "R'", "F'"]
            #OLL 45
            elif [greenFace[0][1],redFace[0][0],redFace[0][2],blueFace[0][1],yellowFace[0][2],yellowFace[1][0],yellowFace[1][2],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'R', 'U', "R'", "U'", "F'"]
            #OLL 46
            elif [redFace[0][1],orangeFace[0][0],orangeFace[0][1],orangeFace[0][2],yellowFace[0][0],yellowFace[0][1],yellowFace[2][0],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", "U'", "R'", 'F', 'R', "F'", 'U', 'R']
            #OLL 47
            elif [greenFace[0][0],greenFace[0][1],redFace[0][1],blueFace[0][2],orangeFace[0][0],orangeFace[0][2],yellowFace[0][1],yellowFace[1][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["F'", "L'", "U'", 'L', 'U', "L'", "U'", 'L', 'U', 'F']
            #OLL 48
            elif [greenFace[0][1],greenFace[0][2],redFace[0][0],redFace[0][2],blueFace[0][0],orangeFace[0][1],yellowFace[0][1],yellowFace[1][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'R', 'U', "R'", "U'", 'R', 'U', "R'", "U'", "F'"]
            #OLL 49
            elif [greenFace[0][0],greenFace[0][1],greenFace[0][2],redFace[0][0],orangeFace[0][1],orangeFace[0][2],yellowFace[0][1],yellowFace[1][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', "R'", 'F2', 'R', 'U2', 'R', 'U2', "R'", 'F']
            #OLL 50
            elif [greenFace[0][0],greenFace[0][1],blueFace[0][2],orangeFace[0][0],orangeFace[0][1],orangeFace[0][2],yellowFace[0][1],yellowFace[1][0]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", 'F', 'R2', "B'", 'R2', "F'", 'R2', 'B', "R'"]
            #OLL 51
            elif [greenFace[0][0],greenFace[0][1],blueFace[0][1],blueFace[0][2],orangeFace[0][0],orangeFace[0][2],yellowFace[1][0],yellowFace[1][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'U', 'R', "U'", "R'", 'U', 'R', "U'", "R'", "F'"]
            #OLL 52
            elif [greenFace[0][0],redFace[0][1],blueFace[0][2],orangeFace[0][0],orangeFace[0][1],orangeFace[0][2],yellowFace[0][1],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["R'", "U'", 'R', "U'", "R'", 'U', "F'", 'U', 'F', 'R']
            #OLL 53
            elif [redFace[0][0],redFace[0][1],redFace[0][2],blueFace[0][1],orangeFace[0][0],orangeFace[0][2],yellowFace[1][2],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["F'", 'L', 'F', "L'", 'U2', 'F2', "R'", "F'", 'R', "F'"]
            #OLL 54
            elif [redFace[0][0],redFace[0][2],blueFace[0][1],orangeFace[0][0],orangeFace[0][1],orangeFace[0][2],yellowFace[1][0],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', "R'", "F'", 'R', 'U2', 'F2', 'L', 'F', "L'", 'F']
            #OLL 55
            elif [redFace[0][0],redFace[0][1],redFace[0][2],orangeFace[0][0],orangeFace[0][1],orangeFace[0][2],yellowFace[0][1],yellowFace[2][1]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['R', 'U2', 'R2', "U'", 'R', "U'", "R'", 'U2', 'F', 'R', "F'"]
            #OLL 56
            elif [greenFace[0][1],redFace[0][0],redFace[0][2],blueFace[0][1],orangeFace[0][0],orangeFace[0][2],yellowFace[1][0],yellowFace[1][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ['F', 'R', 'U', "R'", "U'", 'R', "F'", 'L', 'F', "R'", "F'", "L'"]
            #OLL 57
            elif [greenFace[0][1],blueFace[0][1],yellowFace[0][0],yellowFace[0][2],yellowFace[1][0],yellowFace[1][2],yellowFace[2][0],yellowFace[2][2]] == ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']:
                requiredMoves = ["L'", 'R', 'U', "R'", "U'", 'L', "R'", 'F', 'R', "F'"]
            
            #If OLL is not complete, requiredMoves is either the necessary algorithm or an empty list, so either way, it can be performed.
            if yellowFace != [['yellow','yellow','yellow'],['yellow','yellow','yellow'],['yellow','yellow','yellow']]:
                for i in range(len(requiredMoves)):
                    solveMoves.append(requiredMoves[i])
                    moveList[requiredMoves[i]]()
            #If OLL is already complete, the loop does not need to continue.
            else:
                break
    
    #-=-=-=-=-=-=-=-=-=-=-=PLL=-=-=-=-=-=-=-=-=-=-=-
    requiredMoves = []
    #This dictionary contains every PLL algorithm, from http://algdb.net/puzzle/333/pll, as well as its reverse.
    PLLalgorithms = {
        #Aa
        ("R'", 'F', "R'", 'B2', 'R', "F'", "R'", 'B2', 'R2'):['R2', 'B2', 'R', 'F', "R'", 'B2', 'R', "F'", 'R'],
        #Ab
        ('R2', 'B2', 'R', 'F', "R'", 'B2', 'R', "F'", 'R'):["R'", 'F', "R'", 'B2', 'R', "F'", "R'", 'B2', 'R2'],
        #E
        ('L', "U'", 'R', 'D2', "R'", 'U', 'R', "L'", "U'", 'L', 'D2', "L'", 'U', "R'"):['R', "U'", 'L', 'D2', "L'", 'U', 'L', "R'", "U'", 'R', 'D2', "R'", 'U', "L'"],
        #F
        ("R'", 'U', 'R', "U'", 'R2', "F'", "U'", 'F', 'U', 'R', 'F', "R'", "F'", 'R2'):['R2', 'F', 'R', "F'", "R'", "U'", "F'", 'U', 'F', 'R2', 'U', "R'", "U'", 'R'],
        #Ga
        ('F2', 'R2', 'L2', 'U', 'R2', "U'", 'R2', 'D', 'R2', "D'", 'L2', 'F2'):['F2', 'L2', 'D', 'R2', "D'", 'R2', 'U', 'R2', "U'", 'L2', 'R2', 'F2'],
        #Gb
        ("R'", "U'", 'R', 'B2', 'D', "L'", 'U', 'L', "U'", 'L', "D'", 'B2', 'U2'):['U2', 'B2', 'D', "L'", 'U', "L'", "U'", 'L', "D'", 'B2', "R'", 'U', 'R'],
        #Gc
        ("U'", "L'", "R'", 'U2', 'L', 'R', 'F', "U'", 'B', 'U2', "F'", 'U', "B'"):['B', "U'", 'F', 'U2', "B'", 'U', "F'", "R'", "L'", 'U2', 'R', 'L', 'U'],
        #Gd
        ('R', 'U', "R'", "U'", 'D', 'R2', "U'", 'R', "U'", "R'", 'U', "R'", 'U', 'R2', "D'"):['D', 'R2', "U'", 'R', "U'", 'R', 'U', "R'", 'U', 'R2', "D'", 'U', 'R', "U'", "R'"],
        #H
        ('R2', 'U2', 'R', 'U2', 'R2', 'U2', 'R2', 'U2', 'R', 'U2', 'R2'):['R2', 'U2', "R'", 'U2', 'R2', 'U2', 'R2', 'U2', "R'", 'U2', 'R2'],
        #Ja
        ("R'", 'U', "L'", 'U2', 'R', "U'", "R'", 'U2', 'R', 'L'):["L'", "R'", 'U2', 'R', 'U', "R'", 'U2', 'L', "U'", 'R'],
        #Jb
        ('R', "U'", 'L', 'U2', "R'", 'U', 'R', 'U2', "L'", "R'"):['R', 'L', 'U2', "R'", "U'", 'R', 'U2', "L'", 'U', "R'"],
        #Na
        ('L', "U'", 'R', 'U2', "L'", 'U', "R'", 'L', "U'", 'R', 'U2', "L'", 'U', "R'"):['R', "U'", 'L', 'U2', "R'", 'U', "L'", 'R', "U'", 'L', 'U2', "R'", 'U', "L'"],
        #Nb
        ("R'", 'U', "L'", 'U2', 'R', "U'", 'L', "R'", 'U', "L'", 'U2', 'R', "U'", 'L'):["L'", 'U', "R'", 'U2', 'L', "U'", 'R', "L'", 'U', "R'", 'U2', 'L', "U'", 'R'],
        #Ra
        ('L', 'U2', "L'", 'U2', 'L', "F'", "L'", "U'", 'L', 'U', 'L', 'F', 'L2'):['L2', "F'", "L'", "U'", "L'", 'U', 'L', 'F', "L'", 'U2', 'L', 'U2', "L'"],
        #Rb
        ("R'", 'U2', 'R', 'U2', "R'", 'F', 'R', 'U', "R'", "U'", "R'", "F'", 'R2'):['R2', 'F', 'R', 'U', 'R', "U'", "R'", "F'", 'R', 'U2', "R'", 'U2', 'R'],
        #T
        ('F2', 'D', 'R2', "U'", 'R2', 'F2', "D'", 'L2', 'U', 'L2', "U'"):['U', 'L2', "U'", 'L2', 'D', 'F2', 'R2', 'U', 'R2', "D'", 'F2'],
        #Ua
        ('F2', "U'", 'L', "R'", 'F2', "L'", 'R', "U'", 'F2'):['F2', 'U', "R'", 'L', 'F2', 'R', "L'", 'U', 'F2'],
        #Ub
        ('F2', 'U', 'L', "R'", 'F2', "L'", 'R', 'U', 'F2'):['F2', "U'", "R'", 'L', 'F2', 'R', "L'", "U'", 'F2'],
        #V
        ('R2', "U'", 'B2', 'U', 'B2', 'R', "D'", 'R', 'D', "R'", 'U', 'R', "U'", 'R'):["R'", 'U', "R'", "U'", 'R', "D'", "R'", 'D', "R'", 'B2', "U'", 'B2', 'U', 'R2'],
        #Y
        ('F', 'U', "F'", 'R2', 'F', "U'", "F'", "U'", 'R2', 'U', 'R2', 'U', 'R2'):['R2', "U'", 'R2', "U'", 'R2', 'U', 'F', 'U', "F'", 'R2', 'F', "U'", "F'"],
        #Z
        ("F'", "L'", "U'", 'L', 'U', 'F', "R'", "U'", 'F', "R'", "F'", 'R', 'U', 'R'):["R'", "U'", "R'", 'F', 'R', "F'", 'U', 'R', "F'", "U'", "L'", 'U', 'L', 'F']
    }
    PLLsolved = False
    #If PLL is complete, an algorithm does not need to be performed.
    if compareList([greenFace[0],redFace[0],blueFace[0],orangeFace[0]],[['green','green','green'],['red','red','red'],['blue','blue','blue'],['orange','orange','orange']]) == False:
        #By cycling through every algorithm and undoing it if it's wrong, and then repeating from every orientation of the U face, the correct algorithm will eventually be found.
        PLLalgorithmsList = list(PLLalgorithms)
        for i in range(4):
            if PLLsolved == False:
                for algorithm in PLLalgorithmsList:
                    algorithmReverse = PLLalgorithms[algorithm]
                    for i in range(len(algorithm)):
                        moveList[algorithm[i]]()
                    if compareList([greenFace[0],redFace[0],blueFace[0],orangeFace[0]],[['green','green','green'],['red','red','red'],['blue','blue','blue'],['orange','orange','orange']]) == False:
                        for i in range(len(algorithmReverse)):
                            moveList[algorithmReverse[i]]()
                    else:
                        for i in range(len(algorithm)):
                            solveMoves.append(algorithm[i])
                        PLLsolved = True
                        break
            U()
            solveMoves.append('U')
    
    #Finally, turning the U face to be oriented correctly.
    if greenFace[0][0] == 'red':
        U()
        solveMoves.append('U')
    elif greenFace[0][0] == 'blue':
        U2()
        solveMoves.append('U2')
    elif greenFace[0][0] == 'orange':
        UP()
        solveMoves.append("U'")

    #The final part of unchecked validation is permutation parity.
    #If any unsolvable cube makes it this far, the permutation parity must be incorrect.
    parityValid = True
    if compareList([greenFace[0],redFace[0],blueFace[0],orangeFace[0]],[['green','green','green'],['red','red','red'],['blue','blue','blue'],['orange','orange','orange']]) == False:
        print('The cube has impossible permutation parity. Check that you have entered the cube properly, or else it may have been assembled incorrectly.')
        parityValid = False

    #Any two consecutive moves in the solve move list with the same base are shortened to a single move.
    tempSolveMoves = []
    for i in range(len(solveMoves)):
        try:
            #Check for whether they have the same base:
            if solveMoves[i][0] == tempSolveMoves[-1][0]:
                #If the moves are identical:
                if solveMoves[i] == tempSolveMoves[-1]:
                    try:
                        #If they are both 2 moves, then they cancel to 0.
                        if solveMoves[i][1] == '2' and tempSolveMoves[-1][1] == '2':
                            tempSolveMoves.pop()
                            continue
                        #If they are both prime moves, they add to 2.
                        else:
                            tempSolveMoves.pop()
                            tempSolveMoves.append(solveMoves[i][0]+'2')
                            continue
                    except:
                        #If they are both base moves, they add to 2.
                        tempSolveMoves.pop()
                        tempSolveMoves.append(solveMoves[i][0]+'2')
                        continue
                #If either of them are 2 moves, but not both:
                try:
                    #If one of them is a 2 move and the other is a prime move they cancel to a base move.
                    #This is guaranteed to break if one is a base move.
                    if compareList(["'","2"],[solveMoves[i][1],tempSolveMoves[-1][1]]) == True:
                        tempSolveMoves.pop()
                        tempSolveMoves.append(solveMoves[i][0])
                        continue
                except:
                    #If one of them is a 2 move and the other is a base move, they add to make a prime move.
                    try:
                        #By this point at least one is guaranteed to be a base move, so another try-except is required to check both using separate if statements.
                        #This is because a base move cannot be indexed to the 1 position, so an error will occur on one of these two checks.
                        if solveMoves[i][1] == '2':
                            tempSolveMoves.pop()
                            tempSolveMoves.append(solveMoves[i][0]+"'")
                            continue
                    except:
                        if tempSolveMoves[-1][1] == '2':
                            tempSolveMoves.pop()
                            tempSolveMoves.append(solveMoves[i][0]+"'")
                            continue
                #Anything that makes it to this point can only be a prime move with a base move, which cancel to 0.
                tempSolveMoves.pop()
            else:
                #If the two consecutive moves do not cancel each other out, nothing has to be done.
                tempSolveMoves.append(solveMoves[i])
        except:
            #The first move cannot be checked.
            tempSolveMoves.append(solveMoves[i])
    solveMoves = [i[:] for i in tempSolveMoves]
    if parityValid == True:
        print(" ".join(solveMoves))

def meanMoves():
    #This function takes an integer input for a number of solves that should be performed, and then does that many random solves, while counting how many moves each solve took.
    #At the end, it outputs the mean number of moves required for every solve.
    lengths = []
    for _ in range (int(input('How many solves would you like to test? '))):
        scrambleGen()
        solve()
        lengths.append(len(solveMoves))
    print(statistics.mean(lengths))

def main():
    scrambleGen()
    printCube()
    solve()
    printCube()

main()