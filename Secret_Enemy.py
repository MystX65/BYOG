from Power_Ups import *
import pygame
RED = (232,5,5)

WIN_W = 16*32
WIN_H = 700
class Secret_Enemy(pygame.sprite.Sprite):
    def __init__(self, container, ypos, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.container = container
        self.side_speed = 1
        self.top_speed = 3
        self.image = pygame.image.load("Image/secret_ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,30))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.container.centerx + xpos
        self.rect.y = ypos
        self.life = random.randrange(20, 31)
        self.isAlive = True

    def update(self, bullet_group, ship, enemy_group, platform_group, heal_group, camera):
        self.collide(bullet_group, enemy_group, platform_group, "")
        self.collide(bullet_group, enemy_group, platform_group, "up")
        self.collide(bullet_group, enemy_group, platform_group, "down")
        self.collide(bullet_group, enemy_group, platform_group, "right")
        self.collide(bullet_group, enemy_group, platform_group, "left")
        if self.life <= 0:
            self.isAlive = False
            heal = Heal(int(random.choice('4')), ship)
            if heal.appearance == True:
                heal_group.add(heal)
            self.kill()
        self.rect.clamp_ip(self.container)

    def collide(self, bullet_group, enemy_group, platform_group, dir):
        n = 1
        for b in bullet_group:
            if pygame.sprite.collide_rect(self, b):
                if self.rect.bottom <= b.rect.top:
                    self.life -= 1
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if dir == "left" and self.rect.left > p.rect.right:
                    if dir == "right" and self.rect.right < p.rect.left:
                        if dir == "up" and self.rect.top < p.rect.bottom -10:
                            self.rect.top = self.rect.top
                            print ("Hit Top")
                if dir == "left" and self.rect.left > p.rect.right:
                    if dir == "right" and self.rect.right < p.rect.left:
                        if dir == "down" and self.rect.bottom > p.rect.top + 10:
                            self.rect.bottom = self.rect.bottom
                            print("Hit Bottom")
                if n == 1:
                    if dir == "left" and self.rect.left <= p.rect.right:
                        self.side_speed = -self.side_speed
                        n = -n
                if n == -1:
                    if dir == "right" and self.rect.right >= p.rect.left:
                        self.side_speed = -self.side_speed
                        n = -n
                if self.rect.top < 30:
                    self.rect.top = 30

class Secret_Moving_Enemy(Secret_Enemy):
    def __init__(self, container, ypos, xpos):
        Secret_Enemy.__init__(self, container, ypos, xpos)
        self.image = pygame.image.load("Image/secret_ship2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 30))
        self.move = False

    def update(self, bullet_group, ship, enemy_group, platform_group, heal_group, camera):
        Secret_Enemy.update(self, bullet_group, ship, enemy_group, platform_group, heal_group, camera)
        if camera.apply(ship).y <= camera.apply(self).y +300:
            self.move = True
        if self.move:
            if camera.apply(self).y < camera.apply(ship).y - 300:
                self.rect.y += self.top_speed
        if self.move:
            if camera.apply(self).y > camera.apply(ship).y - 300:
                self.rect.y -= self.top_speed
        else:
            self.rect.y = self.rect.y

        self.rect.x += self.side_speed

class Secret_Sniper(Secret_Enemy):
    def __init__(self, container, ypos, xpos):
        Secret_Enemy.__init__(self,container, ypos, xpos)
        self.image = pygame.image.load("Image/secret_ship3.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,30))

    def update(self, bullet_group, ship, enemy_group, platform_group, heal_group, camera):
        Secret_Enemy.update(self, bullet_group, ship, enemy_group, platform_group, heal_group, camera)

class Secret_DaBoss(Secret_Enemy):
    def __init__(self, container, ypos, xpos, enemy, sniper, moving_enemy):
        self.isAlive = False
        if enemy.isAlive == moving_enemy.isAlive == sniper.isAlive == False:
            pygame.sprite.Sprite.__init__(self)
            self.container = container
            self.side_speed = 1
            self.top_speed = 4
            self.image = pygame.image.load("Image/mothership.gif").convert_alpha()
            self.image = pygame.transform.scale(self.image, (250, 250))
            self.rect = self.image.get_rect()
            self.rect.centerx = self.container.centerx + xpos
            self.rect.y = ypos
            self.life = random.randrange(1000,10000,1000)
            self.isAlive = True


    def update(self, bullet_group, ship, enemy_group, platform_group, power_up_group, camera):
        Secret_Enemy.update(self, bullet_group, ship, enemy_group, platform_group, power_up_group, camera)

    def collide(self, bullet_group, enemy_group, platform_group, dir):
        n = 1
        for b in bullet_group:
            if pygame.sprite.collide_rect(self, b):
                if self.rect.bottom <= b.rect.top:
                    self.life -= 1
                    b.kill()
        for e in enemy_group:
            if pygame.sprite.collide_rect(self, e):
                if dir == "up" and self.rect.top <= e.rect.bottom - 100:
                    self.rect.top = e.rect.bottom
                elif dir == "down" and self.rect.bottom >= e.rect.top:
                    self.rect.bottom = e.rect.top
                elif dir == "left" and self.rect.left <= e.rect.right - 100:
                    self.rect.left = e.rect.right
                elif dir == "right" and self.rect.right >= e.rect.left + 100:
                    self.rect.right = e.rect.left
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if dir == "left" and self.rect.left > p.rect.right:
                    if dir == "right" and self.rect.right < p.rect.left:
                        if dir == "up" and self.rect.top < p.rect.bottom -100:
                            self.rect.top = self.rect.top
                            print ("Hit Top")
                if dir == "left" and self.rect.left > p.rect.right:
                    if dir == "right" and self.rect.right < p.rect.left:
                        if dir == "down" and self.rect.bottom > p.rect.top + 100:
                            self.rect.bottom = self.rect.bottom
                            print("Hit Bottom")
                if n == 1:
                    if dir == "left" and self.rect.left <= p.rect.right:
                        self.side_speed = -self.side_speed
                        n = -n
                if n == -1:
                    if dir == "right" and self.rect.right >= p.rect.left:
                        self.side_speed = -self.side_speed
                        n = -n
                if self.rect.top < 30:
                    self.rect.top = 30




