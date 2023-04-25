import pygame

class PlayerProjectile(pygame.sprite.Sprite):

    def __init__(self,x,y,vx,vy,image):
        super().__init__()
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x > 650:
            self.kill()
        if self.y > 500 or self.y < -10:
            self.kill()
            