import pygame
from pygame.locals import *
import math

from player import *
from spritesheet import *


pygame.init()
gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Clonius")

exit = False
running = True 

clock = pygame.time.Clock()
dt = 0

ships_sheet = spritesheet('ships.png')
projs_sheet = spritesheet('projectiles.png')

player = Player(50,240,ships_sheet.image_at((32,64,16,16)))



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 300*dt
    if keys[pygame.K_s]:
        player.y += 300*dt
    if keys[pygame.K_SPACE]:
        player.fire()


    gamewindow.fill("black")
    
    gamewindow.blit(player.image, player.rect)

    pygame.display.flip()
    player.update()
    dt = clock.tick(60)/1000
