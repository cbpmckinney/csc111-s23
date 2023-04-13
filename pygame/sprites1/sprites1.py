import pygame
import sys
import random
from pygame.locals import *
from enemies import *
from player import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0

class Ball(pygame.sprite.Sprite):

    def __init__(self, imagefile, x, y, velx, vely):
        super().__init__()
        self.image = pygame.image.load(imagefile)
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.velx = velx
        self.vely = vely
    def update(self):
        if (self.rect.x >= 640 - 16) or (self.rect.x <= 0):
            self.velx = -self.velx
        if (self.rect.y >= 480 - 16) or (self.rect.y <= 0):
            self.vely = -self.vely
        
        self.x += self.velx
        self.y += self.vely
        self.rect.x = self.x
        self.rect.y = self.y


def CheckCollision(sprite1,sprite2):
    if pygame.sprite.collide_rect(sprite1, sprite2):
        sprite1.kill()
        sprite2.kill()



allsprites = pygame.sprite.Group()
listofballs = []
for i in range(5):
    listofballs.append(Ball("pie.png", random.randrange(1,600), random.randrange(1,400), random.randrange(1,2), random.randrange(1,2)))
    allsprites.add(listofballs[i])


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    allsprites.draw(screen)
    #flip() the display to put your work on screen
    pygame.display.flip()

    #collisionlist = pygame.sprite.groupcollide(allsprites, allsprites, False, False)
    #print(collisionlist)
    #for i in range(len(collisionlist)):
    #    for j in range(len(collisionlist[i])):
    #        CheckCollision(collisionlist[i],collisionlist[i][j])
        

    allsprites.update()




 

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


