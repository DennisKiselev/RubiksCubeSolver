import os, pygame, time
from pygame.locals import *
from RubiksCubeSolver import *


#Class to represent facelets on the cube.
class Facelet():
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
    

def mainGUI():
    #Dictionary containing all the possible colours and their corresponding RGB values.
    colour_dict = {"green":(0,255,0),"blue":(0,0,255),"red":(255,0,0),"orange":(255,128,0),"white":(255,255,255),"yellow":(255,255,0)}

    #Creates and displays a window
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Rubik's Cube Solver")

    #Draws a plain black background for the whole window size.
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((128,128,128))
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

    #Draws grids around facelets to make them more distinguishable.
    pygame.draw.lines(screen,(0,0,0),False,[faceletLeft7.points[3],faceletRight7.points[3],faceletRight9.points[2],faceletRight6.points[2],faceletRight4.points[3],faceletLeft4.points[3],faceletLeft1.points[3],faceletLeft3.points[2],faceletRight3.points[2],faceletRight3.points[1],faceletRight1.points[0],faceletLeft1.points[0],faceletTop1.points[0],faceletTop3.points[1],faceletRight9.points[2],faceletRight9.points[3],faceletTop3.points[2],faceletTop1.points[3],faceletTop4.points[3],faceletTop6.points[2],faceletRight8.points[3],faceletRight7.points[3],faceletTop9.points[2],faceletTop8.points[2],faceletLeft8.points[2],faceletLeft8.points[3],faceletTop8.points[3],faceletTop7.points[3],faceletLeft7.points[3],faceletLeft7.points[2],faceletTop7.points[2],faceletTop2.points[0],faceletTop2.points[1],faceletTop8.points[2]],4)

    #Updates the display.
    pygame.display.flip()

    #Resets cubeState.
    cubeState = cubeReset()

    going = True
    while going == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False
            elif event.type == KEYDOWN and event.key == K_SPACE:
                scrambleMoves = scrambleGen()
                cubeState = moveInput(scrambleMoves)
                screen.blit(background,(0,0))
                for facelets in faceletList:
                    facelets.update(cubeState)
            elif event.type == MOUSEBUTTONUP:
                for facelets in faceletList:
                    cubeState = facelets.clickCheck(cubeState)
            elif event.type == KEYDOWN and event.key == K_s:
                moveList = {'U':U,'D':D,'F':F,'B':B,'R':R,'L':L,'U2':U2,'D2':D2,'F2':F2,'B2':B2,'R2':R2,'L2':L2,"U'":UP,"D'":DP,"F'":FP,"B'":BP,"R'":RP,"L'":LP}
                solveMoves = solve()
                cubeState = moveInput(moveReversal(solveMoves))
                for move in solveMoves:
                    moveList[move]()
                    for facelets in faceletList:
                        facelets.update(cubeState)
                    pygame.draw.lines(screen,(0,0,0),False,[faceletLeft7.points[3],faceletRight7.points[3],faceletRight9.points[2],faceletRight6.points[2],faceletRight4.points[3],faceletLeft4.points[3],faceletLeft1.points[3],faceletLeft3.points[2],faceletRight3.points[2],faceletRight3.points[1],faceletRight1.points[0],faceletLeft1.points[0],faceletTop1.points[0],faceletTop3.points[1],faceletRight9.points[2],faceletRight9.points[3],faceletTop3.points[2],faceletTop1.points[3],faceletTop4.points[3],faceletTop6.points[2],faceletRight8.points[3],faceletRight7.points[3],faceletTop9.points[2],faceletTop8.points[2],faceletLeft8.points[2],faceletLeft8.points[3],faceletTop8.points[3],faceletTop7.points[3],faceletLeft7.points[3],faceletLeft7.points[2],faceletTop7.points[2],faceletTop2.points[0],faceletTop2.points[1],faceletTop8.points[2]],4)        
                    pygame.display.flip()
                    time.sleep(0.1)
            elif event.type == KEYDOWN and event.key == K_x:
                x()
                for facelets in faceletList:
                    facelets.update(cubeState)
            elif event.type == KEYDOWN and event.key == K_y:
                y()
                for facelets in faceletList:
                    facelets.update(cubeState)
            elif event.type == KEYDOWN and event.key == K_z:
                z()
                for facelets in faceletList:
                    facelets.update(cubeState)
            pygame.draw.lines(screen,(0,0,0),False,[faceletLeft7.points[3],faceletRight7.points[3],faceletRight9.points[2],faceletRight6.points[2],faceletRight4.points[3],faceletLeft4.points[3],faceletLeft1.points[3],faceletLeft3.points[2],faceletRight3.points[2],faceletRight3.points[1],faceletRight1.points[0],faceletLeft1.points[0],faceletTop1.points[0],faceletTop3.points[1],faceletRight9.points[2],faceletRight9.points[3],faceletTop3.points[2],faceletTop1.points[3],faceletTop4.points[3],faceletTop6.points[2],faceletRight8.points[3],faceletRight7.points[3],faceletTop9.points[2],faceletTop8.points[2],faceletLeft8.points[2],faceletLeft8.points[3],faceletTop8.points[3],faceletTop7.points[3],faceletLeft7.points[3],faceletLeft7.points[2],faceletTop7.points[2],faceletTop2.points[0],faceletTop2.points[1],faceletTop8.points[2]],4)
            pygame.display.flip()


if __name__ == '__main__':
    mainGUI()