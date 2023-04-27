import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.health = 1
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 
    
        
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.health <= 0:
            self.kill()


class Fighter(Enemy):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)


class Bomber(Enemy):
    def __init__(self, x, y , image):
        super().__init__(x,y, image)
        self.health = 2

class Boss(Enemy):
    def __init__(self,x,y,image):
        super().__init__(x,y,pygame.transform.scale_by(image,4))
        self.health = 100