import pygame as pg
import sys, time, random

FPS = 60
TARGET_FPS = 60
WIN_WIDTH = 900
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)

pg.init()
running = True
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('hehhehhhehehehehehe')

side = 100
x = (WIN_WIDTH - side) // 2
y = (WIN_HEIGHT - side) // 2
photo = pg.image.load(r'c:/Users/ktnrg/OneDrive/Документы/Python/pygame/heh.jpg')
background_photo = pg.image.load(r"c:/Users/ktnrg/OneDrive/Документы/Python/pygame/bg.png")
background_photo = pg.transform.scale(background_photo, (WIN_WIDTH, WIN_HEIGHT))
photo = pg.transform.scale(photo, (side, side))
photo_left = photo

photo_right = pg.transform.flip(photo, True, False)
photo_down_l = pg.transform.rotate(photo, 90)
photo_up_l = pg.transform.rotate(photo, -90)
photo_up_r = pg.transform.flip(photo_up_l, True, False)
photo_down_r = pg.transform.flip(photo_down_l, True, False)

dt = 0
timer = 0
prev_time = time.time()
acceleration = 1
vel_x = 10
vel_y = const_vel_y = 25
jump = False
on_ground = False

jump_sound_1 = "c:/Users/ktnrg/OneDrive/Документы/Python/pygame/jump1.mp3"
jump_sound_2 = "c:/Users/ktnrg/OneDrive/Документы/Python/pygame/jump2.wav"
jump_sound_3 = "c:/Users/ktnrg/OneDrive/Документы/Python/pygame/jump3.wav"
jump_sound_list = [jump_sound_1, jump_sound_2, jump_sound_3]
while running:
    now = time.time()
    dt = now - prev_time
    prev_time = now
    screen.blit(background_photo, (0, 0))
    screen.blit(photo, (x, y))
    if vel_x < 0:
        photo = photo_left
    else:
        photo = photo_right
    pg.display.update()
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    if keys[pg.K_RIGHT] and x < WIN_WIDTH - side:
        photo = photo_right
        x += vel_x 
    if keys[pg.K_LEFT] and x > 0:
        photo = photo_left
        x -= vel_x 
    if keys[pg.K_UP] and jump == False and on_ground:
        on_ground = False
        jump = True
    if jump:
        y -= vel_y 
        vel_y -= acceleration
        if vel_y <= 0:
            jump = False
            
    if y < WIN_HEIGHT - side and jump is False:
        y += vel_y 
        vel_y += acceleration 
        if y > WIN_HEIGHT - side:
            y = WIN_HEIGHT - side
    if y == WIN_HEIGHT - side:
        pg.mixer.music.load(jump_sound_list[random.randint(0, 2)])
        pg.mixer.music.play()
        jump = True
        vel_y = const_vel_y
        on_ground = True
    x += vel_x
    if x == WIN_WIDTH - side or x == 0:
        vel_x = -vel_x
    
    clock.tick(FPS)