import os, sys
import pygame
from pygame.locals import *

def main():
    #Creates and displays a window
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Rubik's Cube Solver")

    #Draws a plain black background for the whole window size
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    #Draws the cube
    pygame.draw.polygon(screen,(255,255,0),[[screen.get_width()//2,screen.get_height()//2],[screen.get_width()//2-175,screen.get_height()//2-75],[screen.get_width()//2,screen.get_height()//2-150],[screen.get_width()//2+175,screen.get_height()//2-75]])
    pygame.draw.polygon(screen,(0,255,0),[[screen.get_width()//2,screen.get_height()//2],[screen.get_width()//2,screen.get_height()//2+225],[screen.get_width()//2-175,screen.get_height()//2+150],[screen.get_width()//2-175,screen.get_height()//2-75]])
    pygame.draw.polygon(screen,(255,128,0),[[screen.get_width()//2,screen.get_height()//2],[screen.get_width()//2,screen.get_height()//2+225],[screen.get_width()//2+175,screen.get_height()//2+150],[screen.get_width()//2+175,screen.get_height()//2-75]])
    pygame.display.flip()

    going = True
    while going == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False


if __name__ == '__main__':
    main()