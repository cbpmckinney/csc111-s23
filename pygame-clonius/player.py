import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale2x(pygame.transform.rotate(image,90))
        self.rect = image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def fire(self):
        

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
