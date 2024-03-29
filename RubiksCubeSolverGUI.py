import pygame, time, os
from pygame.locals import *
from RubiksCubeSolver import *


#Class to represent facelets on the cube.
class Facelet:
    #Initialises facelet by setting attributes and drawing.
    def __init__(self,surface,colour,colourIndex,points):
        self.surface = surface
        self.points = points
        self.colour = colour
        self.colourIndex = colourIndex
        #Coordinates are rounded converted to integers to avoid using float pixels values.
        for coords in self.points:
            coords[0] = int(round(coords[0]))
            coords[1] = int(round(coords[1]))
        #Facelet is drawn.
        pygame.draw.polygon(self.surface,self.colour,self.points)

        #Temporary empty surface is created, used to store the facelet and nothing else, to create a mask. Never displayed.
        offscreen = pygame.Surface(self.surface.get_size())
        offscreen = offscreen.convert()
        #Black is the default background and is set as the colourkey, which the mask function uses to set as the off bits.
        offscreen.set_colorkey((0,0,0))
        #Facelet is drawn onto this surface.
        pygame.draw.polygon(offscreen,self.colour,self.points)
        #Surface is used to make the mask.
        self.mask = pygame.mask.from_surface(offscreen)

    #Updates the facelet to its new colour.
    def update(self,currentState):
        colour_dict = {"green":(0,255,0),"blue":(0,0,255),"red":(255,0,0),"orange":(255,128,0),"white":(255,255,255),"yellow":(255,255,0)}
        self.colour = colour_dict[currentState[self.colourIndex[0]][self.colourIndex[1]][self.colourIndex[2]]]
        pygame.draw.polygon(self.surface,self.colour,self.points)

    #Checks if the facelet has been clicked on, and changes its colour.
    def clickCheck(self,currentState):
        #This dictionary is used to convert RGB values to words so that the solve function can make sense of it.
        reverse_colour_dict = {(0,255,0):"green",(0,0,255):"blue",(255,0,0):"red",(255,128,0):"orange",(255,255,255):"white",(255,255,0):"yellow"}
        #If the facelet exists (mask = 1) at the position of the mouse cursor, it has been clicked on.
        if self.mask.get_at(pygame.mouse.get_pos()) == 1:
            #List of the possible colours in RGB form.
            colourList = [(0,255,0),(0,0,255),(255,0,0),(255,128,0),(255,255,255),(255,255,0)]
            #The colour of the facelet is changed to the next colour in the list.
            try:
                self.colour = colourList[colourList.index(self.colour) + 1]
            #If the index is out of range, the cycle wraps around and goes back by 5 instead of forward by 1.
            except:
                self.colour = colourList[colourList.index(self.colour) - 5]
            #Facelet is redrawn with its new colour.
            pygame.draw.polygon(self.surface,self.colour,self.points)
            #The cube's state is updated to hold the new information.
            currentState[self.colourIndex[0]][self.colourIndex[1]][self.colourIndex[2]] = reverse_colour_dict[self.colour]
        #Returns the cube's state to update it.
        return currentState


#Class for displaying text at the top of the screen, used for scrambles and validation messages.
class Text:
    #Renders and blits the text.
    #The optional down parameter moves the text down by a certain number of lines, which is useful when a lot of text is being shown.
    #The optional colour parameter is to change the colour of the text, otherwise it is black by default.
    #The optional title parameter is to make the text bold and underlined.
    def __init__(self,message,surface,down = 0,textColour = (0,0,0),customPos = False,title = False):
        self.surface = surface
        #Font is generated.
        font = pygame.font.Font(None, int(round(surface.get_height()/22.5)))
        #If the text is a title, font is generated differently.
        if title == True:
            font.bold = True
            font.underline = True
        self.text = font.render(message, 1, textColour, (128,128,128))
        #self.rect is the rectangle of space that the text in.
        self.rect = self.text.get_rect(center=(int(round(surface.get_width()/2)),int(round(surface.get_height()/10)) + (down * int(round(surface.get_height()/22.5)))))
        #self.pos is the top left corner of the text's rectangle.
        self.pos = int(round(surface.get_width()/2)) - int(round(self.rect.width/2)),int(round(surface.get_height()/10)) - int(round(self.rect.height/2)) + (down * int(round(surface.get_height()/22.5)))
        #If a custom position is passed in, the text's top left corner will be in that position.
        #If the text does not have a custom position, it is automatically placed in the top middle.
        if customPos != False:
            self.pos = customPos
        surface.blit(self.text,self.pos)

    #Hides the text so that new text can be drawn.
    def hide(self):
        self.surface.fill((128,128,128),self.rect)

    #Shows text when it has been hidden.
    def showText(self):
        self.surface.blit(self.text,self.pos)


