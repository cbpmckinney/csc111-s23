import pygame
import sys, random
from pygame.locals import *

pygame.init()
gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Test game!")
exit = False
running = True

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()


