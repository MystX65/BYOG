import pygame, random
from Bullets import *
BLACK = (0,0,0)

SHIP_WIDTH = 30
SHIP_HEIGHT = 50

# Enemy
class Straight_Double():
    def __init__(self, Enemy_Bullet, enemy, enemy_bullet_group):
        enemy_bullet = Enemy_Bullet(enemy, 0, 10)
        enemy_bullet.set_pos_enemy(enemy, 10)
        enemy_bullet_group.add(enemy_bullet)
        enemy_bullet = Enemy_Bullet(enemy, 0, 10)
        enemy_bullet.set_pos_enemy(enemy, 35)
        enemy_bullet_group.add(enemy_bullet)

class Shot_Gun():
    def __init__(self, Enemy_Bullet, moving_enemy, enemy_bullet_group):
        enemy_bullet = Enemy_Bullet(moving_enemy, -3, 7)
        enemy_bullet.set_pos_enemy(moving_enemy, 0)
        enemy_bullet_group.add(enemy_bullet)
        enemy_bullet = Enemy_Bullet(moving_enemy, 0, 7)
        enemy_bullet.set_pos_enemy(moving_enemy, 25)
        enemy_bullet_group.add(enemy_bullet)
        enemy_bullet = Enemy_Bullet(moving_enemy, 3, 7)
        enemy_bullet.set_pos_enemy(moving_enemy, 50)
        enemy_bullet_group.add(enemy_bullet)

class Missles():
    def __init__(self, Enemy_Target_Missles, sniper, enemy_bullet_group):
        enemy_bullet = Enemy_Target_Missles(sniper, 2, 4)
        enemy_bullet.set_pos_enemy(sniper, 10)
        enemy_bullet_group.add(enemy_bullet)
        enemy_bullet = Enemy_Target_Missles(sniper, 2, 4)
        enemy_bullet.set_pos_enemy(sniper, 35)
        enemy_bullet_group.add(enemy_bullet)

class Ultimate_Fire():
    def __init__(self, Enemy_Target_Missles, daboss, enemy_bullet_group, timer):
        timer1 = random.randrange(150, 200, 10)
        timer2 = random.randrange(40, 200, 10)
        timer3 = random.randrange(150, 300, 10)
        if timer % timer1 == 0:
            enemy_bullet = Enemy_Target_Missles(daboss, 2, 4)
            enemy_bullet.set_pos_enemy(daboss, 10)
            enemy_bullet_group.add(enemy_bullet)
            enemy_bullet = Enemy_Target_Missles(daboss, 2, 4)
            enemy_bullet.set_pos_enemy(daboss, 490)
            enemy_bullet_group.add(enemy_bullet)
        if timer % timer2 == 0:
            enemy_bullet = Enemy_Target_Missles(daboss, 3, 7)
            enemy_bullet.set_pos_enemy(daboss, 200)
            enemy_bullet_group.add(enemy_bullet)
            enemy_bullet = Enemy_Bullet(daboss, 0, 7)
            enemy_bullet.set_pos_enemy(daboss, 250)
            enemy_bullet_group.add(enemy_bullet)
            enemy_bullet = Enemy_Target_Missles(daboss, 3, 7)
            enemy_bullet.set_pos_enemy(daboss, 300)
            enemy_bullet_group.add(enemy_bullet)
        if timer % timer3 == 0:
            enemy_bullet = Enemy_Target_Missles(daboss, 1, 7)
            enemy_bullet.set_pos_enemy(daboss, 105)
            enemy_bullet_group.add(enemy_bullet)
            enemy_bullet = Enemy_Target_Missles(daboss, 1, 7)
            enemy_bullet.set_pos_enemy(daboss, 395)
            enemy_bullet_group.add(enemy_bullet)

class Ultimate_Fire2():
    def __init__(self, Enemy_Target_Missles, daboss, enemy_bullet_group, timer):
        timer1 = random.randrange(150, 200, 10)
        timer2 = random.randrange(40, 200, 10)
        timer3 = random.randrange(150, 300, 10)
        if timer % timer1 == 0:
            enemy_bullet = Enemy_Target_Missles(daboss, 2, 4)
            enemy_bullet.set_pos_enemy(daboss, 10)
            enemy_bullet_group.add(enemy_bullet)
            enemy_bullet = Enemy_Target_Missles(daboss, 2, 4)
            enemy_bullet.set_pos_enemy(daboss, 20)
            enemy_bullet_group.add(enemy_bullet)
        if timer % timer2 == 0:
            enemy_bullet = Enemy_Target_Missles(daboss, 3, 7)
            enemy_bullet.set_pos_enemy(daboss, 200)
            enemy_bullet_group.add(enemy_bullet)
            enemy_bullet = Enemy_Bullet(daboss, 0, 7)
            enemy_bullet.set_pos_enemy(daboss, 250)
            enemy_bullet_group.add(enemy_bullet)
            enemy_bullet = Enemy_Target_Missles(daboss, 3, 7)
            enemy_bullet.set_pos_enemy(daboss, 0)
            enemy_bullet_group.add(enemy_bullet)
        if timer % timer3 == 0:
            enemy_bullet = Enemy_Target_Missles(daboss, 1, 7)
            enemy_bullet.set_pos_enemy(daboss, 100)
            enemy_bullet_group.add(enemy_bullet)
            enemy_bullet = Enemy_Target_Missles(daboss, 1, 7)
            enemy_bullet.set_pos_enemy(daboss, 200)
            enemy_bullet_group.add(enemy_bullet)




#Ship
class ShootingTypes():
    def __init__(self, Bullet, ship, bullet_group):
        if ship.shooting_type == 1:
            bullet = Bullet(ship, 0, 10)
            bullet.set_pos(ship, SHIP_WIDTH - 8)
            bullet_group.add(bullet)
            bullet = Bullet(ship, 0, 10)
            bullet.set_pos(ship, 0)
            bullet_group.add(bullet)
        if ship.shooting_type == 3:
            bullet = Bullet(ship, 0, 10)
            bullet.set_pos(ship, SHIP_WIDTH/4-8)
            bullet_group.add(bullet)
            bullet = Bullet(ship, 0, 10)
            bullet.set_pos(ship, SHIP_WIDTH/2-8)
            bullet_group.add(bullet)
            bullet = Bullet(ship, 0, 10)
            bullet.set_pos(ship, SHIP_WIDTH*3/4-8)
            bullet_group.add(bullet)
            bullet = Bullet(ship, 0, 10)
            bullet.set_pos(ship, SHIP_WIDTH - 8)
            bullet_group.add(bullet)
        if ship.shooting_type == 2:
            bullet = Bullet(ship, 3, 7)
            bullet.set_pos(ship, 0)
            bullet_group.add(bullet)
            bullet = Bullet(ship, 0, 7)
            bullet.set_pos(ship, 25)
            bullet_group.add(bullet)
            bullet = Bullet(ship, -3, 7)
            bullet.set_pos(ship, 50)
            bullet_group.add(bullet)
        if ship.shooting_type == 4:
            bullet = Bullet(ship, 0, 10)
            bullet.set_pos(ship, 15)
            bullet_group.add(bullet)



