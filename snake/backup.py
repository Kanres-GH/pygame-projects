import pygame as pg
import sys, random, json
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

data = {}

with open('config.txt') as config_file:
    data = json.load(config_file)

pg.mixer.pre_init(44100, -16, 2, 512)
pg.init()
pg.font.init()

cell_size = 40
cell_number = 15
gamefield_size = cell_size * cell_number

snek = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/snek.png')
snek = pg.transform.scale(snek, (200, 200))

font = pg.font.Font('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/dpcomic.ttf', 30)
title_font = pg.font.Font('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Gant.ttf', 50)
little_font = pg.font.Font('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Gant.ttf', 30)

menu_title_surface = title_font.render('змейка или типа того', True, BLACK)
menu_title_rect = menu_title_surface.get_rect(center = (gamefield_size / 2, 50))
menu_start_surface = title_font.render('начать', True, BLACK)
menu_start_rect = menu_start_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 2))
menu_new_game_surface = title_font.render('новая игра', True, BLACK)
menu_new_game_rect = menu_new_game_surface.get_rect(center = (gamefield_size / 2 + 50, gamefield_size / 2))
menu_continue_surface = title_font.render('продолжить', True, BLACK)
menu_continue_rect = menu_continue_surface.get_rect(center = (gamefield_size / 2 - 50, gamefield_size / 2))
menu_options_surface = title_font.render('настройки', True, BLACK)
menu_options_rect = menu_options_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 2 + 100))
menu_exit_surface = title_font.render('выйти', True, BLACK)
menu_exit_rect = menu_exit_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 2 + 200))

menu_options_music_on_surface = title_font.render('музыка: вкл', True, BLACK)
menu_options_music_on_rect = menu_options_music_on_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 2 - 50))
menu_options_borders_off_surface = title_font.render('границы карты: выкл', True, BLACK)
menu_options_borders_off_rect = menu_options_borders_off_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 2 + 50))
menu_options_music_off_surface = title_font.render('музыка: выкл', True, BLACK)
menu_options_music_off_rect = menu_options_music_off_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 2 - 50))
menu_options_borders_on_surface = title_font.render('границы карты: вкл', True, BLACK)
menu_options_borders_on_rect = menu_options_borders_on_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 2 + 50))
menu_options_back_surface = title_font.render('назад', True, BLACK)
menu_options_back_rect = menu_options_back_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 2 - 150))

game_over_surface = title_font.render('вы проиграли', True, WHITE)
game_over_rect = game_over_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 2 - 200))
game_over_black = pg.Surface((cell_number * cell_size, cell_number * cell_size), pg.SRCALPHA)
game_over_black.fill((0, 0, 0, 128))
game_over_surface_restart = little_font.render('нажмите SPACE или R для рестарта', True, WHITE)
game_over_rect_restart = game_over_surface_restart.get_rect(center = (gamefield_size / 2, gamefield_size / 2 + 150))
game_over_surface_escape = little_font.render('нажмите ESC чтобы перейти в главное меню', True, WHITE)
game_over_rect_escape = game_over_surface_escape.get_rect(center = (gamefield_size / 2, gamefield_size / 2 + 200))

pause_surface = title_font.render('пауза', True, WHITE)
pause_rect = pause_surface.get_rect(center = (gamefield_size / 2, gamefield_size / 4))
pause_surface_continue = little_font.render('Нажмите ESC или P чтобы продолжить', True, WHITE)
pause_rect_continue = pause_surface_continue.get_rect(center = (gamefield_size / 2, gamefield_size / 2))
pause_surface_menu = little_font.render('Нажмите M чтобы вернуться в главное меню', True, WHITE)
pause_rect_menu = pause_surface_menu.get_rect(center = (gamefield_size / 2, gamefield_size / 2 + 100))
pause_sound = pg.mixer.Sound('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/pause.mp3')
pause_sound.set_volume(0.3)

SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, 150)
running = True
update = True
died = False
paused = False
click = False
enable_borders = False
mute_music = False
start_game = False

