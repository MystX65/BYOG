import pygame

pygame.init()

WHITE = (255,255,255)
GRAY = (80,80,80)
GREEN = (75, 150,75)
BLACK = (0,0,0)
RED = (232,5,5)
BLUE_SILVER = (93,135,178)

font100 = pygame.font.Font(None, 100)
font90 = pygame.font.Font(None, 40)
font30 = pygame.font.Font(None, 30)

WIN_W = 16*32
WIN_H = 700


class Text:
    def __init__(self, font, text, xpos, ypos, color):
        self.image = font.render(text, 1, color)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(xpos - self.rect.width/2, ypos - self.rect.width/2)

screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
title = Text(font100, "", 0,0, WHITE)
title.image = pygame.image.load("Image/title-screen.psd").convert_alpha()
title.image = pygame.transform.scale(title.image, (WIN_W, WIN_H))
subStart = Text(font90,"Click here to start!", screen.get_rect().centerx, WIN_H -200, WHITE )
instructions1 = Text(font30,"You are on your way back to Earth in a space ship. ",screen.get_rect().centerx,WIN_H-300, GREEN)
instructions2 = Text(font30, "Unfortunately, space pirates are here to kidnap you. ", screen.get_rect().centerx, WIN_H-260, GREEN)
instructions3 = Text(font30, "You need to kill them before you can return home! ", screen.get_rect().centerx,WIN_H-240, GREEN )
instructions4 = Text(font30, "Use the AWSD keys to move and spacebar to shoot. ", screen.get_rect().centerx, WIN_H - 200, GREEN)
instructions5 = Text(font30, "CAUTION: There is a meteor storm coming!", screen.get_rect().centerx,WIN_H , GREEN )
back_button = Text(font100, "", WIN_W/2 - 40,300, WHITE)
back_button.image = pygame.image.load("Image/Back_Button.png")
back_button.image = pygame.transform.scale(back_button.image, (80,40))
credit = Text(font100, "TrueGaming", screen.get_rect().centerx, WIN_H-400, BLUE_SILVER)
credit1 = Text(font30, "Programed by:    Joshua Chen", screen.get_rect().centerx-3, WIN_H - 200, WHITE)
credit2 = Text(font30, "Designed by:      Joshua Chen", screen.get_rect().centerx- 5, WIN_H - 170, WHITE)
credit3 = Text(font30, "Produced by:  TrueGaming", screen.get_rect().centerx, WIN_H - 390, WHITE)
arrow_keys = Text(font100, "", 50,300, WHITE)
arrow_keys.image= pygame.image.load("Image/arrow_keys.png").convert_alpha()
arrow_keys.image = pygame.transform.scale(arrow_keys.image, (200, 200))
spacebar = Text(font100, "", 50, 550, WHITE)
spacebar.image = pygame.image.load("Image/spacebar.png").convert_alpha()
spacebar.image = pygame.transform.scale(spacebar.image, (400,50))
goodbye = Text(font30, "Press Delete to exit the game.", screen.get_rect().centerx, WIN_H / 2, WHITE)
win = Text(font30, "Congratulations! You killed them all!", screen.get_rect().centerx, WIN_H / 2, BLACK)
win1 = Text(font30, "Press Delete to exit the game.", screen.get_rect().centerx, WIN_H / 2 +40, BLACK)
thanks = Text(font30,"Special Thanks To", screen.get_rect().centerx, WIN_H - 100, RED)
no = Text(font100, "NO ONE", screen.get_rect().centerx, WIN_H, RED)
intro1 = Text(font30, "You are Blep the alien baby captured by humans.", screen.get_rect().centerx, WIN_H-300, GREEN)
intro2 = Text(font30, "You are located in their space station.", screen.get_rect().centerx, WIN_H-325, GREEN)
intro3 = Text(font30, "You have to escape the human's grasp.", screen.get_rect().centerx, WIN_H-290, GREEN)
intro4 = Text(font30, "The only way is to pass through their defense.", screen.get_rect().centerx, WIN_H-220, GREEN)
intro5 = Text(font30, "You need to kill them before you can move on", screen.get_rect().centerx, WIN_H-190, GREEN)
intro6 = Text(font30, "to the next line of defense.", screen.get_rect().centerx, WIN_H-250, GREEN)
intro7 = Text(font30, "CAUTION: There is a meteor storm coming!", screen.get_rect().centerx,WIN_H , GREEN )
secret_win = Text(font30, "Congratulations! You killed them all! ", screen.get_rect().centerx, WIN_H / 2, BLACK)
secret_win2 = Text(font30, "You were able to float back to safety.", screen.get_rect().centerx, WIN_H / 2 + 30, BLACK)
secret_win1 = Text(font30, "Press Delete to exit the game.", screen.get_rect().centerx, WIN_H / 2 +40, BLACK)
