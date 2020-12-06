import random

#Outputs the current state of the cube as text
def printCube():
    print(greenFace)
    print(blueFace)
    print(redFace)
    print(orangeFace)
    print(whiteFace)
    print(yellowFace)

#Makes a list of the keys in a dictionary
#Takes a disctionary as an input, outputs a list
def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

#Compares whether one list contains variables that are all contained in another list, but not necessarily in the same order.
#Takes two lists as an input, outputs a boolean variable.
def compareList(list1,list2):
    for element in list1:
        if not element in list2:
            return False
    return True

def scrambleGen():
    moveList = {"U":U,"D":D,"F":F,"B":B,"R":R,"L":L,"U2":U2,"D2":D2,"F2":F2,"B2":B2,"R2":R2,"L2":L2,"U'":UP,"D'":DP,"F'":FP,"B'":BP,"R'":RP,"L'":LP}
    scramble = []
    for i in range(20):
        current = random.choice(getList(moveList))
        try:
            while current[0] == scramble[i-1][0] or current[0] == scramble[i-2][0]:
                current = random.choice(getList(moveList))
        except:
            pass
        scramble.append(current)
    print(" ".join(scramble))
    cubeReset()
    for move in scramble:
        moveList[move]()

def scrambleInput():
    moveList = {"U":U,"D":D,"F":F,"B":B,"R":R,"L":L,"U2":U2,"D2":D2,"F2":F2,"B2":B2,"R2":R2,"L2":L2,"U'":UP,"D'":DP,"F'":FP,"B'":BP,"R'":RP,"L'":LP}
    scramble = input('Input your custom scramble: ')
    scramble = scramble.split()
    cubeReset()
    for move in scramble:
        moveList[move]()

def cubeReset():
    global greenFace,blueFace,redFace,orangeFace,whiteFace,yellowFace
    greenFace = (["green","green","green"],["green","green","green"],["green","green","green"])
    blueFace = (["blue","blue","blue"],["blue","blue","blue"],["blue","blue","blue"])
    redFace = (["red","red","red"],["red","red","red"],["red","red","red"])
    orangeFace = (["orange","orange","orange"],["orange","orange","orange"],["orange","orange","orange"])
    whiteFace = (["white","white","white"],["white","white","white"],["white","white","white"])
    yellowFace = (["yellow","yellow","yellow"],["yellow","yellow","yellow"],["yellow","yellow","yellow"])

def U():
    tempGreenFace = [i[:] for i in greenFace]
    tempBlueFace = [i[:] for i in blueFace]
    tempRedFace = [i[:] for i in redFace]
    tempOrangeFace = [i[:] for i in orangeFace]
    tempYellowFace = [i[:] for i in yellowFace]
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

def U2():
    [U() for i in range(2)]

def UP():
    [U() for i in range(3)]

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

def D2():
    [D() for i in range(2)]

def DP():
    [D() for i in range(3)]

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

def F2():
    [F() for i in range(2)]

def FP():
    [F() for i in range(3)]

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

def B2():
    [B() for i in range(2)]

def BP():
    [B() for i in range(3)]

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

def R2():
    [R() for i in range(2)]

def RP():
    [R() for i in range(3)]

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

def L2():
    [L() for i in range(2)]

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

