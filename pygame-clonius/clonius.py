import pygame
from pygame.locals import *
import math

from player import *
from spritesheet import *
from enemies import *
from hud import *


pygame.init()
pygame.mixer.init()
gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Clonius")
hud = Hud(gamewindow, (640,480))

exit = False
running = True 

clock = pygame.time.Clock()
dt = 0

ships_sheet = spritesheet('ships.png')
projs_sheet = spritesheet('projectiles.png')

player = Player(50,240,ships_sheet.image_at((32,64,16,16)))
playerprojgroup = pygame.sprite.Group()
gamestate = 0

enemiesgroup = pygame.sprite.Group()


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if gamestate == 0:
        if keys[pygame.K_SPACE]:
            gamestate = 1

        gamewindow.fill('black')

        hud.main_menu("Clonius IV", "green")

        pygame.display.flip()

    if gamestate == 1:
        playerscore = 0
        gamestate = 1.1
        boss = Boss(400,240,ships_sheet.image_at((48,64,16,16)))
        enemiesgroup.add(boss)

    if gamestate == 1.1:
        
        if keys[pygame.K_w]:
            player.y -= 300*dt
        if keys[pygame.K_s]:
            player.y += 300*dt
        if keys[pygame.K_SPACE]:
            player.fire(projs_sheet.image_at((0,8,8,8)), playerprojgroup)

        gamewindow.fill("black")
        
        for object in pygame.sprite.spritecollide(boss, playerprojgroup, False):
            object.kill()
            boss.health -= 1
        
    

        gamewindow.blit(player.image, player.rect)
        playerprojgroup.draw(gamewindow)
        enemiesgroup.draw(gamewindow)
        hud.score = playerscore
        hud.game_info()

        pygame.display.flip()
        player.update()
        playerprojgroup.update()
        enemiesgroup.update()
        dt = clock.tick(60)/1000
