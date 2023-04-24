import pygame


# Defines auxiliary stuff
# Player class, enemy class, projectile class, sprite sheet class, etc.



# Spritesheet class, from the Pygame wiki
class spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    # Load a specific image from a specific rectangle

    def image_at(self, rectangle, colorkey=None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list

    def images_at(self, rects, colorkey=None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images

    def load_strip(self, rect, image_count, colorkey=None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale2x(pygame.transform.rotate(image,90))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.weapontype = "peashooter"
        self.firing = 0
        self.firingdelay = 100
    
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.firing == 1 and pygame.time.get_ticks() - self.firingtime > self.firingdelay:
            self.firing = 0

    def fire(self, projectileimage, group):
        if self.firing == 0:
            if self.weapontype == "peashooter":
                self.firing = 1
                self.firingtime = pygame.time.get_ticks()

                projectileimage = pygame.transform.rotate(projectileimage, 90)
                projectileimage = pygame.transform.scale2x(projectileimage)
                proj = PlayerProjectile(self.x+32, self.y+8, 10, 0, projectileimage)
                group.add(proj)



class PlayerProjectile(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy,image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.vx = vx
        self.vy = vy 

    def update(self):
        self.x += self.vx 
        self.y += self.vy
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x > 650:
            self.kill()
        if self.y > 500 or self.y < -10:
            self.kill()