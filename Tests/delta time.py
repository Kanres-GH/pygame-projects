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
pg.font.init()
font = pg.font.SysFont('Comic Sans MS', 40)
canvas = pg.Surface((WIN_WIDTH, WIN_HEIGHT))
running = True
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('hehhehhhehehehehehe')
pg.display.update()

side = 100
#x = (WIN_WIDTH - side) // 2
x = 0
y = (WIN_HEIGHT - side) // 2
speedx = speedy = 5
photo = pg.image.load(r'c:/Users/ktnrg/OneDrive/Документы/Python/pygame/heh.jpg')
photo = pg.transform.scale(photo, (side, side))
photo = pg.transform.flip(photo, True, False)

dt = 0
timer = 0
prev_time = time.time()
passed, start = False, False
record = 0

while running:
    clock.tick(FPS)
    now = time.time()
    dt = now - prev_time
    prev_time = now
    if start:
        timer += dt
        x += speedx * dt * TARGET_FPS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                start = True
    if x > WIN_WIDTH and not passed:
        record = timer
        passed = True
    countdown = font.render("Time: " + str(round(timer, 5)), False, WHITE)
    fps_text = font.render("FPS: " + str(round(clock.get_fps(), 2)), False, WHITE)
    canvas.fill(ORANGE)
    canvas.blit(countdown, (0, 0))
    canvas.blit(fps_text, (0, 50))
    if record:
        record_text = font.render("Time: " + str(round(record, 5)), False, WHITE)
        canvas.blit(record_text, (WIN_WIDTH / 4, WIN_HEIGHT / 2))
    screen.blit(canvas, (0, 0))
    screen.blit(photo, (x, y))
    pg.display.update()