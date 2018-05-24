from Power_Ups import *
import pygame, random
WHITE = (255,255,255)
GRAY = (80,80,80)
GREEN = (75, 150,75)
BLACK = (0,0,0)
RED = (232,5,5)

WIN_W = 16*32
WIN_H = 700

SHIP_WIDTH = 30
SHIP_HEIGHT = 50

class Secret_Ship(pygame.sprite.Sprite):
    def __init__(self,container):
        pygame.sprite.Sprite.__init__(self)
        self.container = container
        self.side_speed = 5
        self.top_speed = 4
        self.image = pygame.image.load("Image/Space_Hero.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.container.centerx
        self.rect.y = self.container.bottom-(3*self.rect.height)
        self.life = 20
        self.shooting_type = 1
        self.power_up_active = True
        self.powerNumber = 0
        self.power_timer = 0

    def update(self, platform_group, enemy_group, timer, ship, power_up_group, camera_entity):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and camera_entity.offscreen3 == False:
            self.rect.y -= self.top_speed
            self.collide(platform_group, "up", enemy_group)
        if key[pygame.K_s]:
            if camera_entity.offscreen == False:
                if camera_entity.offscreen2 == False:
                    self.rect.y +=self.top_speed
                    self.collide(platform_group, "down",enemy_group)
        if key[pygame.K_a]:
            self.rect.x -= self.side_speed
            self.collide(platform_group, "left",enemy_group)
        if key[pygame.K_d]:
            self.rect.x += self.side_speed
            self.collide(platform_group, "right",enemy_group)

        if self.powerNumber == 0:
            self.power_up(16, timer, 2000, ship, power_up_group)
        elif self.powerNumber == 1:
            self.power_up(10, timer, 1000, ship, power_up_group)
        elif self.powerNumber == 2:
            self.power_up(5, timer, 100, ship, power_up_group)

        if self.powerNumber == 3:
            self.power_timer += 1

        if self.power_timer >= 1000:
            self.powerNumber = 2
            self.shooting_type = self.shooting_type -1
            self.power_timer = 0

        if camera_entity.offscreen and camera_entity.check:
            self.rect.y -= 1

        if self.life <= 0:
            self.kill()

    def power_up(self, life, timer, time, ship, power_up_group):
        if self.life <= life:
            if timer % time == 0:
                self.power_up_active = True
                if self.power_up_active == True:
                    upgrade = Upgrade(int(random.choice('4')), ship)
                    if upgrade.appearance == True:
                        power_up_group.add(upgrade)
                        self.power_up_active = False
                        self.powerNumber += 1

    def new_level(self):
        self.rect.centerx = self.container.centerx
        self.rect.y = self.container.bottom - (3 * self.rect.height)

    def collide(self, platform_group, dir, enemy_group):
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if dir == "up" and self.rect.top < p.rect.bottom:
                    self.rect.top = p.rect.bottom
                elif dir == "down" and self.rect.bottom > p.rect.top:
                    self.rect.bottom = p.rect.top
                elif dir == "left" and self.rect.left < p.rect.right:
                    self.rect.left = p.rect.right
                elif dir == "right" and self.rect.right > p.rect.left:
                    self.rect.right = p.rect.left
        for e in enemy_group:
            if pygame.sprite.collide_rect(self, e):
                if dir == "up" and self.rect.top < e.rect.bottom:
                    self.rect.top = e.rect.bottom
                elif dir == "down" and self.rect.bottom > e.rect.top:
                    self.rect.bottom = e.rect.top
                elif dir == "left" and self.rect.left < e.rect.right:
                    self.rect.left = e.rect.right
                elif dir == "right" and self.rect.right > e.rect.left:
                    self.rect.right = e.rect.left

