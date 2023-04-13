# Define the Player object by extending pygame.sprite.Sprite
# Instead of a surface, use an image for a better-looking sprite

import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self, imagefile, posx, posy):
        super(Player, self).__init__()
        self.surf = pygame.image.load(imagefile)
        self.rect = self.rect
