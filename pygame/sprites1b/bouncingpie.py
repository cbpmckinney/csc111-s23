import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True
dt = 0

class Ball(pygame.sprite.Sprite):

    def __init__(self, imagefile, x, y, velx, vely, ax, ay):
        super().__init__()
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        self.ax = ax
        self.ay = ay
        self.image = pygame.image.load(imagefile)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        if (self.x >= 640 - 16) or (self.x <= 0):
            self.velx = -self.velx

        if (self.y >= 480 - 16) or (self.y <= 0):
            self.vely = -self.vely
            
        
        self.velx += self.ax
        self.vely += self.ay
        self.x += self.velx
        self.y += self.vely
        self.rect.x = self.x
        self.rect.y = self.y


class MouseCursor(pygame.sprite.Sprite):

    def __init__(self, imagefile, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(imagefile)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.rect.x = self.x
        self.rect.y = self.y



allsprites = pygame.sprite.Group()
#for i in range(10):
#    allsprites.add(Ball("pie.png", random.randrange(16,640-16), random.randrange(16,480-16), 1, 1, 0, 0))
allsprites.add(MouseCursor("pie.png",100,100))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print(pygame.mouse.get_pos())
    screen.fill("white")
    allsprites.draw(screen)
    pygame.display.flip()

    allsprites.update()
    clock.tick(60)
pygame.quit()