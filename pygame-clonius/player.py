import pygame
from projectiles import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale2x(pygame.transform.rotate(image,90))
        self.rect = image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.firing = False
        self.firingdelay = 100

    def fire(self, image, group):
        if self.firing:
            pass
        else:
            self.firingtime = pygame.time.get_ticks()
            self.firing = True
            image = pygame.transform.scale2x(pygame.transform.rotate(image,-90))
            proj = PlayerProjectile(self.x+32, self.y+8, 10, 0, image)
            group.add(proj)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.firing and pygame.time.get_ticks() - self.firingtime > self.firingdelay:
            self.firing = False
