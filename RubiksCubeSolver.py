import random

def printCube():
    print(greenFace)
    print(blueFace)
    print(redFace)
    print(orangeFace)
    print(whiteFace)
    print(yellowFace)

def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

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
    for key in scramble:
        moveList[key]()

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

def compareList(list1,list2):
    for corner in list1:
        if not corner in list2:
            return False
    return True

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
        pass

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
    
    #check permutation parity

def solve():
    #White Cross:
    #First it checks for which pieces have already been solved
    solveMoves = []
    whiteCrossSolved = False
    while whiteCrossSolved == False:
        if whiteFace[0][1] == 'white' and greenFace[2][1] == 'green':
            whiteCrossGreen = True
        if whiteFace[1][2] == 'white' and orangeFace[2][1] == 'orange':
            whiteCrossOrange = True
        if whiteFace[2][1] == 'white' and blueFace[2][1] == 'blue':
            whiteCrossBlue = True
        if whiteFace[1][0] == 'white' and redFace[2][1] == 'red':
            whiteCrossRed = True
        
        if whiteCrossGreen != None and whiteCrossOrange != None and whiteCrossBlue != None and whiteCrossRed != None:
            whiteCrossSolved = True
        
        clockwisePositions = ['green','red','blue','orange']
        if whiteCrossGreen == None:
            if whiteFace[0][1] == 'white':
                F2()
                solveMoves.append('F2')
                if clockwisePositions.index(greenFace[0][1]) == 1:
                    U()
                    L2()
                    solveMoves.append('U')
                    solveMoves.append('L2')
                elif clockwisePositions.index(greenFace[0][1]) == 2:
                    U2()
                    B2()
                    solveMoves.append('U2')
                    solveMoves.append('B2')
                elif clockwisePositions.index(greenFace[0][1]) == 3:
                    UP()
                    R2()
                    solveMoves.append("U'")
                    solveMoves.append('R2')
    print(solveMoves)                    

def main():
    cubeReset()
    colourConversion()

main()
