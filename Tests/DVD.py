import pygame as pg
import sys
FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)

pg.init()
sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()

pg.display.set_caption('HELP ME')
pg.display.update()
side = 100
x = (WIN_WIDTH - side) // 2
y = (WIN_HEIGHT - side) // 2
speedx = speedy = 10
photo = pg.image.load(r'c:/Users/ktnrg/OneDrive/Документы/Python/pygame/heh.jpg')
photo = pg.transform.scale(photo, (side, side))
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    sc.fill(BLACK)
    sc.blit(photo, (x,y))
    pg.display.update()
    if y < 0:
        speedy = -speedy
    if y > WIN_HEIGHT - side:
        speedy = -speedy
    if x > WIN_WIDTH - side:
        speedx = -speedx
    if x < 0:
        speedx = -speedx
    x += speedx
    y += speedy
    clock.tick(FPS)