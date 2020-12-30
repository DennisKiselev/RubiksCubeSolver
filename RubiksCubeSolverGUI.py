import os, sys
import pygame
from pygame.locals import *

class facelet():
    def __init__(self,surface,colour,points):
        self.points = points
        self.colour = colour
        pygame.draw.polygon(surface,colour,points)

def main():
    greenFace = [["green","green","green"],["green","green","green"],["green","green","green"]]
    blueFace = [["blue","blue","blue"],["blue","blue","blue"],["blue","blue","blue"]]
    redFace = [["red","red","red"],["red","red","red"],["red","red","red"]]
    orangeFace = [["orange","orange","orange"],["orange","orange","orange"],["orange","orange","orange"]]
    whiteFace = [["white","white","white"],["white","white","white"],["white","white","white"]]
    yellowFace = [["yellow","yellow","yellow"],["yellow","yellow","yellow"],["yellow","yellow","yellow"]]

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
    faceletTop1 = facelet(screen,colour_dict[yellowFace[0][0]],[[screen.get_width()//2,screen.get_height()//2],[screen.get_width()//2*93/128,screen.get_height()//2*19/24],[screen.get_width()//2,screen.get_height()//2*7/12],[screen.get_width()//2*163/128,screen.get_height()//2*19/24]])
    faceletLeft1 = facelet(screen,colour_dict[greenFace[0][0]],[[screen.get_width()//2,screen.get_height()//2],[screen.get_width()//2,screen.get_height()//2*13/8],[screen.get_width()//2*93/128,screen.get_height()//2*17/12],[screen.get_width()//2*93/128,screen.get_height()//2*19/24]])
    faceletRight1 = facelet(screen,colour_dict[orangeFace[0][0]],[[screen.get_width()//2,screen.get_height()//2],[screen.get_width()//2,screen.get_height()//2*13/8],[screen.get_width()//2*163/128,screen.get_height()//2*17/12],[screen.get_width()//2*163/128,screen.get_height()//2*19/24]])
    pygame.display.flip()

    going = True
    while going == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False


if __name__ == '__main__':
    main()