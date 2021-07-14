import pygame as pg
import sys, time, random

from pygame.math import Vector2
FPS = 60
TARGET_FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GAME_FIELD = (175, 215, 70)
BLUE = (128, 128, 255)
SNAKE_BLOCK = (255, 146, 2)

pg.init()
pg.font.init()
font = pg.font.Font('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/dpcomic.ttf', 30)

SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, 150)
running = True
cell_size = 30
cell_number = 20
update = True

class FOOD:
    def __init__(self):
        self.randomize()
    def draw_food(self):
        food_rect = pg.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pg.draw.rect(screen, RED, food_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pg.math.Vector2(self.x, self.y)

class SNAKE:
    photo = pg.image.load(r'c:/Users/ktnrg/OneDrive/Документы/Python/pygame/heh.jpg')
    photo = pg.transform.scale(photo, (cell_size, cell_size))

    photo_left = photo
    photo_right = pg.transform.flip(photo, True, False)
    photo_down_l = pg.transform.rotate(photo, 90)
    photo_up_l = pg.transform.rotate(photo, -90)
    photo_up_r = pg.transform.flip(photo_up_l, True, False)
    photo_down_r = pg.transform.flip(photo_down_l, True, False)

    def __init__(self):
        self.body = [pg.math.Vector2(5, 10), pg.math.Vector2(4, 10), pg.math.Vector2(3, 10)]
        self.direction = pg.math.Vector2(1, 0)
        self.new_block = False
    
    def update_head(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == pg.math.Vector2(1, 0):
            self.head = self.photo_left
        if head_relation == pg.math.Vector2(-1, 0):
            self.head = self.photo_right
        if head_relation == pg.math.Vector2(0, 1) and self.head == self.photo_left:
            self.head = self.photo_up_l
        if head_relation == pg.math.Vector2(0, 1) and self.head == self.photo_right:
            self.head = self.photo_up_r
        if head_relation == pg.math.Vector2(0, -1) and self.head == self.photo_left:
            self.head = self.photo_down_l
        if head_relation == pg.math.Vector2(0, -1) and self.head == self.photo_right:
            self.head = self.photo_down_r

    def draw_snake(self):
        self.update_head()
        for index, block in enumerate(self.body):
            block_rect = pg.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            else:
                pg.draw.rect(screen, SNAKE_BLOCK, block_rect)
    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
    
    def reset(self):
        self.body = [pg.math.Vector2(5, 10), pg.math.Vector2(4, 10), pg.math.Vector2(3, 10)]

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()
        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.randomize()
    
    def game_over(self):
        self.snake.reset()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            """self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()"""
            self.snake.direction = pg.math.Vector2(0, 0)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = font.render(score_text, True, BLACK)
        score_x = cell_size * cell_number - 40
        score_y = 40
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)

screen = pg.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pg.time.Clock()
pg.display.set_caption('Snake? Snake?! SNAAAAAKE!')

main_game = MAIN()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = pg.math.Vector2(0, -1)
            if event.key == pg.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = pg.math.Vector2(0, 1)
            if event.key == pg.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = pg.math.Vector2(-1, 0)
            if event.key == pg.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = pg.math.Vector2(1, 0)
    screen.fill(GAME_FIELD)
    main_game.draw_elements()
    pg.display.update()
    clock.tick(FPS)