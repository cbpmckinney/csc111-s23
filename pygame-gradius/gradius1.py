import pygame
import sys
import random
from pygame.locals import *
from aux import *
import math 

pygame.init()
gamewindow = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Gradius Clone")

exit = False
running = True

titlefont = pygame.font.Font('freesansbold.ttf', 64)
menufont = pygame.font.Font('freesansbold.ttf', 32)
hudfont = pygame.font.Font('freesansbold.ttf', 24)

ships_sheet = spritesheet('ships.png')
projs_sheet = spritesheet('projectiles.png')

player = Player(50,240,ships_sheet.image_at((32,64,16,16)))
playerprojgroup = pygame.sprite.Group()

gamestate = 0

clock = pygame.time.Clock()
dt = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if gamestate == 0:
        #Display game menu
        
        if keys[pygame.K_SPACE]:
            gamestate = 1

        gamewindow.fill("black")
        
        titletext = titlefont.render("Clonius IV", True, "green")
        titletextRect = titletext.get_rect()
        titletextRect.center = (320,240)
        gamewindow.blit(titletext, titletextRect)

        subtitletext = menufont.render("A Gradius Clone by CSC-111", True, "blue")
        subtitletextRect = subtitletext.get_rect()
        subtitletextRect.center = (320,304)
        gamewindow.blit(subtitletext, subtitletextRect)

        starttext = menufont.render("Press Space to Start", True, "red")
        starttextRect = starttext.get_rect()
        starttextRect.center = (320, 368)
        gamewindow.blit(starttext, starttextRect)

        pygame.display.flip() 

    if (gamestate == 1) or (gamestate == 1.1):
        gamewindow.fill("black")
        if gamestate == 1:
            playerscore = 0
            gamestarttime = pygame.time.get_ticks()
            gamestate = 1.1
        scorestring = "Score: " + str(playerscore)
        scoretext = hudfont.render(scorestring, True, "red")
        scoretextRect = scoretext.get_rect()
        scoretextRect.topleft = (8, 8)
        gamewindow.blit(scoretext, scoretextRect)
            

        #Actually play game

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if (player.y > 1):
                player.y -= 300 * dt
        if keys[pygame.K_s]:
            if player.y < 480 - 33:
                player.y += 300 * dt
        if keys[pygame.K_SPACE]:
            player.fire(projs_sheet.image_at((0,8,8,8)), playerprojgroup)

   
        gamewindow.blit(player.image, player.rect)
        playerprojgroup.draw(gamewindow)
        pygame.display.flip()

        player.update()
        playerprojgroup.update()
        dt = clock.tick(60) / 1000

