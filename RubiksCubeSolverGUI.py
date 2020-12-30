import os, sys
import pygame
from pygame.locals import *


class facelet():
    def __init__(self,surface,colour,points):
        self.surface = surface
        self.points = points
        self.colour = colour
        for coords in self.points:
            coords[0] = int(round(coords[0]))
            coords[1] = int(round(coords[1]))
        pygame.draw.polygon(self.surface,self.colour,self.points)


def main():
    greenFace = [['blue', 'green', 'green'], ['green', 'green', 'orange'], ['green', 'white', 'green']]
    blueFace = [['blue', 'red', 'red'], ['green', 'blue', 'blue'], ['green', 'yellow', 'red']]
    redFace = [['yellow', 'green', 'white'], ['white', 'red', 'white'], ['white', 'yellow', 'red']]
    orangeFace = [['white', 'blue', 'orange'], ['yellow', 'orange', 'red'], ['red', 'red', 'orange']]
    whiteFace = [['white', 'orange', 'yellow'], ['blue', 'white', 'blue'], ['blue', 'red', 'yellow']]
    yellowFace = [['blue', 'white', 'yellow'], ['orange', 'yellow', 'orange'], ['orange', 'yellow', 'orange']]

    #Dictionary containing all the possible colours and their corresponding RGB values.
    colour_dict = {"green":[0,255,0],"blue":[0,0,255],"red":[255,0,0],"orange":[255,128,0],"white":[255,255,255],"yellow":[255,255,0]}

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
    faceletTop1 = facelet(screen,colour_dict[yellowFace[0][0]],[[screen.get_width()/2,screen.get_height()/2*7/12],[screen.get_width()/2*419/384,screen.get_height()/2*47/72],[screen.get_width()/2,screen.get_height()/2*13/18],[screen.get_width()/2*349/384,screen.get_height()/2*47/72]])
    faceletTop2 = facelet(screen,colour_dict[yellowFace[0][1]],[faceletTop1.points[1],[screen.get_width()/2*227/192,faceletTop1.points[2][1]],[faceletTop1.points[1][0],screen.get_height()/2*19/24],faceletTop1.points[2]])
    faceletTop3 = facelet(screen,colour_dict[yellowFace[0][2]],[faceletTop2.points[1],[screen.get_width()/2*163/128,faceletTop2.points[2][1]],[faceletTop2.points[1][0],screen.get_height()/2*31/36],faceletTop2.points[2]])
    faceletTop4 = facelet(screen,colour_dict[yellowFace[1][0]],[faceletTop1.points[3],faceletTop1.points[2],[faceletTop1.points[3][0],faceletTop2.points[2][1]],[screen.get_width()/2*157/192,faceletTop1.points[2][1]]])
    faceletTop5 = facelet(screen,colour_dict[yellowFace[1][1]],[faceletTop1.points[2],faceletTop2.points[2],[screen.get_width()/2,faceletTop3.points[2][1]],faceletTop4.points[2]])
    faceletTop6 = facelet(screen,colour_dict[yellowFace[1][2]],[faceletTop2.points[2],faceletTop3.points[2],[faceletTop2.points[0][0],screen.get_height()/2*67/72],faceletTop5.points[2]])
    faceletTop7 = facelet(screen,colour_dict[yellowFace[2][0]],[faceletTop4.points[3],faceletTop4.points[2],[faceletTop4.points[3][0],faceletTop3.points[2][1]],[screen.get_width()/2*93/128,faceletTop3.points[1][1]]])
    faceletTop8 = facelet(screen,colour_dict[yellowFace[2][1]],[faceletTop4.points[2],faceletTop5.points[2],[faceletTop4.points[0][0],faceletTop6.points[2][1]],faceletTop7.points[2]])
    faceletTop9 = facelet(screen,colour_dict[yellowFace[2][2]],[faceletTop5.points[2],faceletTop6.points[2],[screen.get_width()/2,screen.get_height()/2],faceletTop8.points[2]])

    #faceletLeft objects work exactly the same as faceletTop, but instead represent the green face.
    faceletLeft1 = facelet(screen,colour_dict[greenFace[0][0]],[faceletTop7.points[3],faceletTop7.points[2],[faceletTop7.points[0][0],screen.get_height()/2*77/72],[screen.get_width()/2*93/128,screen.get_height()/2]])
    faceletLeft2 = facelet(screen,colour_dict[greenFace[0][1]],[faceletTop8.points[3],faceletTop8.points[2],[faceletTop8.points[0][0],screen.get_height()/2*41/36],faceletLeft1.points[2]])
    faceletLeft3 = facelet(screen,colour_dict[greenFace[0][2]],[faceletTop9.points[3],faceletTop9.points[2],[faceletTop9.points[0][0],screen.get_height()/2*29/24],faceletLeft2.points[2]])
    faceletLeft4 = facelet(screen,colour_dict[greenFace[1][0]],[faceletLeft1.points[3],faceletLeft1.points[2],[faceletLeft1.points[1][0],screen.get_height()/2*23/18],[faceletLeft1.points[0][0],faceletLeft3.points[2][1]]])
    faceletLeft5 = facelet(screen,colour_dict[greenFace[1][1]],[faceletLeft2.points[3],faceletLeft2.points[2],[faceletLeft2.points[1][0],screen.get_height()/2*97/72],faceletLeft4.points[2]])
    faceletLeft6 = facelet(screen,colour_dict[greenFace[1][2]],[faceletLeft3.points[3],faceletLeft3.points[2],[faceletLeft3.points[1][0],screen.get_height()/2*17/12],faceletLeft5.points[2]])
    faceletLeft7 = facelet(screen,colour_dict[greenFace[2][0]],[faceletLeft4.points[3],faceletLeft4.points[2],[faceletLeft4.points[1][0],screen.get_height()/2*107/72],[faceletLeft1.points[0][0],faceletLeft6.points[2][1]]])
    faceletLeft8 = facelet(screen,colour_dict[greenFace[2][1]],[faceletLeft5.points[3],faceletLeft5.points[2],[faceletLeft5.points[1][0],screen.get_height()/2*14/9],faceletLeft7.points[2]])
    faceletLeft9 = facelet(screen,colour_dict[greenFace[2][2]],[faceletLeft6.points[3],faceletLeft6.points[2],[faceletLeft6.points[1][0],screen.get_height()/2*13/8],faceletLeft8.points[2]])
    
    #faceletRight objects work exactly the same as faceletTop and faceletRight, but instead represent the orange face.
    #faceletRight1 = facelet(screen,colour_dict[orangeFace[0][0]],[[screen.get_width()/2,screen.get_height()/2],[screen.get_width()/2,screen.get_height()/2*13/8],[screen.get_width()/2*163/128,screen.get_height()/2*17/12],[screen.get_width()/2*163/128,screen.get_height()/2*19/24]])
    faceletRight1 = facelet(screen,colour_dict[orangeFace[0][0]],[faceletTop9.points[2],faceletTop9.points[1],[faceletTop1.points[1][0],faceletLeft3.points[3][1]],faceletLeft3.points[2]])
    faceletRight2 = facelet(screen,colour_dict[orangeFace[0][1]],[faceletTop9.points[1],faceletTop6.points[1],[faceletTop2.points[1][0],faceletLeft2.points[3][1]],faceletRight1.points[2]])
    faceletRight3 = facelet(screen,colour_dict[orangeFace[0][2]],[faceletTop6.points[1],faceletTop3.points[1],[faceletTop3.points[1][0],faceletLeft1.points[3][1]],faceletRight2.points[2]])
    faceletRight4 = facelet(screen,colour_dict[orangeFace[1][0]],[faceletRight1.points[3],faceletRight1.points[2],[faceletTop1.points[1][0],faceletLeft6.points[3][1]],faceletLeft6.points[2]])
    faceletRight5 = facelet(screen,colour_dict[orangeFace[1][1]],[faceletRight2.points[3],faceletRight2.points[2],[faceletTop2.points[1][0],faceletLeft5.points[3][1]],faceletRight4.points[2]])
    faceletRight6 = facelet(screen,colour_dict[orangeFace[1][2]],[faceletRight3.points[3],faceletRight3.points[2],[faceletTop3.points[1][0],faceletLeft4.points[3][1]],faceletRight5.points[2]])
    faceletRight7 = facelet(screen,colour_dict[orangeFace[2][0]],[faceletRight4.points[3],faceletRight4.points[2],[faceletTop1.points[1][0],faceletLeft9.points[3][1]],faceletLeft9.points[2]])
    faceletRight8 = facelet(screen,colour_dict[orangeFace[2][1]],[faceletRight5.points[3],faceletRight5.points[2],[faceletTop2.points[1][0],faceletLeft8.points[3][1]],faceletRight7.points[2]])
    faceletRight9 = facelet(screen,colour_dict[orangeFace[2][2]],[faceletRight6.points[3],faceletRight6.points[2],[faceletTop3.points[1][0],faceletLeft7.points[3][1]],faceletRight8.points[2]])
    #Updates the display.
    pygame.display.flip()

    going = True
    while going == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False


if __name__ == '__main__':
    main()


#faceletRight1 = facelet(screen,colour_dict[orangeFace[0][0]],[[faceletTop9.points[2][0]+1,faceletTop9.points[2][1]],faceletTop6.points[2],[faceletTop1.points[1][0],faceletLeft2.points[2][1]],[faceletLeft3.points[2][0]+1,faceletLeft3.points[2][1]]])