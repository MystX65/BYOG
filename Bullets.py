import pygame
WHITE = (255,255,255)
GRAY = (80,80,80)
GREEN = (75, 150,75)
BLACK = (0,0,0)
RED = (232,5,5)
SILVER = (205, 203, 195)
class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self,ship,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("Image/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (8, 8))
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx

    def set_pos_enemy(self, enemy, w):
        self.rect.x = enemy.rect.x + w
        self.rect.y = enemy.rect.y + 30
        self.start_y = enemy.rect.y + 30

    def update(self, platform_group, ship):
        self.rect.y += self.y
        self.rect.x += self.x
        self.collide(platform_group, ship)

        if self.rect.y <= 0:
            self.kill()

    def collide(self, platform_group, ship):
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if self.rect.bottom > p.rect.top:
                    self.rect.bottom = p.rect.top
                    self.kill()
                if self.rect.right >  p.rect.left:
                    self.rect.right = p.rect.left
                    self.kill()
                if self.rect.left < p.rect.right:
                    self.rect.left = p.rect.right
                    self.kill()
        if pygame.sprite.collide_rect(self,ship):
            if self.rect.bottom >= ship.rect.top:
                ship.life -= 1
                self.kill()

class Enemy_Target_Missles(pygame.sprite.Sprite):
    def __init__(self, ship,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.y = y
        self.x = x
        self.image = pygame.image.load("Image/sniper_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (8, 8))
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx

    def set_pos_enemy(self, enemy, w):
        self.rect.x = enemy.rect.x + w
        self.rect.y = enemy.rect.y + 30
        self.start_y = enemy.rect.y + 30

    def update(self, platform_group, ship):
        if self.rect.x > ship.rect.x:
            self.rect.x -= self.x
        elif self.rect.x < ship.rect.x:
            self.rect.x += self.x
        else:
            self.rect.x += 0
        self.rect.y += self.y
        self.collide(platform_group, ship)

        if self.rect.y <=0:
            self.kill()

    def collide(self, platform_group, ship):
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if self.rect.bottom > p.rect.top:
                    self.rect.bottom = p.rect.top
                    self.kill()
                if self.rect.right >  p.rect.left:
                    self.rect.right = p.rect.left
                    self.kill()
                if self.rect.left < p.rect.right:
                    self.rect.left = p.rect.right
                    self.kill()
        if pygame.sprite.collide_rect(self,ship):
            if self.rect.bottom >= ship.rect.top:
                ship.life -= 1
                self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,ship, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 10
        self.image = pygame.image.load("Image/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (8,8))
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx

    def set_pos(self,ship, w):
        self.rect.x = ship.rect.x + w
        self.rect.y = ship.rect.y

    def update(self, platform_group, enemy_group):
        self.rect.y -= self.y
        self.rect.x -= self.x
        self.collide(platform_group, "up", enemy_group)

        if self.rect.y <= 0:
            self.kill()

    def collide(self, platform_group, dir, enemy_group):
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if dir == "up" and self.rect.top < p.rect.bottom:
                    self.rect.top = p.rect.bottom
                    self.kill()
        for e in enemy_group:
            if pygame.sprite.collide_rect(self, e):
                if dir == "up" and self.rect.top<e.rect.bottom:
                    self.rect.top = e.rect.bottom
                    e.life -= 1
                    self.kill()
