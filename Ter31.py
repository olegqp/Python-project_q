import pygame
from random import randint
from time import time as timer

FPS = 30
window = pygame.display.set_mode((640, 480))
# Bezhevuy
bz = (238, 232, 170)
background = (bz)
# Cvet knopki
buttext_col = (205, 133, 63)

s_button = True
pygame.font.init()
font = pygame.font.Font(None, 74)
start_text = font.render('Почати', True, buttext_col)
quit_text = font.render('Вийти', True, buttext_col)
play_rect = start_text.get_rect(center=(325, 150))
quit_rect = quit_text.get_rect(center=(325, 350))
while s_button:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s_button = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if play_rect.collidepoint(mouse_pos):
                print('Почати')
                s_button = False
            elif quit_rect.collidepoint(mouse_pos):
                print('Вийти')
                s_button = False
                pygame.quit()

    window.fill(bz)
    window.blit(start_text, play_rect)
    window.blit(quit_text, quit_rect)
    pygame.display.flip()

from random import randint

from pygame import *

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

img_back = "galaxy.jpg"
img_hero = "rocket.png"
img_hero1 = "rocket1.png"
img_hero2 = "rocket.png"

img_bullet = 'bullet.png'
img_enemy = 'ufo.png'

score = 0
lost = 0
max_lost = 3


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,
                 size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


bullets = sprite.Group()

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
ship1 = Player1(img_hero1, 5, win_height - 100, 80, 100, 10)
ship2 = Player2(img_hero2, 5, win_height - 200, 80, 200, 10)
finish = False
run = True


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_height - 80)
            self.rect.y = -50
            lost += 1


monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(50, win_width - 80), -60, 80, 50,
                    randint(1, 5))
    monsters.add(monster)
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
goal = 15

life = 3
max_fire = 5
max_fire1 = 5
max_fire2 = 5
rel_time = False
rel_time1 = False
rel_time2 = False
num_fire = 0
num_fire1 = 0
num_fire2 = 0
from time import time as timer

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < max_fire and rel_time == False:
                    num_fire = num_fire + 1
                    fire_sound.play()
                    ship.fire()

                if num_fire >= max_fire and rel_time == False:
                    last_time = timer()
                    rel_time = True

            if e.key == K_m:
                if num_fire1 < max_fire and rel_time1 == False:
                    num_fire1 = num_fire1 + 1
                    fire_sound.play()
                    ship1.fire()

                if num_fire1 >= max_fire and rel_time1 == False:
                    last_time = timer()
                    rel_time1 = True

            if e.key == K_g:
                if num_fire2 < max_fire and rel_time2 == False:
                    num_fire2 = num_fire2 + 1
                    fire_sound.play()
                    ship2.fire()

                if num_fire2 >= max_fire and rel_time2 == False:
                    last_time = timer()
                    rel_time2 = True

    if not finish:
        window.blit(background, (0, 0))
        ship.update()
        ship1.update()
        ship2.update()
        bullets.update()
        monsters.update()
        text = font2.render("Рахунок: " + str(score), True, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render("Пропущено: " + str(lost), True, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        ship.reset()
        ship1.reset()
        ship2.reset()
        bullets.draw(window)
        monsters.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                reload = font2.render('Wait, reload...', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0
                rel_time = False

        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0, 0)

        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))
        if sprite.spritecollide(ship, monsters, False):
            sprite.spritecollide(ship, monsters, True)
            life = life - 1
        if life == 0 or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
    else:
        time.delay(3000)
        score = 0
        lost = 0
        life = 3
        num_fire = 0
        finish = False
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        for i in range(1, 6):
            monster = Enemy(img_enemy, randint(
                50, win_width - 80), -60, 80, 50, randint(1, 5))
            monsters.add(monster)

    display.update()
    time.delay(50)