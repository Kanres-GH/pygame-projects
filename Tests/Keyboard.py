import pygame as pg
import sys
FPS = 50
WIN_WIDTH = 800
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)
pg.init()

screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('HELP ME')
pg.display.update()
image_file = 'c:/Users/ktnrg/OneDrive/Документы/Python/pygame/heh.jpg'
space_image = 'c:/Users/ktnrg/OneDrive/Документы/Python/pygame/402868.jpg'
photo = pg.image.load(image_file)
space_photo = pg.image.load(space_image)

side = 100
space_photo = pg.transform.scale(space_photo, (WIN_WIDTH, WIN_HEIGHT))
photo = pg.transform.scale(photo, (side, side))
photo_left = photo

photo_right = pg.transform.flip(photo, True, False)
photo_down_l = pg.transform.rotate(photo, 90)
photo_up_l = pg.transform.rotate(photo, -90)
photo_up_r = pg.transform.flip(photo_up_l, True, False)
photo_down_r = pg.transform.flip(photo_down_l, True, False)

gravity = 1
x = (WIN_WIDTH - side) // 2
y = (WIN_HEIGHT - side) // 2

speedx = 10
speedy = 10
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    screen.blit(space_photo, (0, 0))
    screen.blit(photo, (x,y))
    pg.display.update()
    keys = pg.key.get_pressed()
    # ---- Выход за экран ---- #
    if x < 0:
        x += speedx
    if x > WIN_WIDTH - side:
        x -= speedx
    if y < 0:
        y += speedy
    if y > WIN_HEIGHT - side:
        y -= speedy
    # ---- Клавишы ---- #
    if keys[pg.K_RIGHT]:
        photo = photo_right
        x += speedx
    if keys[pg.K_LEFT]:
        photo = photo_left
        x -= speedx
    if keys[pg.K_UP]:
        if photo == photo_left:
            photo = photo_up_l
        if photo == photo_right:
            photo = photo_up_r
        if photo == photo_down_l:
            photo = photo_up_l
        if photo == photo_down_r:
            photo = photo_up_r
        y -= speedy
    if keys[pg.K_DOWN]:
        if photo == photo_left:
            photo = photo_down_l
        if photo == photo_right:
            photo = photo_down_r
        if photo == photo_up_l:
            photo = photo_down_l
        if photo == photo_up_r:
            photo = photo_down_r
        y += speedy
    clock.tick(FPS)