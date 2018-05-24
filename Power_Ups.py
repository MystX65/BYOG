import pygame, random
GREEN = (74,224,74)
ORANGE = (255,156,0)
PB_WIDTH = 10
P_HEIGHT = 20
WIN_H = 700

class Upgrade(pygame.sprite.Sprite):
    def __init__(self, appear, ship):
        pygame.sprite.Sprite.__init__(self)
        self.appear = appear
        self.appearance = False
        self.x = random.randrange(-2,3)
        self.y = random.randrange(-2,2)
        if self.appear == 4:
            self.image = pygame.image.load("Image/rocket.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (20,20))
            self.rect = self.image.get_rect()
            self.rect.x = ship.rect.centerx
            self.rect.y = WIN_H/2
            self.appearance = True
            self.activated = False

    def update(self, ship, platform_group):
        self.rect.x += self.x
        self.rect.y += self.y
        self.collide(ship, platform_group, "")

    def collide(self, ship, platform_group, dir):
        if self.x<0:
            n = 1
        elif self.x > 0:
            n = -1
        else:
            n = 0
        if self.y < 0:
            s = 1
        elif  self.y > 0:
            s = -1
        else:
            s = 0
        self.activated = False
        if pygame.sprite.collide_rect(self,ship):
            if dir == "" and self.rect.bottom >= ship.rect.top:
                ship.shooting_type += 1
                self.kill()
            elif dir == "" and self.rect.left <= ship.rect.right:
                ship.shooting_type += 1
                self.kill()
            elif dir == "" and self.rect.right >= ship.rect.left:
                ship.shooting_type += 1
                self.kill()
            elif dir == "" and self.rect.top <= ship.bottom:
                ship.shooting_type += 1
                self.kill()
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if self.activated == False:
                    if n == 1:
                        if self.rect.left <= p.rect.right:
                            self.x *= -1
                    elif s == 1:
                        if self.rect.top <= p.rect.bottom:
                            self.y *= -1
                    elif n == -1:
                        if self.rect.right >= p.rect.left:
                            self.x *= -1
                    elif s == -1:
                        if self.rect.bottom >= p.rect.top:
                            self.y *= -1
                    self.activated = True

class Heal(Upgrade):
    def __init__(self, appear, ship):
        Upgrade.__init__(self, appear, ship)
        self.image = pygame.image.load("Image/life.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))

    def update(self, ship, platform_group):
        Upgrade.update(self, ship, platform_group)


    def collide(self, ship, platform_group, dir):
        if self.x<0:
            n = 1
        elif self.x > 0:
            n = -1
        else:
            n = 0
        if self.y < 0:
            s = 1
        elif  self.y > 0:
            s = -1
        else:
            s = 0
        self.activated = False
        if pygame.sprite.collide_rect(self,ship):
            if dir == "" and self.rect.bottom >= ship.rect.top:
                ship.life += 1
                self.kill()
            elif dir == "" and self.rect.left <= ship.rect.right:
                ship.life += 1
                self.kill()
            elif dir == "" and self.rect.right >= ship.rect.left:
                ship.life += 1
                self.kill()
            elif dir == "" and self.rect.top <= ship.bottom:
                ship.life += 1
                self.kill()
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if self.activated == False:
                    if n == 1:
                        if self.rect.left <= p.rect.right:
                            self.x *= -1
                    elif s == 1:
                        if self.rect.top <= p.rect.bottom:
                            self.y *= -1
                    elif n == -1:
                        if self.rect.right >= p.rect.left:
                            self.x *= -1
                    elif s == -1:
                        if self.rect.bottom >= p.rect.top:
                            self.y *= -1
                    self.activated = True


