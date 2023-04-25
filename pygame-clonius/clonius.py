import pygame
from pygame.locals import *
import math

from player import *
from spritesheet import *
from enemies import *


pygame.init()
gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Clonius")

exit = False
running = True 

clock = pygame.time.Clock()
dt = 0

ships_sheet = spritesheet('ships.png')
projs_sheet = spritesheet('projectiles.png')

titlefont = pygame.font.Font('freesansbold.ttf',64)
hudfont = pygame.font.Font('freesansbold.ttf',24)


player = Player(50,240,ships_sheet.image_at((32,64,16,16)))
playerprojgroup = pygame.sprite.Group()
gamestate = 0

enemiesgroup = pygame.sprite.Group()
boss = Boss(400,240,ships_sheet.image_at((48,64,16,16)))
enemiesgroup.add(boss)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if gamestate == 0:
        if keys[pygame.K_SPACE]:
            gamestate = 1

        gamewindow.fill('black')

        titletext = titlefont.render("Clonius IV", True, "green")
        titletextrect = titletext.get_rect()
        titletextrect.center = (320,200)
        gamewindow.blit(titletext, titletextrect)

        pygame.display.flip()

    if gamestate == 1:
        playerscore = 0
        gamestate = 1.1
        
    if gamestate == 1.1:
        
        if keys[pygame.K_w]:
            player.y -= 300*dt
        if keys[pygame.K_s]:
            player.y += 300*dt
        if keys[pygame.K_SPACE]:
            player.fire(projs_sheet.image_at((0,8,8,8)), playerprojgroup)

        gamewindow.fill("black")
        
        
        

        gamewindow.blit(player.image, player.rect)
        playerprojgroup.draw(gamewindow)
        enemiesgroup.draw(gamewindow)

        scorestring = "Score: " + str(playerscore)
        scoretext = hudfont.render(scorestring, True, "red")
        scoretextrect = scoretext.get_rect()
        scoretextrect.topleft = (8,8)
        gamewindow.blit(scoretext, scoretextrect)

        pygame.display.flip()
        player.update()
        playerprojgroup.update()
        enemiesgroup.update()
        dt = clock.tick(60)/1000
