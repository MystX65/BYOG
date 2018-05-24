import pygame, random

GRAY = (80,80,80)
level = [
    "PPPPPPPPPPPPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P           PP     P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P      P           P",
    "P            PPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P          PPP     P",
    "PPPPPP             P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P            PPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPPPP             P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPPPPPPPPPPPPPPPPPP", ]
level2 = [
    "PPPPPPPPPPPPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P             P    P",
    "P                  P",
    "P                  P",
    "P    P             P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P          P       P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P    PP            P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P       P          P",
    "P                  P",
    "P  P           P   P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P       P          P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P       P          P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P             P    P",
    "P                  P",
    "P      P           P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPPPPPPPPPPPPPPPPPP", ]
level3 = [
    "PPPPPPPPPPPPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P   P          PP  P",
    "P                  P",
    "P          P       P",
    "P                  P",
    "P P                P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P           PP     P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PP  PPPPPPPPPPPPPP P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPP  PPPPPPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P  PPPPPPPPPPPP    P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P  PPPPPPPPPPPPPP  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPPPPPP  PPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P  PPPPPPPPPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P PPPPPPPPPPPPPP   P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPPPPPPPPPPPPPPPPPP", ]
level4 = [
    "PPPPPPPPPPPPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P             P    P",
    "P                  P",
    "P                  P",
    "P    P             P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P       PPPPPP     P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P          P       P",
    "P                  P",
    "P     PPPPPPPPPP   P",
    "P                  P",
    "P                  P",
    "P    PP            P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P      PPPPPPPP    P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P  P       PPPPP   P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P       P          P",
    "P       P          P",
    "P       P          P",
    "P       P          P",
    "P       P          P",
    "P       P          P",
    "P       P          P",
    "P       P          P",
    "P       P     P    P",
    "P       P          P",
    "P      PPPP        P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPPPPPPPPPPPPPPPPPP", ]
level5 = [
    "PPPPPPPPPPPPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P    P        P    P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P    P        P    P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P    P        P    P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P        P         P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P   P         P    P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P      PPPPP       P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P  PPPPPPPPPPPPP   P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P       PP         P",
    "P                  P",
    "P       PP         P",
    "P                  P",
    "P                  P",
    "P       PP         P",
    "P                  P",
    "P                  P",
    "P       PP         P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPPPPPPPPPPPPPPPPPP", ]
level6 = [
    "PPPPPPPPPPPPPPPPPPPP",
    "PPPPP         PPPPPP",
    "PPPPP         PPPPPP",
    "PPPPP         PPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P   P         P    P",
    "P                  P",
    "P        P         P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P PPPP             P",
    "P            PP    P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P    PPP           P",
    "P                  P",
    "P                  P",
    "P           PPPP   P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P      PPPPPP      P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P    PPPPPPPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P PPPPPPPPPPPPP    P",
    "P                  P",
    "P                  P",
    "P     PPPPPPPPPPPPPP",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPPPPPPPPPPPPP    P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "P                  P",
    "PPPPPPPPPPPPPPPPPPPP", ]

class Platform(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Image/asteroid.gif").convert_alpha()
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = pygame.Rect(xpos ,ypos ,32,32)


class Create(pygame.sprite.Sprite):
    def __init__(self, level, platform_group ):
        pygame.sprite.Sprite.__init__(self)
        self.x = self.y = 0
        # build the level
        for row in level:
            for col in row:
                if col == "P":
                    p = Platform(self.x, self.y)
                    platform_group.add(p)
                self.x += 32
            self.y += 32
            self.x = 0