def mainGUI():
    #Pygame is initialised.
    pygame.init()

    #Dictionary containing all the possible colours and their corresponding RGB values.
    colour_dict = {"green":(0,255,0),"blue":(0,0,255),"red":(255,0,0),"orange":(255,128,0),"white":(255,255,255),"yellow":(255,255,0)}

    #Creates and displays a window
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Rubik's Cube Solver")

    #Sets the icon
    icon = pygame.image.load(os.path.join('', 'RubiksCube.png'))
    pygame.display.set_icon(icon)

    #Draws a plain black background for the whole window size.
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((128,128,128))
    screen.blit(background,(0,0))

    #Initial screen shows instructions and resolution input.
    #Each instruction is a separate text object, each one is shown below the last.
    text1 = Text("List of controls:", screen, -1, title = True)
    text2 = Text("Click on the cube to change its colours.", screen, 1)
    text3 = Text("Escape = Exit", screen, 2)
    text4 = Text("Space = Scramble cube", screen, 3)
    text5 = Text("X, Y, Z = Rotate cube around X, Y, or Z axis", screen, 4)
    text6 = Text("R = Reset cube", screen, 5)
    text6 = Text("S = Enter solve mode", screen, 6)
    text7 = Text("During solve mode:", screen, 8,  title = True)
    text8 = Text("Right arrow key = Show next move", screen, 10)
    text9 = Text("Left arrow key = Undo last move", screen, 11)
    text10 = Text("Up arrow key = Show solve automatically", screen, 12)
    text11 = Text("Down arrow key = Undo solve automatically", screen, 13)
    text12 = Text("S = Exit solve mode", screen, 14)
    text13 = Text("(Optional) Type to enter custom window resolution - values too large will default to 720", screen, 16)
    text14 = Text("Height (Pixels) = ", screen, 17)
    text15 = Text("Press enter to proceed.", screen, 19)

    #Display is updated to show text.
    pygame.display.flip()

    #Loop that keeps instructions open.
    #Going keeps track of whether the program should be running.
    going = True
    #Waiting keeps track of whether the instructions should be showing.
    waiting = True
    #Resolution keeps track of the current resolution input.
    resolution = 720
    while waiting == True:
        for event in pygame.event.get():
            #If the user presses quit, the program ends.
            if event.type == QUIT:
                waiting = False
                going = False
            #If the user presses a key, a new selection happens.
            elif event.type == KEYDOWN:
                #If the user presses escape, the program ends.
                if event.key == K_ESCAPE:
                    waiting = False
                    going = False
                #If the user presses enter, the cube can be shown.
                elif event.key == K_RETURN:
                    waiting = False
                #Any other key is a resolution input.
                else:
                    #If backspace is pressed, the last digit of resolution is removed.
                    if event.key == K_BACKSPACE:
                        #Last digit of value is removed.
                        resolution = resolution // 10
                        
                        screen.blit(background,(0,0))
                        pygame.display.update(text14.rect)
                    #If any number is pressed, it is added to the end of the resolution.
                    elif event.key == K_0:
                        resolution = int(str(resolution) + "0")

                    elif event.key == K_1:
                        resolution = int(str(resolution) + "1")

                    elif event.key == K_2:
                        resolution = int(str(resolution) + "2")

                    elif event.key == K_3:
                        resolution = int(str(resolution) + "3")

                    elif event.key == K_4:
                        resolution = int(str(resolution) + "4")

                    elif event.key == K_5:
                        resolution = int(str(resolution) + "5")

                    elif event.key == K_6:
                        resolution = int(str(resolution) + "6")

                    elif event.key == K_7:
                        resolution = int(str(resolution) + "7")

                    elif event.key == K_8:
                        resolution = int(str(resolution) + "8")

                    elif event.key == K_9:
                        resolution = int(str(resolution) + "9")

            if len(str(resolution)) > 10:
                resolution = resolution // 10

            text14 = Text("Height (Pixels) = "+str(resolution),screen, 17)
            pygame.display.update(text14.rect)

    #If a resolution of 0 is given, then it is set back to its default value.
    if resolution == 0:
        resolution = 720
    #If resolution is too high, then it is set back to its default value.
    elif resolution > 4320:
        resolution = 720

    #Window is updated with new resolution.
    screen = pygame.display.set_mode((round(resolution*16/9), resolution))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((128,128,128))

    #If the user has not quit, the cube is displayed.
    if going == True:
        #Instructions are covered by a new background.
        screen.blit(background,(0,0))

        #Draws the cube.
        #Each object belonging to the facelet class is just a polygon with a specified colour and position.
        #The faceletTop objects represent every facelet on the yellow face in order, starting at 0,0 and then going through every facelet row by row.
        faceletTop1 = Facelet(screen,colour_dict[yellowFace[0][0]],[5,0,0],[[screen.get_width()/2,screen.get_height()/2*7/12],[screen.get_width()/2*419/384,screen.get_height()/2*47/72],[screen.get_width()/2,screen.get_height()/2*13/18],[screen.get_width()/2*349/384,screen.get_height()/2*47/72]])
        faceletTop2 = Facelet(screen,colour_dict[yellowFace[0][1]],[5,0,1],[faceletTop1.points[1],[screen.get_width()/2*227/192,faceletTop1.points[2][1]],[faceletTop1.points[1][0],screen.get_height()/2*19/24],faceletTop1.points[2]])
        faceletTop3 = Facelet(screen,colour_dict[yellowFace[0][2]],[5,0,2],[faceletTop2.points[1],[screen.get_width()/2*163/128,faceletTop2.points[2][1]],[faceletTop2.points[1][0],screen.get_height()/2*31/36],faceletTop2.points[2]])
        faceletTop4 = Facelet(screen,colour_dict[yellowFace[1][0]],[5,1,0],[faceletTop1.points[3],faceletTop1.points[2],[faceletTop1.points[3][0],faceletTop2.points[2][1]],[screen.get_width()/2*157/192,faceletTop1.points[2][1]]])
        faceletTop5 = Facelet(screen,colour_dict[yellowFace[1][1]],[5,1,1],[faceletTop1.points[2],faceletTop2.points[2],[screen.get_width()/2,faceletTop3.points[2][1]],faceletTop4.points[2]])
        faceletTop6 = Facelet(screen,colour_dict[yellowFace[1][2]],[5,1,2],[faceletTop2.points[2],faceletTop3.points[2],[faceletTop2.points[0][0],screen.get_height()/2*67/72],faceletTop5.points[2]])
        faceletTop7 = Facelet(screen,colour_dict[yellowFace[2][0]],[5,2,0],[faceletTop4.points[3],faceletTop4.points[2],[faceletTop4.points[3][0],faceletTop3.points[2][1]],[screen.get_width()/2*93/128,faceletTop3.points[1][1]]])
        faceletTop8 = Facelet(screen,colour_dict[yellowFace[2][1]],[5,2,1],[faceletTop4.points[2],faceletTop5.points[2],[faceletTop4.points[0][0],faceletTop6.points[2][1]],faceletTop7.points[2]])
        faceletTop9 = Facelet(screen,colour_dict[yellowFace[2][2]],[5,2,2],[faceletTop5.points[2],faceletTop6.points[2],[screen.get_width()/2,screen.get_height()/2],faceletTop8.points[2]])

        #faceletLeft objects work exactly the same as faceletTop, but instead represent the green face.
        faceletLeft1 = Facelet(screen,colour_dict[greenFace[0][0]],[0,0,0],[faceletTop7.points[3],faceletTop7.points[2],[faceletTop7.points[0][0],screen.get_height()/2*77/72],[screen.get_width()/2*93/128,screen.get_height()/2]])
        faceletLeft2 = Facelet(screen,colour_dict[greenFace[0][1]],[0,0,1],[faceletTop8.points[3],faceletTop8.points[2],[faceletTop8.points[0][0],screen.get_height()/2*41/36],faceletLeft1.points[2]])
        faceletLeft3 = Facelet(screen,colour_dict[greenFace[0][2]],[0,0,2],[faceletTop9.points[3],faceletTop9.points[2],[faceletTop9.points[0][0],screen.get_height()/2*29/24],faceletLeft2.points[2]])
        faceletLeft4 = Facelet(screen,colour_dict[greenFace[1][0]],[0,1,0],[faceletLeft1.points[3],faceletLeft1.points[2],[faceletLeft1.points[1][0],screen.get_height()/2*23/18],[faceletLeft1.points[0][0],faceletLeft3.points[2][1]]])
        faceletLeft5 = Facelet(screen,colour_dict[greenFace[1][1]],[0,1,1],[faceletLeft2.points[3],faceletLeft2.points[2],[faceletLeft2.points[1][0],screen.get_height()/2*97/72],faceletLeft4.points[2]])
        faceletLeft6 = Facelet(screen,colour_dict[greenFace[1][2]],[0,1,2],[faceletLeft3.points[3],faceletLeft3.points[2],[faceletLeft3.points[1][0],screen.get_height()/2*17/12],faceletLeft5.points[2]])
        faceletLeft7 = Facelet(screen,colour_dict[greenFace[2][0]],[0,2,0],[faceletLeft4.points[3],faceletLeft4.points[2],[faceletLeft4.points[1][0],screen.get_height()/2*107/72],[faceletLeft1.points[0][0],faceletLeft6.points[2][1]]])
        faceletLeft8 = Facelet(screen,colour_dict[greenFace[2][1]],[0,2,1],[faceletLeft5.points[3],faceletLeft5.points[2],[faceletLeft5.points[1][0],screen.get_height()/2*14/9],faceletLeft7.points[2]])
        faceletLeft9 = Facelet(screen,colour_dict[greenFace[2][2]],[0,2,2],[faceletLeft6.points[3],faceletLeft6.points[2],[faceletLeft6.points[1][0],screen.get_height()/2*13/8],faceletLeft8.points[2]])

        #faceletRight objects work exactly the same as faceletTop and faceletRight, but instead represent the orange face.
        faceletRight1 = Facelet(screen,colour_dict[orangeFace[0][0]],[3,0,0],[faceletTop9.points[2],faceletTop9.points[1],[faceletTop1.points[1][0],faceletLeft3.points[3][1]],faceletLeft3.points[2]])
        faceletRight2 = Facelet(screen,colour_dict[orangeFace[0][1]],[3,0,1],[faceletTop9.points[1],faceletTop6.points[1],[faceletTop2.points[1][0],faceletLeft2.points[3][1]],faceletRight1.points[2]])
        faceletRight3 = Facelet(screen,colour_dict[orangeFace[0][2]],[3,0,2],[faceletTop6.points[1],faceletTop3.points[1],[faceletTop3.points[1][0],faceletLeft1.points[3][1]],faceletRight2.points[2]])
        faceletRight4 = Facelet(screen,colour_dict[orangeFace[1][0]],[3,1,0],[faceletRight1.points[3],faceletRight1.points[2],[faceletTop1.points[1][0],faceletLeft6.points[3][1]],faceletLeft6.points[2]])
        faceletRight5 = Facelet(screen,colour_dict[orangeFace[1][1]],[3,1,1],[faceletRight2.points[3],faceletRight2.points[2],[faceletTop2.points[1][0],faceletLeft5.points[3][1]],faceletRight4.points[2]])
        faceletRight6 = Facelet(screen,colour_dict[orangeFace[1][2]],[3,1,2],[faceletRight3.points[3],faceletRight3.points[2],[faceletTop3.points[1][0],faceletLeft4.points[3][1]],faceletRight5.points[2]])
        faceletRight7 = Facelet(screen,colour_dict[orangeFace[2][0]],[3,2,0],[faceletRight4.points[3],faceletRight4.points[2],[faceletTop1.points[1][0],faceletLeft9.points[3][1]],faceletLeft9.points[2]])
        faceletRight8 = Facelet(screen,colour_dict[orangeFace[2][1]],[3,2,1],[faceletRight5.points[3],faceletRight5.points[2],[faceletTop2.points[1][0],faceletLeft8.points[3][1]],faceletRight7.points[2]])
        faceletRight9 = Facelet(screen,colour_dict[orangeFace[2][2]],[3,2,2],[faceletRight6.points[3],faceletRight6.points[2],[faceletTop3.points[1][0],faceletLeft7.points[3][1]],faceletRight8.points[2]])

        #Full facelet list that can be used to control all facelets together.
        faceletList = [faceletTop1,faceletTop2,faceletTop3,faceletTop4,faceletTop5,faceletTop6,faceletTop7,faceletTop8,faceletTop9,faceletLeft1,faceletLeft2,faceletLeft3,faceletLeft4,faceletLeft5,faceletLeft6,faceletLeft7,faceletLeft8,faceletLeft9,faceletRight1,faceletRight2,faceletRight3,faceletRight4,faceletRight5,faceletRight6,faceletRight7,faceletRight8,faceletRight9]

        #The grid is drawn onto the cube to make the facelets more distinguishable.
        pygame.draw.lines(screen,(0,0,0),False,[faceletLeft7.points[3],faceletRight7.points[3],faceletRight9.points[2],faceletRight6.points[2],faceletRight4.points[3],faceletLeft4.points[3],faceletLeft1.points[3],faceletLeft3.points[2],faceletRight3.points[2],faceletRight3.points[1],faceletRight1.points[0],faceletLeft1.points[0],faceletTop1.points[0],faceletTop3.points[1],faceletRight9.points[2],faceletRight9.points[3],faceletTop3.points[2],faceletTop1.points[3],faceletTop4.points[3],faceletTop6.points[2],faceletRight8.points[3],faceletRight7.points[3],faceletTop9.points[2],faceletTop8.points[2],faceletLeft8.points[2],faceletLeft8.points[3],faceletTop8.points[3],faceletTop7.points[3],faceletLeft7.points[3],faceletLeft7.points[2],faceletTop7.points[2],faceletTop2.points[0],faceletTop2.points[1],faceletTop8.points[2]],int(round(screen.get_height()/180)))

        #Updates the display.
        pygame.display.flip()

        #Resets cubeState.
        cubeState = cubeReset()

        #Some invisible text to stop program from breaking the first time it tries to hide the text.
        text = Text('',screen)

    #Keeps track of whether the solve is currently being displayed.
    solving = False
    #Keeps track of how many moves have been displayed in this solve.
    moveCount = 0
    #Window continues to be displayed and repeatedly updated while the condition is true.
    while going == True:
        #If the solve is not being shown, the program continues as normal.
        if solving == False:
            #Every event in the event list is cycled through and functions are carried out depending on the event.
            for event in pygame.event.get():
                #If the user presses quit, the program ends.
                if event.type == QUIT:
                    going = False
                #If the user presses escape, the program ends.
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    going = False

                #If the user presses space, the cube is scrambled.
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    #Scramble is generated and made into a list.
                    scrambleMoves = scrambleGen()
                    #The cube needs to be in its default state before the scramble is performed.
                    cubeReset()
                    #Cube is updated to contain the scramble.
                    cubeState = moveInput(scrambleMoves)
                    #Another cube is being drawn, so the screen has to be reset by redrawing the background.
                    screen.blit(background,(0,0))
                    #Scramble moves are displayed to the user.
                    text = Text(scrambleMoves, screen)

                #If the user presses R, the cube is reset.
                elif event.type == KEYDOWN and event.key == K_r:
                    #Cube state is set to a solved cube.
                    cubeState = cubeReset()
                    text.hide()

                #If the user clicks, the facelet that is clicked on cycles to a new colour.
                elif event.type == MOUSEBUTTONUP:
                    #Every facelet is checked for whether it has been clicked on and the correct one is updated.
                    for facelets in faceletList:
                        cubeState = facelets.clickCheck(cubeState)

                #If the user presses S, the cube is solved.
                elif event.type == KEYDOWN and event.key == K_s:
                    #This dictionary contains every possible move and the name of the function it corresponds to.
                    moveList = {'U':U,'D':D,'F':F,'B':B,'R':R,'L':L,'U2':U2,'D2':D2,'F2':F2,'B2':B2,'R2':R2,'L2':L2,"U'":UP,"D'":DP,"F'":FP,"B'":BP,"R'":RP,"L'":LP}
                    #If there is text displayed, it needs to be hidden.
                    text.hide()
                    #The cube is validated for whether it is possible to solve.
                    #If the validation returns a boolean and a string, they are both stored.
                    try:
                        valid, message = validation()
                    #If the validation returns only a boolean, it is stored.
                    except:
                        valid = validation()
                    #If the cube is valid, it can be solved.
                    if valid == True:
                        #Colours are converted and the list of moves for the solve is generated.
                        solveMoves, parityValid = colourConversion(cubeState)
                        #If  permutation parity is also valid, the cube can be solved.
                        if parityValid == True:
                            #Solve is reversed so that the cube is back in its scrambled form before the solve is displayed to the user.
                            cubeState = moveInput(moveReversal(solveMoves))
                            #The solve can now be displayed.
                            solving = True
                            #The solve moves are split into shorter 30 move length lists that can fit on the screen.
                            splitSolveMoves = []
                            tempSolveMoves = []
                            for move in solveMoves:
                                #Every 30 moves are added to a list as a list.
                                if len(tempSolveMoves) == 30:
                                    splitSolveMoves.append(tempSolveMoves)
                                    tempSolveMoves = []
                                tempSolveMoves.append(move)
                                #If this is the last move in the list being checked, then the list needs to be added to the overall list despite being less than 30 moves in length.
                                if (len(splitSolveMoves) * 30 + len(tempSolveMoves)) == len(solveMoves):
                                    splitSolveMoves.append(tempSolveMoves)
                            #The split solve lists are then displayed and made into a list to easily manipulate at the same time.
                            solveText = []
                            for i in range(len(splitSolveMoves)):
                                displayedMoves = (" ".join(splitSolveMoves[i]))
                                solveText.append(Text(displayedMoves,screen,i))
                        #If permutation parity is invalid, the cube cannot be solved.
                        else:
                            #Cube is changed back to what it was before the attempted solve.
                            cubeState = moveInput(moveReversal(solveMoves))
                            valid = False
                            message = 'The cube has impossible permutation parity. Check that you have entered the cube properly.'
                    #If the cube is not solvable, a message is displayed letting the user know what is wrong.
                    if valid == False:
                        #If there is already text displayed, it needs to be hidden.
                        text.hide()
                        text = Text(message,screen)

                #If the user presses X, the cube is turned on the x-axis.
                elif event.type == KEYDOWN and event.key == K_x:
                    x()
                #If the user presses Y, the cube is turned on the y-axis.
                elif event.type == KEYDOWN and event.key == K_y:
                    y()
                #If the user presses Z, the cube is turned on the z-axis.
                elif event.type == KEYDOWN and event.key == K_z:
                    z()

                #The facelets are constantly updated to show how they look after any change to the cube happens.
                for facelets in faceletList:
                    facelets.update(cubeState)
                #The grid is drawn onto the cube to make the facelets more distinguishable.
                pygame.draw.lines(screen,(0,0,0),False,[faceletLeft7.points[3],faceletRight7.points[3],faceletRight9.points[2],faceletRight6.points[2],faceletRight4.points[3],faceletLeft4.points[3],faceletLeft1.points[3],faceletLeft3.points[2],faceletRight3.points[2],faceletRight3.points[1],faceletRight1.points[0],faceletLeft1.points[0],faceletTop1.points[0],faceletTop3.points[1],faceletRight9.points[2],faceletRight9.points[3],faceletTop3.points[2],faceletTop1.points[3],faceletTop4.points[3],faceletTop6.points[2],faceletRight8.points[3],faceletRight7.points[3],faceletTop9.points[2],faceletTop8.points[2],faceletLeft8.points[2],faceletLeft8.points[3],faceletTop8.points[3],faceletTop7.points[3],faceletLeft7.points[3],faceletLeft7.points[2],faceletTop7.points[2],faceletTop2.points[0],faceletTop2.points[1],faceletTop8.points[2]],int(round(screen.get_height()/180)))

                #The display is updated at the end of every loop.
                pygame.display.flip()

        #If the cube is solving, the solve is displayed.
        elif solving == True and len(solveMoves) > 0:
            #The actions that have to be done when the solve is being displayed are different from what is normally done.
            for event in pygame.event.get():
                #If the user presses quit, the program ends.
                if event.type == QUIT:
                    going = False
                #If the user presses escape, the program ends.
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    going = False

                #Solve is stopped when the S key is pressed again.
                elif event.type == KEYDOWN and event.key == K_s:
                    #Solve is no longer being displayed.
                    solving = False
                    moveCount = 0
                    #Solve moves are hidden.
                    for text in solveText:
                        text.hide()

                #If the user presses the right arrow key, the next move in the solve is performed.
                elif event.type == KEYDOWN and event.key == K_RIGHT:
                    #Checks if every move has been shown.
                    if moveCount != len(solveMoves):
                        #The current move's function is called to change the cube's state.
                        moveList[solveMoves[moveCount]]()

                        #Red text covers the solve moves to show which moves have already been done.
                        #Loops for how many lines of moves have already been done, plus one for the current line.
                        for i in range(moveCount // 30 + 1):
                            #For the number of lines of moves that are fully done, each line is written again in red.
                            for j in range(i):
                                displayedMoves = (" ".join(splitSolveMoves[j]))
                                Text(displayedMoves,screen,j,(255,0,0))
                            #Checks if this is the last loop.
                            if i == moveCount // 30:
                                #A new list of every move that has been done on the newest line is made.
                                tempTextList = []
                                for j in range(moveCount % 30 + 1):
                                    tempTextList.append(splitSolveMoves[i][j])
                                #Every move in this list is made red.
                                displayedMoves = (" ".join(tempTextList))
                                #The old text's position is used to write the text directly over the old text.
                                Text(displayedMoves,screen,i,(255,0,0),(solveText[i].pos))

                        #If the solve is not done showing, the next move can be shown.
                        moveCount = moveCount + 1

                #If the user presses the left arrow key, the last move in the solve is undone.
                elif event.type == KEYDOWN and event.key == K_LEFT:
                    #The last move can only be undone if it exists. If moveCount is 0, there are no moves to undo.
                    if moveCount != 0:
                        #The current move's function is called in reverse to change the cube's state.
                        moveCount = moveCount - 1
                        moveList[moveReversal(solveMoves[moveCount])]()

                        for text in solveText:
                            text.showText()

                        #Red text covers the solve moves to show which moves have already been done.
                        #Loops for how many lines of moves have already been done, plus one for the current line.
                        for i in range(moveCount // 30 + 1):
                            #For the number of lines of moves that are fully done, each line is written again in red.
                            for j in range(i):
                                displayedMoves = (" ".join(splitSolveMoves[j]))
                                Text(displayedMoves,screen,j,(255,0,0))
                            #Checks if this is the last loop.
                            if i == moveCount // 30:
                                #A new list of every move that has been done on the newest line is made.
                                tempTextList = []
                                for j in range(moveCount % 30):
                                    tempTextList.append(splitSolveMoves[i][j])
                                #Every move in this list is made red.
                                displayedMoves = (" ".join(tempTextList))
                                #The old text's position is used to write the text directly over the old text.
                                Text(displayedMoves,screen,i,(255,0,0),(solveText[i].pos))

                #If the user presses the up arrow key, the solve is shown automatically.
                elif event.type == KEYDOWN and event.key == K_UP:
                    auto = True
                    while auto == True:
                        #Every move has a slight delay to show each move separately.
                        time.sleep(0.1)
                        #Checks if every move has been shown.
                        if moveCount == len(solveMoves):
                            #Solve is no longer being displayed.
                            auto = False
                        else:
                            #Red text covers the solve moves to show which moves have already been done.
                            #Loops for how many lines of moves have already been done, plus one for the current line.
                            for i in range(moveCount // 30 + 1):
                                #For the number of lines of moves that are fully done, each line is written again in red.
                                for j in range(i):
                                    displayedMoves = (" ".join(splitSolveMoves[j]))
                                    Text(displayedMoves,screen,j,(255,0,0))
                                #Checks if this is the last loop.
                                if i == moveCount // 30:
                                    #A new list of every move that has been done on the newest line is made.
                                    tempTextList = []
                                    for j in range(moveCount % 30 + 1):
                                        tempTextList.append(splitSolveMoves[i][j])
                                    #Every move in this list is made red.
                                    displayedMoves = (" ".join(tempTextList))
                                    #The old text's position is used to write the text directly over the old text.
                                    Text(displayedMoves,screen,i,(255,0,0),(solveText[i].pos))

                            #The current move's function is called to change the cube's state.
                            moveList[solveMoves[moveCount]]()
                            #If the solve is not done showing, the next move can be shown.
                            moveCount = moveCount + 1
                        #The facelets are constantly updated to show how they look after any change to the cube happens.
                        for facelets in faceletList:
                            facelets.update(cubeState)
                        #The grid is drawn onto the cube to make the facelets more distinguishable.
                        pygame.draw.lines(screen,(0,0,0),False,[faceletLeft7.points[3],faceletRight7.points[3],faceletRight9.points[2],faceletRight6.points[2],faceletRight4.points[3],faceletLeft4.points[3],faceletLeft1.points[3],faceletLeft3.points[2],faceletRight3.points[2],faceletRight3.points[1],faceletRight1.points[0],faceletLeft1.points[0],faceletTop1.points[0],faceletTop3.points[1],faceletRight9.points[2],faceletRight9.points[3],faceletTop3.points[2],faceletTop1.points[3],faceletTop4.points[3],faceletTop6.points[2],faceletRight8.points[3],faceletRight7.points[3],faceletTop9.points[2],faceletTop8.points[2],faceletLeft8.points[2],faceletLeft8.points[3],faceletTop8.points[3],faceletTop7.points[3],faceletLeft7.points[3],faceletLeft7.points[2],faceletTop7.points[2],faceletTop2.points[0],faceletTop2.points[1],faceletTop8.points[2]],int(round(screen.get_height()/180)))        
                        #The display is updated at the end of every loop.
                        pygame.display.flip()

                        for event in pygame.event.get():
                            #If the user presses quit, the program ends.
                            if event.type == QUIT:
                                auto = False
                                going = False
                            #If the user presses escape, the program ends.
                            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                                auto = False
                                going = False

                            #Pressing the up arrow again pauses the solve.
                            elif event.type == KEYDOWN and event.key == K_UP:
                                auto = False

                #If the user presses the down arrow key, the solve is reversed automatically.
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    auto = True
                    while auto == True:
                        #Every move has a slight delay to show each move separately.
                        time.sleep(0.1)
                        #Checks if every move has been shown.
                        if moveCount == 0:
                            #Solve is no longer being displayed.
                            auto = False
                        else:
                            #Black text is reapplied over red text.
                            for text in solveText:
                                text.showText()

                            #If the solve is not done showing, the next move can be shown.
                            moveCount = moveCount - 1
                            moveList[moveReversal(solveMoves[moveCount])]()

                            #Red text covers the solve moves to show which moves have already been done.
                            #Loops for how many lines of moves have already been done, plus one for the current line.
                            for i in range(moveCount // 30 + 1):
                                #For the number of lines of moves that are fully done, each line is written again in red.
                                for j in range(i):
                                    displayedMoves = (" ".join(splitSolveMoves[j]))
                                    Text(displayedMoves,screen,j,(255,0,0))
                                #Checks if this is the last loop.
                                if i == moveCount // 30:
                                    #A new list of every move that has been done on the newest line is made.
                                    tempTextList = []
                                    for j in range(moveCount % 30):
                                        tempTextList.append(splitSolveMoves[i][j])
                                    #Every move in this list is made red.
                                    displayedMoves = (" ".join(tempTextList))
                                    #The old text's position is used to write the text directly over the old text.
                                    Text(displayedMoves,screen,i,(255,0,0),(solveText[i].pos))
                            
                        #The facelets are constantly updated to show how they look after any change to the cube happens.
                        for facelets in faceletList:
                            facelets.update(cubeState)
                        #The grid is drawn onto the cube to make the facelets more distinguishable.
                        pygame.draw.lines(screen,(0,0,0),False,[faceletLeft7.points[3],faceletRight7.points[3],faceletRight9.points[2],faceletRight6.points[2],faceletRight4.points[3],faceletLeft4.points[3],faceletLeft1.points[3],faceletLeft3.points[2],faceletRight3.points[2],faceletRight3.points[1],faceletRight1.points[0],faceletLeft1.points[0],faceletTop1.points[0],faceletTop3.points[1],faceletRight9.points[2],faceletRight9.points[3],faceletTop3.points[2],faceletTop1.points[3],faceletTop4.points[3],faceletTop6.points[2],faceletRight8.points[3],faceletRight7.points[3],faceletTop9.points[2],faceletTop8.points[2],faceletLeft8.points[2],faceletLeft8.points[3],faceletTop8.points[3],faceletTop7.points[3],faceletLeft7.points[3],faceletLeft7.points[2],faceletTop7.points[2],faceletTop2.points[0],faceletTop2.points[1],faceletTop8.points[2]],int(round(screen.get_height()/180)))        
                        #The display is updated at the end of every loop.
                        pygame.display.flip()

                        for event in pygame.event.get():
                            #If the user presses quit, the program ends.
                            if event.type == QUIT:
                                auto = False
                                going = False
                            #If the user presses escape, the program ends.
                            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                                auto = False
                                going = False

                            #Pressing the up arrow again pauses the solve.
                            elif event.type == KEYDOWN and event.key == K_DOWN:
                                auto = False

            #The facelets are constantly updated to show how they look after any change to the cube happens.
            for facelets in faceletList:
                facelets.update(cubeState)
            #The grid is drawn onto the cube to make the facelets more distinguishable.
            pygame.draw.lines(screen,(0,0,0),False,[faceletLeft7.points[3],faceletRight7.points[3],faceletRight9.points[2],faceletRight6.points[2],faceletRight4.points[3],faceletLeft4.points[3],faceletLeft1.points[3],faceletLeft3.points[2],faceletRight3.points[2],faceletRight3.points[1],faceletRight1.points[0],faceletLeft1.points[0],faceletTop1.points[0],faceletTop3.points[1],faceletRight9.points[2],faceletRight9.points[3],faceletTop3.points[2],faceletTop1.points[3],faceletTop4.points[3],faceletTop6.points[2],faceletRight8.points[3],faceletRight7.points[3],faceletTop9.points[2],faceletTop8.points[2],faceletLeft8.points[2],faceletLeft8.points[3],faceletTop8.points[3],faceletTop7.points[3],faceletLeft7.points[3],faceletLeft7.points[2],faceletTop7.points[2],faceletTop2.points[0],faceletTop2.points[1],faceletTop8.points[2]],int(round(screen.get_height()/180)))        
            #The display is updated at the end of every loop.
            pygame.display.flip()

        #If the solve is 0 moves long, nothing has to be displayed.
        elif solving == True:
            solving = False
            text = Text('The cube is already solved.', screen)

#If this is the main file being run, the main function is run.
if __name__ == '__main__':
    mainGUI()