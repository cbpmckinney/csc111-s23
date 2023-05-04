import pygame


class spritesheet(object):

    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()
        self.transColor = self.sheet.get_at((0, 0))

    def image_at(self, rectangle, colorkey=None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        image.set_colorkey(self.transColor)
        return image
