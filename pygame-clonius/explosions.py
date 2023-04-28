import pygame

class Explosion(pygame.sprite.Sprite):

    def __init__(self, x, y, size):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.images = []
        self.imagenumber = 0
        for i in range(1,9):
            image = pygame.image.load(str(i) + '.png')
            image = pygame.transform.scale_by(image, size)
            self.images.append(image)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.imagenumber == 8:
            self.kill()
        else:
            self.image = self.images[self.imagenumber]
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            self.imagenumber += 1

        



