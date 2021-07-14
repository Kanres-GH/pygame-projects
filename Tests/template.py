import pygame as pg
import sys, time

FPS = 30
TARGET_FPS = 60
WIN_WIDTH = 600
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)

pg.init()
running = True
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('ЗДЕСЬ МОГЛА БЫ БЫТЬ ВАША РЕКЛАМА')

side = 100
x = (WIN_WIDTH - side) // 2
y = (WIN_HEIGHT - side) // 2
photo = pg.image.load(r'ПУТЬ К ФАЙЛУ')
background_photo = pg.image.load(r"ПУТЬ К ФАЙЛУ")
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

while running:
    now = time.time()
    dt = now - prev_time
    prev_time = now
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    pg.display.update()
    clock.tick(FPS)