def validation():
    cubeState = []
    cubeState.extend([greenFace,blueFace,redFace,orangeFace,whiteFace,yellowFace])
    greenCount = 0
    blueCount = 0
    redCount = 0
    orangeCount = 0
    whiteCount = 0
    yellowCount = 0
    for face in cubeState:
        for colour in face:
            greenCount = greenCount + colour.count("green")
            blueCount = blueCount + colour.count("blue")
            redCount = redCount + colour.count("red")
            orangeCount = orangeCount + colour.count("orange")
            whiteCount = whiteCount + colour.count("white")
            yellowCount = yellowCount + colour.count("yellow")
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
    
    cornerList = (['yellow','red','green'],['yellow','orange','green'],['yellow','orange','blue'],['yellow','red','blue'],['white','red','green'],['white','orange','green'],['white','orange','blue'],['white','red','blue'])
    corners = [[yellowFace[2][0],redFace[0][2],greenFace[0][0]],[yellowFace[2][2],orangeFace[0][0],greenFace[0][2]],[yellowFace[0][2],orangeFace[0][2],blueFace[0][0]],[yellowFace[0][0],redFace[0][0],blueFace[0][2]],[whiteFace[0][0],redFace[2][2],greenFace[2][0]],[whiteFace[0][2],orangeFace[2][0],greenFace[2][2]],[whiteFace[2][2],orangeFace[2][2],blueFace[2][0]],[whiteFace[2][0],redFace[2][0],blueFace[2][2]]]
    cornerCheck = [False for i in range(8)]
    for i in range (8):
        for j in range (8):
            if compareList(cornerList[i],corners[j]) == True:
                cornerCheck[i] = True
    for i in range (8):
        if cornerCheck[i] == False:
            print("The cube is missing a corner with the colours "+cornerList[i][0]+", "+cornerList[i][1]+", and "+cornerList[i][2]+".")

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
    
    orientationList = {('green','yellow','orange'):['blue','white','red'],('green','red','yellow'):['blue','orange','white'],('green','white','red'):['blue','yellow','orange'],('green','orange','white'):['blue','red','yellow'],('blue','yellow','red'):['green','white','orange'],('blue','orange','yellow'):['green','red','white'],('blue','white','orange'):['green','yellow','red'],('blue','red','white'):['green','orange','yellow'],('red','yellow','green'):['orange','white','blue'],('red','blue','yellow'):['orange','green','white'],('red','white','blue'):['orange','yellow','green'],('red','green','white'):['orange','blue','yellow'],('orange','yellow','blue'):['red','white','green'],('orange','green','yellow'):['red','blue','white'],('orange','white','green'):['red','yellow','blue'],('orange','blue','white'):['red','green','yellow'],('white','green','orange'):['yellow','blue','red'],('white','red','green'):['yellow','orange','blue'],('white','blue','red'):['yellow','green','orange'],('white','orange','blue'):['yellow','red','green'],('yellow','green','red'):['white','blue','orange'],('yellow','orange','green'):['white','red','blue'],('yellow','blue','orange'):['white','green','red'],('yellow','red','blue'):['white','orange','green']}
    currentOrientation = (greenFace[1][1],yellowFace[1][1],orangeFace[1][1])
    try:
        if [blueFace[1][1],whiteFace[1][1],redFace[1][1]] != orientationList[currentOrientation]:
            print('The cube is invalid. Please check whether you have entered the centre pieces correctly.')
    except:
        print('The cube is invalid. Please check whether you have entered the centre pieces correctly.')

    orientedCount = 0
    for colour in [greenFace[0][2],redFace[0][2],blueFace[0][2],orangeFace[0][2],greenFace[2][0],redFace[2][0],blueFace[2][0],orangeFace[2][0]]:
        if colour == 'white' or colour == 'yellow':
            orientedCount = orientedCount + 1
    for colour in [greenFace[0][0],redFace[0][0],blueFace[0][0],orangeFace[0][0],greenFace[2][2],redFace[2][2],blueFace[2][2],orangeFace[2][2]]:
        if colour == 'white' or colour == 'yellow':
            orientedCount = orientedCount + 2
    if orientedCount % 3 != 0:
        print('The cube has a twisted corner. Check that you have entered the corners correctly, or else they may be twisted.')

    orientedCount = 0
    for edge in [[yellowFace[2][1],greenFace[0][1]],[yellowFace[1][2],orangeFace[0][1]],[yellowFace[0][1],blueFace[0][1]],[yellowFace[1][0],redFace[0][1]],[greenFace[1][2],orangeFace[1][0]],[blueFace[1][0],orangeFace[1][2]],[blueFace[1][2],redFace[1][0]],[greenFace[1][0],redFace[1][2]],[whiteFace[0][1],greenFace[2][1]],[whiteFace[1][2],orangeFace[2][1]],[whiteFace[2][1],blueFace[2][1]],[whiteFace[1][0],redFace[2][1]]]:
        if edge[0] in ['yellow','white']:
            orientedCount = orientedCount + 1
        if edge[0] in ['blue','green'] and edge[1] in ['red','orange']:
            orientedCount = orientedCount + 1
    if orientedCount % 2 != 0:
        print('The cube has a twisted edge. Check that you have entered the edges correctly, or else they may be twisted.')
    
    #Permutation parity is checked later in the solve, it's just much easier to program that way.

