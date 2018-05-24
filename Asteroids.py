import pygame, random

WIN_W = 16*32

WHITE = (255,255,255)
GRAY = (80,80,80)
GREEN = (75, 150,75)
BLACK = (0,0,0)
RED = (232,5,5)
SILVER = (205, 203, 195)

class Meteor(pygame.sprite.Sprite):
    def __init__(self,ship):
        pygame.sprite.Sprite.__init__(self)
        self.destiny = random.randrange(2)
        self.x = random.randrange(WIN_W)
        if self.destiny == 0:
            self.x = -self.x
        else:
            self.x = self.x
        self.speed = 10
        self.image = pygame.image.load("Image/meteor.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (15,20))
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx +self.x

    def update(self, ship):

        self.rect.y += self.speed
        self.collide(ship)

        if self.rect.y <= 0:
            self.kill()

    def collide(self,ship):
        if pygame.sprite.collide_rect(self,ship):
            if self.rect.bottom >= ship.rect.top:
                ship.life -= 2
                self.kill()