class FOOD:
    def __init__(self):
        self.randomize()
    def draw_food(self):
        food_rect = pg.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple, food_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        head = pg.image.load(r'c:/Users/ktnrg/OneDrive/Документы/Python/pygame/heh.jpg').convert_alpha()
        head = pg.transform.scale(head, (cell_size, cell_size))

        self.head_left = head
        self.head_right = pg.transform.flip(head, True, False)
        self.head_down_l = pg.transform.rotate(head, 90)
        self.head_up_l = pg.transform.rotate(head, -90)
        self.head_up_r = pg.transform.flip(self.head_up_l, True, False)
        self.head_down_r = pg.transform.flip(self.head_down_l, True, False)

        self.tail_up = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/tail_down.png').convert_alpha()
        self.tail_left = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/tail_left.png').convert_alpha()
        self.tail_right = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/tail_right.png').convert_alpha()

        self.body_vertical = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/body_tl.png').convert_alpha()
        self.body_br = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/body_br.png').convert_alpha()
        self.body_bl = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/body_bl.png').convert_alpha()

        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.crunch_sound = pg.mixer.Sound('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/crunch.wav')
        self.crunch_sound.set_volume(0.2)
    
    def update_head(self):
        for block in self.body:
            if block.x > cell_number - 1:
                block.x = 0
            if block.y > cell_number - 1:
                block.y = 0
            if block.x < 0:
                block.x = cell_number - 1
            if block.y < 0:
                block.y = cell_number - 1
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        if head_relation == Vector2(-1, 0):
            self.head = self.head_right
        if head_relation == Vector2(0, 1) and self.head == self.head_left:
            self.head = self.head_up_l
        if head_relation == Vector2(0, 1) and self.head == self.head_right:
            self.head = self.head_up_r
        if head_relation == Vector2(0, -1) and self.head == self.head_left:
            self.head = self.head_down_l
        if head_relation == Vector2(0, -1) and self.head == self.head_right:
            self.head = self.head_down_r
    def update_tail(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        if tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        if tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        if tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def draw_snake(self):
        self.update_head()
        self.update_tail()
        
        for index, block in enumerate(self.body):
            block_rect = pg.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                prev_block = self.body[index + 1] - block   
                next_block = self.body[index - 1] - block
                if prev_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if (prev_block.x == -1 and next_block.y == -1) or (prev_block.y == -1 and next_block.x == -1):
                        screen.blit(self.body_tl, block_rect)
                    elif (prev_block.x == -1 and next_block.y == 1) or (prev_block.y == 1 and next_block.x == -1):
                        screen.blit(self.body_bl, block_rect)
                    elif (prev_block.x == 1 and next_block.y == -1) or (prev_block.y == -1 and next_block.x == 1):
                        screen.blit(self.body_tr, block_rect)
                    elif (prev_block.x == 1 and next_block.y == 1) or (prev_block.y == 1 and next_block.x == 1):
                        screen.blit(self.body_br, block_rect)

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
        global died
        died = False
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = pg.Vector2(1, 0)

    def play_crunch_sound(self):
        self.crunch_sound.play()

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def show_options(self):
        global click, mute_music, enable_borders
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            screen.fill(GAME_FIELD)
            mouse_x, mouse_y = pg.mouse.get_pos()
            #music_button_off = menu_options_music_off_rect
            #music_button_on = menu_options_music_on_rect
            back_button = menu_options_back_rect
            if mute_music:
                music_button = menu_options_music_off_rect
            else:
                music_button = menu_options_music_on_rect
            
            if enable_borders:
                borders_button = menu_options_borders_on_rect
            else:
                borders_button = menu_options_borders_off_rect

            if music_button.collidepoint((mouse_x, mouse_y)) and music_button == menu_options_music_on_rect:
                if click:
                    mute_music = True
            if music_button.collidepoint((mouse_x, mouse_y)) and music_button == menu_options_music_off_rect:
                if click:
                    mute_music = False

            if borders_button.collidepoint((mouse_x, mouse_y)) and borders_button == menu_options_borders_on_rect:
                if click:
                    enable_borders = False
            if borders_button.collidepoint((mouse_x, mouse_y)) and borders_button == menu_options_borders_off_rect:
                if click:
                    enable_borders = True
            
            if back_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    #print(2)
                    #self.show_menu()
                    break

            if mute_music:
                pg.mixer.music.set_volume(0)
                screen.blit(menu_options_music_off_surface, menu_options_music_off_rect)
            else:
                pg.mixer.music.set_volume(0.2)
                screen.blit(menu_options_music_on_surface, menu_options_music_on_rect)

            if enable_borders:
                screen.blit(menu_options_borders_on_surface, menu_options_borders_on_rect)
            else:
                screen.blit(menu_options_borders_off_surface, menu_options_borders_off_rect)

            screen.blit(menu_options_back_surface, menu_options_back_rect)

            click = False

            pg.display.update()
            clock.tick(FPS)

    def show_levels(self):
        pass

    def show_menu(self):
        global start_game
        while True:
            screen.fill(GAME_FIELD)
            global menu_title_surface, menu_title_rect, menu_start_surface, menu_start_rect, click
            mouse_x, mouse_y = pg.mouse.get_pos()
            start_button = menu_start_rect
            exit_button = menu_exit_rect
            new_game_button = menu_new_game_rect
            continue_button = menu_continue_rect
            options_button = menu_options_rect
            if start_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    start_game = True
            if exit_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    pg.quit()
                    sys.exit()
            if continue_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    pass
            if new_game_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    pass
            if options_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    self.show_options()
            click = False

            #pg.draw.rect(screen, (103, 136, 20), start_button)
            #pg.draw.rect(screen, (103, 136, 20), options_button)
            #pg.draw.rect(screen, (103, 136, 20), exit_button)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            if start_game:
                break
            else:
                screen.blit(snek, (200, 50))
                screen.blit(menu_title_surface, menu_title_rect)
                screen.blit(menu_start_surface, menu_start_rect)
                screen.blit(menu_options_surface, menu_options_rect)
                screen.blit(menu_exit_surface, menu_exit_rect)

            pg.display.update()
            clock.tick(FPS)
    
    def new_game(self):
        pass

    def pause_game(self):
        global paused, start_game
        pg.mixer.music.pause()
        screen.blit(game_over_black, (0, 0))
        screen.blit(pause_surface, pause_rect)
        screen.blit(pause_surface_continue, pause_rect_continue)
        screen.blit(pause_surface_menu, pause_rect_menu)
        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    with open("config.txt", "w") as config_file:
                        json.dump(data, config_file)
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE or event.key == pg.K_p:
                        pg.mixer.music.unpause()
                        paused = False
                    if event.key == pg.K_m:
                        paused = False
                        start_game = False
                        pg.mixer.music.unpause()
                        self.show_menu()
                        
            pg.display.update()
            clock.tick(FPS)

    def draw_grid(self):
        grid_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2:        
                for column in range(cell_number):
                    if column % 2:
                        grid_rect = pg.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pg.draw.rect(screen, grid_color, grid_rect)
            else:
                for column in range(cell_number):
                    if column % 2 == 0:
                        grid_rect = pg.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pg.draw.rect(screen, grid_color, grid_rect)

    def draw_elements(self):
        self.draw_grid()
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.randomize()
    
    def game_over(self):
        global died, start_game
        screen.blit(game_over_black, (0, 0))
        screen.blit(game_over_surface, game_over_rect)
        self.draw_final_score()
        screen.blit(game_over_surface_restart, game_over_rect_restart)
        screen.blit(game_over_surface_escape, game_over_rect_escape)
        while died:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    with open("config.txt", "w") as config_file:
                        json.dump(data, config_file)
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE or event.key == pg.K_r:
                        self.snake.reset()
                    if event.key == pg.K_ESCAPE:
                        with open("config.txt", "w") as config_file:
                            json.dump(data, config_file)
                        start_game = False
                        died = False
                        self.show_menu()
            pg.display.update()
            clock.tick(FPS)
                    
    def check_fail(self):
        global died, enable_borders
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                died = True
        if enable_borders:
            if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                died = True

    def draw_score(self):
        score = len(self.snake.body) - 3
        global highscore, data
        if score > data['highscore']:
            highscore = score
            data['highscore'] = highscore
        self.score_text = str(score)
        self.highscore_text = str(data['highscore'])
        score_surface = font.render(self.score_text, True, BLACK)
        highscore_surface = font.render(self.highscore_text, True, BLACK)
        score_x = gamefield_size - 40
        score_y = 40
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        highscore_x = gamefield_size - 40
        highscore_y = 100
        highscore_rect = highscore_surface.get_rect(center = (highscore_x, highscore_y))
        screen.blit(score_surface, score_rect)
        screen.blit(highscore_surface, highscore_rect)

    def draw_final_score(self):
        game_over_surface_score = title_font.render(f'ваш счёт: {self.score_text}', True, WHITE)
        game_over_rect_score = game_over_surface_score.get_rect(center = (gamefield_size / 2, gamefield_size / 2 - 50))
        game_over_surface_highscore = title_font.render(f'лучший рекорд: {self.highscore_text}', True, WHITE)
        game_over_rect_highscore = game_over_surface_highscore.get_rect(center = (gamefield_size / 2, gamefield_size / 2 + 50))
        screen.blit(game_over_surface_score, game_over_rect_score)
        screen.blit(game_over_surface_highscore, game_over_rect_highscore)
        

screen = pg.display.set_mode((gamefield_size, gamefield_size))
clock = pg.time.Clock()
pg.display.set_caption('Snakey-Snakey')

apple = pg.image.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/Graphics/apple.png').convert_alpha()
highscore = 0
main_game = MAIN()
music = pg.mixer.music.load('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/snake/music.mp3')
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(-1)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            with open("config.txt", "w") as config_file:
                json.dump(data, config_file)
            pg.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pg.KEYDOWN:
            if (event.key == pg.K_UP or event.key == pg.K_w) and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if (event.key == pg.K_DOWN or event.key == pg.K_s) and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if (event.key == pg.K_LEFT or event.key == pg.K_a) and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
            if (event.key == pg.K_RIGHT or event.key == pg.K_d) and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                pause_sound.play()
                paused = True
    screen.fill(GAME_FIELD)
    if start_game:
        main_game.draw_elements()
    else:
        main_game.show_menu()
    if paused:
        main_game.pause_game()
    if died:
        main_game.game_over()
    #screen.fill(GAME_FIELD)
    #main_game.draw_elements()
    
    pg.display.update()
    clock.tick(FPS)