def solve():
    moveList = {"U":U,"D":D,"F":F,"B":B,"R":R,"L":L,"U2":U2,"D2":D2,"F2":F2,"B2":B2,"R2":R2,"L2":L2,"U'":UP,"D'":DP,"F'":FP,"B'":BP,"R'":RP,"L'":LP}
    #-=-=-=-=-=-=-=-=-=-=-=WHITE CROSS=-=-=-=-=-=-=-=-=-=-=-
    #First it checks for which pieces have already been solved.
    solveMoves = []
    whiteCrossSolved = [False,False,False,False]
    while whiteCrossSolved != [True,True,True,True]:
        if whiteFace[0][1] == 'white' and greenFace[2][1] == 'green':
            whiteCrossSolved[0] = True
        if whiteFace[1][0] == 'white' and redFace[2][1] == 'red':
            whiteCrossSolved[1] = True
        if whiteFace[2][1] == 'white' and blueFace[2][1] == 'blue':
            whiteCrossSolved[2] = True
        if whiteFace[1][2] == 'white' and orangeFace[2][1] == 'orange':
            whiteCrossSolved[3] = True

        #Solving the side face bottom slice.
        if greenFace[2][1] == 'white':
            possibleMoves = {'green':["F'",'D',"R'","D'"],'red':['F','L'],'blue':["F'","D'","R'",'D'],'orange':["F'","R'"]}
            requiredMoves = possibleMoves[whiteFace[0][1]]
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()

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
    """
    #-=-=-=-=-=-=-=-=-=-=-=F2L=-=-=-=-=-=-=-=-=-=-=-
    #First it checks for which pairs have already been solved.
    F2Lsolved = [False,False,False,False]
    while F2Lsolved != [True,True,True,True]:
        if greenFace[1][0] == 'green' and greenFace[2][0] == 'green' and redFace[1][2] == 'red' and redFace[2][2] == 'red' and whiteFace[0][0] == 'white':
            F2Lsolved[0] = True
        if redFace[1][0] == 'red' and redFace[2][0] == 'red' and blueFace[1][2] == 'blue' and blueFace[2][2] == 'blue' and whiteFace[2][0] == 'white':
            F2Lsolved[1] = True
        if blueFace[1][0] == 'blue' and blueFace[2][0] == 'blue' and orangeFace[1][2] == 'orange' and orangeFace[2][2] == 'orange' and whiteFace[2][2] == 'white':
            F2Lsolved[2] = True
        if orangeFace[1][0] == 'orange' and orangeFace[2][0] == 'orange' and greenFace[1][2] == 'green' and greenFace[2][2] == 'green' and whiteFace[0][2] == 'white':
            F2Lsolved[3] = True

        #For the case when there is an unsolved corner in the green-red-white corner:
        if 'white' in [greenFace[2][0],redFace[2][2],whiteFace[0][0]] and F2Lsolved[0] == False:
            #Three moves required to take it out.
            requiredMoves = ["L'","U'",'L']
            for i in range(len(requiredMoves)):
                solveMoves.append(requiredMoves[i])
                moveList[requiredMoves[i]]()
            #
    """
    #Any two consecutive moves in the solve move list with the same base are shortened to a single move.
    tempSolveMoves = []
    for i in range(len(solveMoves)):
        try:
            #Check for whether they have the same base:
            if solveMoves[i][0] == tempSolveMoves[-1][0]:
                #If the moves are indentical:
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
    print(" ".join(solveMoves))

def main():
    scrambleGen()
    solve()

main()
