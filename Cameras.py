import pygame
WIN_W = 16*32
WIN_H = 700
class Camera:
    def __init__(self, width, height):
        self.x_offset = 0
        self.y_offset = 0
        self.width = width
        self.height = height


    def apply(self,obj):
        return pygame.Rect(obj.rect.x + self.x_offset, obj.rect.y + self.y_offset, obj.rect.width, obj.rect.height)

    def update(self,ship, camera_entity):
        self.x_offset = -ship.rect.x + WIN_W/2
        self.y_offset = -camera_entity.rect.y + WIN_H/2

        # Stop scrolling at left edge
        if self.x_offset > 0:
            self.x_offset = 0
        # Stop scrolling at the right edge
        elif self.x_offset < -(self.width - WIN_W):
            self.x_offset = -(self.width - WIN_W)
        # Stop scrolling at top
        if self.y_offset > 0:
            self.y_offset = 0
        # Stop scrolling at the bottom
        elif self.y_offset < -(self.height - WIN_H):
            self.y_offset = -(self.height - WIN_H)

class Camera_Entity(pygame.sprite.Sprite):
    def __init__(self, container):
        pygame.sprite.Sprite.__init__(self)
        self.container = container
        self.image = pygame.Surface((0,0)).convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = container.centerx
        self.rect.y = container.bottom
        self.is_moving = False
        self.check = False
        self.offscreen = False
        self.offscreen2 = False
        self.offscreen3 = False

    def update(self, ship):
        if self.rect.y != 350:
            self.rect.y -= 1

        if self.rect.y < self.container.bottom - WIN_H/2:
            self.is_moving = True
            self.check = True
        if self.rect.y <= 350:
            self.check = False
        if ship.rect.y + 50 > self.rect.y + WIN_H/2:
            self.offscreen = True
        else:
            self.offscreen = False
        if ship.rect.y < self.rect.y - WIN_H/2:
            self.offscreen3 = True
        else:
            self.offscreen3 = False
        if self.check == False:
            self.offscreen = False
        if self.rect.y <= 350 and ship.rect.y >= 651:
            self.offscreen2 = True
        else:
            self.offscreen2 = False

    def new_level(self, container):
        self.rect.centerx = container.centerx
        self.rect.y = container.bottom




