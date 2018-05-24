from Enemy import *
from Cameras import *
from Ship import *
from Shooting_Type import *
from Levels import *
from Asteroids import *
from Exit import *
from Text import *
from Secret_Ship import *
from Secret_Enemy import *
import pygame, os, sys, random

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Constants
WHITE = (255,255,255)
GRAY = (80,80,80)
GREEN = (75, 150,75)
BLACK = (0,0,0)
RED = (232,5,5)

WIN_W = 16*32
WIN_H = 700

SHIP_WIDTH = 30
SHIP_HEIGHT = 50


def main():
    # initialize variables
    pygame.init()
    fps = 60
    clock = pygame.time.Clock()
    play1 = True
    play2 = True
    play3 = True
    timer = 0
    numBullet = 0
    bullet_timer = 0
    secret = False
    intro = True
    instruction_screen = True
    instruction = False
    credit_screen = False
    outro = True
    outroin = False
    win_screen = False

    beg_time = pygame.time.get_ticks()

    font30 = pygame.font.Font(None, 30)

    pygame.display.set_caption('Raiden')
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #Sprite Groups
    platform_group = pygame.sprite.Group()
    ship_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    power_up_group = pygame.sprite.Group()
    meteor_group = pygame.sprite.Group()
    heal_group = pygame.sprite.Group()

    container = pygame.Rect(0, 0, len(level[0]) *32, len(level) * 32)
    ship = Ship(container)
    enemy = Enemy(container, WIN_H/2, 0)
    moving_enemy = Moving_Enemy(container, WIN_H/5, 0)
    sniper = Sniper(container, WIN_H/20, 0)
    camera = Camera(container.width, container.height)
    camera_entity = Camera_Entity(container)
    enemy_group.add(enemy, moving_enemy, sniper)
    ship_group.add(ship, camera_entity)

    Create(level, platform_group)

    # create objects

    while intro:
        if instruction != True and credit_screen != True:
            screen.fill(BLACK)
            screen.blit(title.image, title.rect)
        #screen.blit(subStart, subpos)



        #Checks if window exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 217 and pos[0]<= 297 and pos[1] >= 242 and pos[1] <= 316:
                    if instruction != True and credit_screen != True:
                        intro = False
                elif pos[0] >= 217 and pos[0] <= 297 and pos[1] >= 387 and pos[1]<= 462:
                    instruction = True
                    if instruction == True and credit_screen == False:
                        screen.fill(BLACK)
                        screen.blit(arrow_keys.image, arrow_keys.rect)
                        screen.blit(spacebar.image, spacebar.rect)
                        screen.blit(instructions4.image, instructions4.rect)
                        screen.blit(back_button.image, back_button.rect)
                elif pos[0] >= 217 and pos[0]<= 297 and pos[1] >= 538 and pos[1] <= 614:
                    credit_screen = True
                    if credit_screen == True and instruction == False:
                        screen.fill(BLACK)
                        screen.blit(credit.image, credit.rect)
                        screen.blit(credit1.image, credit1.rect)
                        screen.blit(credit2.image, credit2.rect)
                        screen.blit(credit3.image, credit3.rect)
                        screen.blit(no.image, no.rect)
                        screen.blit(thanks.image, thanks.rect)
                        screen.blit(back_button.image, back_button.rect)
                if pos[0] >= 222 and pos[0] <= 294 and pos[1] >= 307 and pos[1] <= 339:
                    credit_screen = False
                if pos[0] >= 222 and pos[0] <= 294 and pos[1] >= 307 and pos[1] <= 339:
                    instruction = False
                if pos[0] >= 296 and pos[0] <= 302 and pos[1] >= 97 and pos[1] <= 101:
                    secret = True
                    print True


            #Limits FPS of while loop
        clock.tick(fps)
            #Writes to main surface
        pygame.display.flip()
    if secret == False:
        while instruction_screen:
            screen.fill(BLACK)
            # Blinking Text : Click To Start
            cur_time = pygame.time.get_ticks()
            if ((cur_time - beg_time) % 1000) < 500:
                screen.blit(subStart.image, subStart.rect)

            screen.blit(instructions1.image, instructions1.rect)
            screen.blit(instructions2.image, instructions2.rect)
            screen.blit(instructions3.image, instructions3.rect)
            screen.blit(instructions5.image, instructions5.rect)


            # Checks if window exit button pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] != 0:
                    screen.blit(subStart.image, subStart.rect)
                    pygame.display.flip()
                    pygame.time.wait(1500)
                    instruction_screen = False

                    # Limits FPS of while loop
            clock.tick(fps)
            # Writes to main surface
            pygame.display.flip()

        while play1:
            score = timer/100
            # Chekcs if window exit button pressed
            Quit()
            key = pygame.key.get_pressed()

            if key[pygame.K_SPACE] == 0:
                bullet_timer = 19
            if key[pygame.K_SPACE]:
                bullet_timer += 1
                if ship.shooting_type != 4:
                    if bullet_timer %20 ==0:
                        if bullet_group.__len__() < 6:
                            ShootingTypes(Bullet, ship, bullet_group)
                else:
                    ShootingTypes(Bullet, ship, bullet_group)

            if timer % 40 == 0:
                if ship.rect.y  <= enemy.rect.bottom + 500:
                    if enemy.isAlive:
                        Straight_Double(Enemy_Bullet, enemy, enemy_bullet_group)
            if timer % 200 == 0:
                if ship.rect.y <= moving_enemy.rect.bottom + 300:
                    if moving_enemy.isAlive:
                        Shot_Gun(Enemy_Bullet, moving_enemy, enemy_bullet_group)
            if timer % 150 == 0:
                if ship.rect.y <= enemy.rect.bottom + 1000:
                    if sniper.isAlive:
                        Missles(Enemy_Target_Missles, sniper, enemy_bullet_group)

            if timer%(random.randrange(200, 500, 40))== 0:
                meteor = Meteor(ship)
                meteor_group.add(meteor)
            # run update
            if camera_entity.is_moving == True:
                ship.update(platform_group,enemy_group, timer, ship, power_up_group, camera_entity)
            camera_entity.update(ship)
            camera.update(ship, camera_entity)
            bullet_group.update(platform_group, enemy_group)
            enemy_bullet_group.update(platform_group, ship)
            enemy_group.update(bullet_group, ship, enemy_group, platform_group, heal_group, camera)
            power_up_group.update(ship,platform_group)
            meteor_group.update(ship)
            heal_group.update(ship, platform_group)

            #create life and score boards
            ship.life = str(ship.life)
            health = Text(font30, "Life Remaining: "+ship.life, screen.get_rect().centerx - 150, 100, GREEN)

            score = str(score)
            score_text = Text(font30,"Time: " + score,screen.get_rect().centerx - 206, 80, GREEN)
            #Bullet Boundary
            for b in bullet_group:
                if camera.apply(b).centery < -20:
                    b.kill()

            #Instant Death
            if camera.apply(ship).centerx < 47 or camera.apply(ship).centerx > 465:
                ship.life = 0
            if camera.apply(ship).y < -10:
                ship.life = 0

            # Draw Objects
            screen.fill(BLACK)
            for p in platform_group:
                screen.blit(p.image, camera.apply(p))
            for s in ship_group:
                screen.blit(s.image, camera.apply(s))
            for b in bullet_group:
                screen.blit(b.image, camera.apply(b))
            for e in enemy_group:
                screen.blit(e.image, camera.apply(e))
            for t in enemy_bullet_group:
                screen.blit(t.image, camera.apply(t))
            for p in power_up_group:
                screen.blit(p.image, camera.apply(p))
            for m in meteor_group:
                screen.blit(m.image, camera.apply(m))
            for h in heal_group:
                screen.blit(h.image, camera.apply(h))
            screen.blit(ship.image, camera.apply(ship))
            screen.blit(health.image, health.rect)
            screen.blit(score_text.image, score_text.rect)
            # limits frames per iteration of while loop
            timer += 1
            clock.tick(fps)
            #Writes to main surface
            pygame.display.flip()

            #change datatype back to integer
            ship.life = int(ship.life)
            score = int(score)

            if ship.life <= 0:
                outroin = True
                play1 = play2 = play3 = False
            if enemy.isAlive == moving_enemy.isAlive == sniper.isAlive == False:
                #creates new map
                for x in power_up_group.sprites():
                    ship.shooting_type += 1
                for y in heal_group.sprites():
                    ship.life += 1
                platform_group.empty()
                enemy_bullet_group.empty()
                meteor_group.empty()
                power_up_group.empty()
                heal_group.empty()

                container = pygame.Rect(0, 0, len(level2[0]) * 32, len(level2) * 32)

                Create(level2, platform_group)

                ship.new_level()
                camera_entity.new_level(container)

                #adds enemy to new map
                moving_enemy1 = Moving_Enemy(container, WIN_H - 50, 50)
                moving_enemy2 = Moving_Enemy(container, WIN_H/2, 0)
                moving_enemy3 = Moving_Enemy(container, WIN_H - 300, 100)
                sniper1 = Sniper(container, WIN_H - 200, 90)
                sniper2 = Sniper(container, WIN_H - 200, -90)
                enemy_group.add(moving_enemy1, moving_enemy2, moving_enemy3, sniper1, sniper2)

                #Begins new level
                play1 = False

        while play2:

            score = timer/100

            Quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] == 0:
                bullet_timer = 19
            if key[pygame.K_SPACE]:
                bullet_timer += 1
                if ship.shooting_type != 4:
                    if bullet_timer %20 ==0:
                        if bullet_group.__len__() < 6:
                            ShootingTypes(Bullet, ship, bullet_group)
                else:
                    ShootingTypes(Bullet, ship, bullet_group)

            if timer % random.randrange(100,200,20) == 0:
                if ship.rect.y <= moving_enemy1.rect.bottom + 300:
                    if moving_enemy1.isAlive:
                        Shot_Gun(Enemy_Bullet, moving_enemy1, enemy_bullet_group)
            if timer % random.randrange(100,200,20) == 0:
                if ship.rect.y <= moving_enemy2.rect.bottom + 300:
                    if moving_enemy2.isAlive:
                        Shot_Gun(Enemy_Bullet, moving_enemy2, enemy_bullet_group)
            if timer % random.randrange(100,200,20) == 0:
                if ship.rect.y <= moving_enemy3.rect.bottom + 300:
                    if moving_enemy3.isAlive:
                        Shot_Gun(Enemy_Bullet, moving_enemy3, enemy_bullet_group)
            if timer % random.randrange(150, 350, 50) == 0:
                if ship.rect.y <= enemy.rect.bottom + 1000:
                    if sniper1.isAlive:
                        Missles(Enemy_Target_Missles, sniper1, enemy_bullet_group)
            if timer % random.randrange(150, 350, 50) == 0:
                if ship.rect.y <= enemy.rect.bottom + 1000:
                    if sniper2.isAlive:
                        Missles(Enemy_Target_Missles, sniper2, enemy_bullet_group)

            if timer % (random.randrange(200, 500, 40)) == 0:
                meteor = Meteor(ship)
                meteor_group.add(meteor)


            # run update
            if camera_entity.is_moving == True:
                ship.update(platform_group, enemy_group, timer, ship, power_up_group, camera_entity)
            camera_entity.update(ship)
            camera.update(ship, camera_entity)
            bullet_group.update(platform_group, enemy_group)
            enemy_bullet_group.update(platform_group, ship)
            enemy_group.update(bullet_group, ship, enemy_group, platform_group, heal_group, camera)
            power_up_group.update(ship, platform_group)
            meteor_group.update(ship)
            heal_group.update(ship, platform_group)

            ship.life = str(ship.life)
            health = Text(font30, "Life Remaining: " + ship.life, screen.get_rect().centerx - 150, 100, GREEN)

            score = str(score)
            score_text = Text(font30, "Time: " + score, screen.get_rect().centerx - 205, 80, GREEN)


            # Bullet Boundary
            for b in bullet_group:
                if camera.apply(b).centery < -20:
                    b.kill()
            # Instant Death
            if camera.apply(ship).centerx < 47 or camera.apply(ship).centerx > 465:
                ship.life = 0
            if camera.apply(ship).y < 0:
                ship.life = 0

            screen.fill(BLACK)
            for p in platform_group:
                screen.blit(p.image, camera.apply(p))
            for s in ship_group:
                screen.blit(s.image, camera.apply(s))
            for b in bullet_group:
                screen.blit(b.image, camera.apply(b))
            for e in enemy_group:
                screen.blit(e.image, camera.apply(e))
            for t in enemy_bullet_group:
                screen.blit(t.image, camera.apply(t))
            for p in power_up_group:
                screen.blit(p.image, camera.apply(p))
            for m in meteor_group:
                screen.blit(m.image, camera.apply(m))
            for h in heal_group:
                screen.blit(h.image, camera.apply(h))
            screen.blit(ship.image, camera.apply(ship))
            screen.blit(health.image, health.rect)
            screen.blit(score_text.image, score_text.rect)
            # limits frames per iteration of while loop
            timer += 1
            clock.tick(fps)
            # Writes to main surface
            pygame.display.flip()

            # change datatype back to integer
            ship.life = int(ship.life)
            score = int(score)

            if ship.life <= 0:
                outroin = True
                play2 = play3 = False

            if moving_enemy1.isAlive == moving_enemy2.isAlive == moving_enemy3.isAlive == sniper1.isAlive == sniper2.isAlive == False:
                #creates new map
                for x in power_up_group.sprites():
                    ship.shooting_type += 1
                for y in heal_group.sprites():
                    ship.life += 1
                platform_group.empty()
                enemy_bullet_group.empty()
                power_up_group.empty()
                meteor_group.empty()
                heal_group.empty()

                container = pygame.Rect(0, 0, len(level3[0]) * 32, len(level3) * 32)

                Create(level3, platform_group)

                ship.new_level()
                camera_entity.new_level(container)

                #adds enemy to new map
                daboss = DaBoss(container, WIN_H/20, 0, enemy, sniper, moving_enemy)
                enemy_group.add(daboss)

                #Begins new level
                play2 = False

        while play3:
            score = timer/100

            Quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] == 0:
                bullet_timer = 19
            if key[pygame.K_SPACE]:
                bullet_timer += 1
                if ship.shooting_type != 4:
                    if bullet_timer %20 ==0:
                        if bullet_group.__len__() < 6:
                            ShootingTypes(Bullet, ship, bullet_group)
                else:
                    ShootingTypes(Bullet, ship, bullet_group)

            Ultimate_Fire(Enemy_Target_Missles, daboss, enemy_bullet_group, timer)

            if timer%(random.randrange(200, 500, 40))== 0:
                meteor = Meteor(ship)
                meteor_group.add(meteor)

            # run update
            if camera_entity.is_moving == True:
                ship.update(platform_group, enemy_group, timer, ship, power_up_group, camera_entity)
            camera_entity.update(ship)
            camera.update(ship, camera_entity)
            bullet_group.update(platform_group, enemy_group)
            enemy_bullet_group.update(platform_group, ship)
            enemy_group.update(bullet_group, ship, enemy_group, platform_group, heal_group, camera)
            power_up_group.update(ship, platform_group)
            meteor_group.update(ship)
            heal_group.update(ship, platform_group)

            daboss.life = str(daboss.life)
            boss_life = Text(font30,"Health: " + daboss.life, screen.get_rect().centerx + 150, 70, RED)

            ship.life = str(ship.life)
            health = Text(font30, "Life Remaining: " + ship.life, screen.get_rect().centerx - 150, 100, GREEN)

            score = str(score)
            score_text = Text(font30, "Time: " + score, screen.get_rect().centerx - 200, 80, GREEN)

            # Bullet Boundary
            for b in bullet_group:
                if camera.apply(b).centery < -20:
                    b.kill()
            # Instant Death
            if camera.apply(ship).centerx < 47 or camera.apply(ship).centerx > 465:
                ship.life = 0
            if camera.apply(ship).y < 0:
                ship.life = 0

            screen.fill(BLACK)
            for p in platform_group:
                screen.blit(p.image, camera.apply(p))
            for s in ship_group:
                screen.blit(s.image, camera.apply(s))
            for b in bullet_group:
                screen.blit(b.image, camera.apply(b))
            for e in enemy_group:
                screen.blit(e.image, camera.apply(e))
            for t in enemy_bullet_group:
                screen.blit(t.image, camera.apply(t))
            for p in power_up_group:
                screen.blit(p.image, camera.apply(p))
            for m in meteor_group:
                screen.blit(m.image, camera.apply(m))
            for h in heal_group:
                screen.blit(h.image, camera.apply(h))
            screen.blit(ship.image, camera.apply(ship))
            screen.blit(health.image, health.rect)
            screen.blit(score_text.image, score_text.rect)
            screen.blit(boss_life.image, boss_life.rect)
            # limits frames per iteration of while loop
            timer += 1
            clock.tick(fps)
            # Writes to main surface
            pygame.display.flip()

            # change datatype back to integer
            ship.life = int(ship.life)
            score = int(score)
            daboss.life = int(daboss.life)

            if ship.life <= 0:
                play3 = False
                outroin = True

            if daboss.isAlive == False:
                win_screen = True
                play3 = False

        while outro:

            while outroin:
                screen.fill(BLACK)
                keyoutro = pygame.key.get_pressed()
                screen.blit(goodbye.image, goodbye.rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if keyoutro[pygame.K_BACKSPACE]:
                        sys.exit()
                clock.tick(fps)
                pygame.display.flip()
            while win_screen:
                screen.fill(WHITE)
                keyoutro = pygame.key.get_pressed()
                screen.blit(win.image, win.rect)
                screen.blit(win1.image, win1.rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if keyoutro[pygame.K_BACKSPACE]:
                        sys.exit()
                clock.tick(fps)
                pygame.display.flip()
    elif secret == True:
        secret_platform_group = pygame.sprite.Group()
        secret_ship_group = pygame.sprite.Group()
        secret_bullet_group = pygame.sprite.Group()
        secret_enemy_bullet_group = pygame.sprite.Group()
        secret_enemy_group = pygame.sprite.Group()
        secret_power_up_group = pygame.sprite.Group()
        secret_meteor_group = pygame.sprite.Group()
        secret_heal_group = pygame.sprite.Group()

        secret_ship = Secret_Ship(container)
        secret_enemy = Secret_Enemy(container, WIN_H / 2, -200)
        secret_enemy1 = Secret_Enemy(container, WIN_H/2, 210)
        secret_moving_enemy = Secret_Moving_Enemy(container, WIN_H / 5, 0)
        secret_sniper = Secret_Sniper(container, WIN_H / 20, 0)
        camera = Camera(container.width, container.height)
        camera_entity = Camera_Entity(container)
        secret_enemy_group.add(secret_enemy,secret_enemy1, secret_moving_enemy, secret_sniper)
        secret_ship_group.add(secret_ship, camera_entity)

        Create(level4, secret_platform_group)

        while instruction_screen:
            screen.fill(BLACK)
            # Blinking Text : Click To Start
            cur_time = pygame.time.get_ticks()
            if ((cur_time - beg_time) % 1000) < 500:
                screen.blit(subStart.image, subStart.rect)

            screen.blit(intro1.image, intro1.rect)
            screen.blit(intro2.image, intro2.rect)
            screen.blit(intro3.image, intro3.rect)
            screen.blit(intro4.image, intro4.rect)
            screen.blit(intro5.image, intro5.rect)
            screen.blit(intro6.image, intro6.rect)
            screen.blit(intro7.image, intro7.rect)


            # Checks if window exit button pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] != 0:
                    screen.blit(subStart.image, subStart.rect)
                    pygame.display.flip()
                    pygame.time.wait(1500)
                    instruction_screen = False

                    # Limits FPS of while loop
            clock.tick(fps)
            # Writes to main surface
            pygame.display.flip()

        while play1:
            secret_score = timer/100
            # Chekcs if window exit button pressed
            Quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] == 0:
                bullet_timer = 19
            if key[pygame.K_SPACE]:
                bullet_timer += 1
                if secret_ship.shooting_type != 4:
                    if bullet_timer % 20 == 0:
                        if secret_bullet_group.__len__()<6:
                            ShootingTypes(Bullet, secret_ship, secret_bullet_group)
                else:
                    ShootingTypes(Bullet, secret_ship, secret_bullet_group)
            if timer % 40 == 0:
                if secret_ship.rect.y  <= secret_enemy.rect.bottom + 500:
                    if secret_enemy.isAlive:
                        Straight_Double(Enemy_Bullet, secret_enemy, secret_enemy_bullet_group)
            if timer % 40 == 0:
                if secret_ship.rect.y  <= secret_enemy1.rect.bottom + 500:
                    if secret_enemy1.isAlive:
                        Straight_Double(Enemy_Bullet, secret_enemy1, secret_enemy_bullet_group)
            if timer % 200 == 0:
                if secret_ship.rect.y <= secret_moving_enemy.rect.bottom + 300:
                    if secret_moving_enemy.isAlive:
                        Shot_Gun(Enemy_Bullet, secret_moving_enemy, secret_enemy_bullet_group)
            if timer % 150 == 0:
                if secret_ship.rect.y <= secret_enemy.rect.bottom + 1000:
                    if secret_sniper.isAlive:
                        Missles(Enemy_Target_Missles, secret_sniper, secret_enemy_bullet_group)

            if timer%(random.randrange(200, 500, 40))== 0:
                secret_meteor = Meteor(ship)
                secret_meteor_group.add(secret_meteor)

            # run update
            if camera_entity.is_moving == True:
                secret_ship.update(secret_platform_group,secret_enemy_group, timer, secret_ship, secret_power_up_group, camera_entity)
            camera_entity.update(secret_ship)
            camera.update(secret_ship, camera_entity)
            secret_bullet_group.update(secret_platform_group, secret_enemy_group)
            secret_enemy_bullet_group.update(secret_platform_group, secret_ship)
            secret_enemy_group.update(secret_bullet_group, secret_ship, secret_enemy_group, secret_platform_group, secret_heal_group, camera)
            secret_power_up_group.update(secret_ship,secret_platform_group)
            secret_meteor_group.update(secret_ship)
            secret_heal_group.update(secret_ship, secret_platform_group)

            #create life and score boards
            secret_ship.life = str(secret_ship.life)
            secret_health = Text(font30, "Life Remaining: "+secret_ship.life, screen.get_rect().centerx - 150, 100, GREEN)

            secret_score = str(secret_score)
            secret_score_text = Text(font30,"Time: " + secret_score,screen.get_rect().centerx - 206, 80, GREEN)
            #Bullet Boundary
            for b in secret_bullet_group:
                if camera.apply(b).centery < -20:
                    b.kill()

            #Instant Death
            if camera.apply(secret_ship).centerx < 47 or camera.apply(secret_ship).centerx > 465:
                secret_ship.life = 0
            if camera.apply(secret_ship).y < 0:
                secret_ship.life = 0

            # Draw Objects
            screen.fill(BLACK)
            for p in secret_platform_group:
                screen.blit(p.image, camera.apply(p))
            for s in secret_ship_group:
                screen.blit(s.image, camera.apply(s))
            for b in secret_bullet_group:
                screen.blit(b.image, camera.apply(b))
            for e in secret_enemy_group:
                screen.blit(e.image, camera.apply(e))
            for t in secret_enemy_bullet_group:
                screen.blit(t.image, camera.apply(t))
            for p in secret_power_up_group:
                screen.blit(p.image, camera.apply(p))
            for m in secret_meteor_group:
                screen.blit(m.image, camera.apply(m))
            for h in secret_heal_group:
                screen.blit(h.image, camera.apply(h))
            screen.blit(secret_ship.image, camera.apply(secret_ship))
            screen.blit(secret_health.image, secret_health.rect)
            screen.blit(secret_score_text.image, secret_score_text.rect)
            # limits frames per iteration of while loop
            timer += 1
            clock.tick(fps)
            #Writes to main surface
            pygame.display.flip()

            #change datatype back to integer
            secret_ship.life = int(secret_ship.life)
            secret_score = int(secret_score)

            if secret_ship.life <= 0:
                outroin = True
                play1 = play2 = play3 = False
            if secret_enemy.isAlive == secret_enemy1.isAlive == secret_moving_enemy.isAlive == secret_sniper.isAlive == False:
                #creates new map
                for x in secret_power_up_group.sprites():
                    secret_ship.shooting_type += 1
                for y in secret_heal_group.sprites():
                    secret_ship.life += 1
                secret_platform_group.empty()
                secret_enemy_bullet_group.empty()
                secret_meteor_group.empty()
                secret_power_up_group.empty()
                secret_heal_group.empty()

                container = pygame.Rect(0, 0, len(level2[0]) * 32, len(level2) * 32)

                Create(level5, secret_platform_group)

                secret_ship.new_level()
                camera_entity.new_level(container)

                #adds enemy to new map
                secret_moving_enemy1 = Secret_Moving_Enemy(container, WIN_H - 50, 50)
                secret_moving_enemy2 = Secret_Moving_Enemy(container, WIN_H/2, 0)
                secret_moving_enemy3 = Secret_Moving_Enemy(container, WIN_H - 300, 100)
                secret_sniper1 = Secret_Sniper(container, WIN_H - 200, 90)
                secret_sniper2 = Secret_Sniper(container, WIN_H - 200, -90)
                secret_enemy_group.add(secret_moving_enemy1, secret_moving_enemy2, secret_moving_enemy3, secret_sniper1, secret_sniper2)

                #Begins new level
                play1 = False

        while play2:

            secret_score = timer/100

            Quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] == 0:
                bullet_timer = 19
            if key[pygame.K_SPACE]:
                bullet_timer += 1
                if secret_ship.shooting_type != 4:
                    if bullet_timer % 20 == 0:
                        if secret_bullet_group.__len__()<6:
                            ShootingTypes(Bullet, secret_ship, secret_bullet_group)
                else:
                    ShootingTypes(Bullet, secret_ship, secret_bullet_group)
            if timer % random.randrange(100,200,20) == 0:
                if secret_ship.rect.y <= secret_moving_enemy1.rect.bottom + 300:
                    if secret_moving_enemy1.isAlive:
                        Shot_Gun(Enemy_Bullet, secret_moving_enemy1, secret_enemy_bullet_group)
            if timer % random.randrange(100,200,20) == 0:
                if secret_ship.rect.y <= secret_moving_enemy2.rect.bottom + 300:
                    if secret_moving_enemy2.isAlive:
                        Shot_Gun(Enemy_Bullet, secret_moving_enemy2, secret_enemy_bullet_group)
            if timer % random.randrange(100,200,20) == 0:
                if secret_ship.rect.y <= secret_moving_enemy3.rect.bottom + 300:
                    if secret_moving_enemy3.isAlive:
                        Shot_Gun(Enemy_Bullet, secret_moving_enemy3, secret_enemy_bullet_group)
            if timer % random.randrange(150, 350, 50) == 0:
                if secret_ship.rect.y <= secret_enemy.rect.bottom + 1000:
                    if secret_sniper1.isAlive:
                        Missles(Enemy_Target_Missles, secret_sniper1, secret_enemy_bullet_group)
            if timer % random.randrange(150, 350, 50) == 0:
                if secret_ship.rect.y <= secret_enemy.rect.bottom + 1000:
                    if secret_sniper2.isAlive:
                        Missles(Enemy_Target_Missles, secret_sniper2, secret_enemy_bullet_group)

            if timer % (random.randrange(200, 500, 40)) == 0:
                secret_meteor = Meteor(secret_ship)
                secret_meteor_group.add(secret_meteor)


            # run update
            if camera_entity.is_moving == True:
                secret_ship.update(secret_platform_group, secret_enemy_group, timer, secret_ship, secret_power_up_group, camera_entity)
            camera_entity.update(secret_ship)
            camera.update(secret_ship, camera_entity)
            secret_bullet_group.update(secret_platform_group, secret_enemy_group)
            secret_enemy_bullet_group.update(secret_platform_group, secret_ship)
            secret_enemy_group.update(secret_bullet_group, secret_ship, secret_enemy_group, secret_platform_group, secret_heal_group, camera)
            secret_power_up_group.update(secret_ship, secret_platform_group)
            secret_meteor_group.update(secret_ship)
            secret_heal_group.update(secret_ship, secret_platform_group)

            secret_ship.life = str(secret_ship.life)
            secret_health = Text(font30, "Life Remaining: " + secret_ship.life, screen.get_rect().centerx - 150, 100, GREEN)

            secret_score = str(secret_score)
            secret_score_text = Text(font30, "Time: " + secret_score, screen.get_rect().centerx - 205, 80, GREEN)


            # Bullet Boundary
            for b in secret_bullet_group:
                if camera.apply(b).centery < -20:
                    b.kill()

            # Instant Death
            if camera.apply(secret_ship).centerx < 47 or camera.apply(secret_ship).centerx > 465:
                secret_ship.life = 0
            if camera.apply(secret_ship).y < 0:
                secret_ship.life = 0

            screen.fill(BLACK)
            for p in secret_platform_group:
                screen.blit(p.image, camera.apply(p))
            for s in secret_ship_group:
                screen.blit(s.image, camera.apply(s))
            for b in secret_bullet_group:
                screen.blit(b.image, camera.apply(b))
            for e in secret_enemy_group:
                screen.blit(e.image, camera.apply(e))
            for t in secret_enemy_bullet_group:
                screen.blit(t.image, camera.apply(t))
            for p in secret_power_up_group:
                screen.blit(p.image, camera.apply(p))
            for m in secret_meteor_group:
                screen.blit(m.image, camera.apply(m))
            for h in secret_heal_group:
                screen.blit(h.image, camera.apply(h))
            screen.blit(secret_ship.image, camera.apply(secret_ship))
            screen.blit(secret_health.image, secret_health.rect)
            screen.blit(secret_score_text.image, secret_score_text.rect)
            # limits frames per iteration of while loop
            timer += 1
            clock.tick(fps)
            # Writes to main surface
            pygame.display.flip()

            # change datatype back to integer
            secret_ship.life = int(secret_ship.life)
            secret_score = int(secret_score)

            if secret_ship.life <= 0:
                outroin = True
                play2 = play3 = False

            if secret_moving_enemy1.isAlive == secret_moving_enemy2.isAlive == secret_moving_enemy3.isAlive == secret_sniper1.isAlive == secret_sniper2.isAlive == False:
                #creates new map
                for x in secret_power_up_group.sprites():
                    secret_ship.shooting_type += 1
                for y in secret_heal_group.sprites():
                    secret_ship.life += 1
                secret_platform_group.empty()
                secret_enemy_bullet_group.empty()
                secret_power_up_group.empty()
                secret_meteor_group.empty()
                secret_heal_group.empty()

                container = pygame.Rect(0, 0, len(level3[0]) * 32, len(level3) * 32)

                Create(level6, secret_platform_group)

                secret_ship.new_level()
                camera_entity.new_level(container)

                #adds enemy to new map
                secret_daboss = Secret_DaBoss(container, WIN_H/20, 0, secret_enemy, secret_sniper, secret_moving_enemy)
                secret_enemy_group.add(secret_daboss)

                #Begins new level
                play2 = False

        while play3:
            secret_score = timer/100

            Quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] == 0:
                bullet_timer = 19
            if key[pygame.K_SPACE]:
                bullet_timer += 1
                if secret_ship.shooting_type != 4:
                    if bullet_timer % 20 == 0:
                        if secret_bullet_group.__len__()<6:
                            ShootingTypes(Bullet, secret_ship, secret_bullet_group)
                else:
                    ShootingTypes(Bullet, secret_ship, secret_bullet_group)
            Ultimate_Fire2(Enemy_Target_Missles, secret_daboss, secret_enemy_bullet_group, timer)

            if timer%(random.randrange(200, 500, 40))== 0:
                secret_meteor = Meteor(secret_ship)
                secret_meteor_group.add(secret_meteor)

            # run update
            if camera_entity.is_moving == True:
                secret_ship.update(secret_platform_group, secret_enemy_group, timer, secret_ship, secret_power_up_group, camera_entity)
            camera_entity.update(secret_ship)
            camera.update(secret_ship, camera_entity)
            secret_bullet_group.update(secret_platform_group, secret_enemy_group)
            secret_enemy_bullet_group.update(secret_platform_group, secret_ship)
            secret_enemy_group.update(secret_bullet_group, secret_ship, secret_enemy_group, secret_platform_group, secret_heal_group, camera)
            secret_power_up_group.update(secret_ship, secret_platform_group)
            secret_meteor_group.update(secret_ship)
            secret_heal_group.update(secret_ship, secret_platform_group)

            secret_daboss.life = str(secret_daboss.life)
            secret_boss_life = Text(font30,"Health: " + secret_daboss.life, screen.get_rect().centerx + 150, 70, RED)

            secret_ship.life = str(secret_ship.life)
            secret_health = Text(font30, "Life Remaining: " + secret_ship.life, screen.get_rect().centerx - 150, 100, GREEN)

            secret_score = str(secret_score)
            secret_score_text = Text(font30, "Time: " + secret_score, screen.get_rect().centerx - 200, 80, GREEN)

            # Bullet Boundary
            for b in secret_bullet_group:
                if camera.apply(b).centery < -20:
                    b.kill()
            # Instant Death
            if camera.apply(secret_ship).centerx < 47 or camera.apply(secret_ship).centerx > 465:
                secret_ship.life = 0
            if camera.apply(secret_ship).y < 0:
                secret_ship.life = 0

            screen.fill(BLACK)
            for p in secret_platform_group:
                screen.blit(p.image, camera.apply(p))
            for s in secret_ship_group:
                screen.blit(s.image, camera.apply(s))
            for b in secret_bullet_group:
                screen.blit(b.image, camera.apply(b))
            for e in secret_enemy_group:
                screen.blit(e.image, camera.apply(e))
            for t in secret_enemy_bullet_group:
                screen.blit(t.image, camera.apply(t))
            for p in secret_power_up_group:
                screen.blit(p.image, camera.apply(p))
            for m in secret_meteor_group:
                screen.blit(m.image, camera.apply(m))
            for h in secret_heal_group:
                screen.blit(h.image, camera.apply(h))
            screen.blit(secret_ship.image, camera.apply(secret_ship))
            screen.blit(secret_health.image, secret_health.rect)
            screen.blit(secret_score_text.image, secret_score_text.rect)
            screen.blit(secret_boss_life.image, secret_boss_life.rect)
            # limits frames per iteration of while loop
            timer += 1
            clock.tick(fps)
            # Writes to main surface
            pygame.display.flip()

            # change datatype back to integer
            secret_ship.life = int(secret_ship.life)
            secret_score = int(secret_score)
            secret_daboss.life = int(secret_daboss.life)

            if secret_ship.life <= 0:
                play3 = False
                outroin = True

            if secret_daboss.isAlive == False:
                win_screen = True
                play3 = False

        while outro:
            while outroin:
                screen.fill(BLACK)
                keyoutro = pygame.key.get_pressed()
                screen.blit(goodbye.image, goodbye.rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if keyoutro[pygame.K_BACKSPACE]:
                        sys.exit()
                clock.tick(fps)
                pygame.display.flip()
            while win_screen:
                screen.fill(WHITE)
                keyoutro = pygame.key.get_pressed()
                screen.blit(secret_win.image, secret_win.rect)
                screen.blit(secret_win1.image, secret_win1.rect)
                screen.blit(secret_win2.image, secret_win2.rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if keyoutro[pygame.K_BACKSPACE]:
                        sys.exit()
                clock.tick(fps)
                pygame.display.flip()


if __name__ == "__main__":
    main()