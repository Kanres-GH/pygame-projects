import pygame as pg
import sys, time, random

FPS = 60
TARGET_FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)

pg.init()
pg.font.init()
font = pg.font.SysFont('Consolas', 40)

running = True
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('ЗДЕСЬ МОГЛА БЫ БЫТЬ ВАША РЕКЛАМА')

side = 50
photo = pg.image.load(r'c:/Users/ktnrg/OneDrive/Документы/Python/pygame/heh.jpg')
background_photo = pg.image.load(r"c:/Users/ktnrg/OneDrive/Документы/Python/pygame/crappy bird/inf_bg.png")
pipe = pg.image.load(r"c:/Users/ktnrg/OneDrive/Документы/Python/pygame/crappy bird/pipe.png")
pipe2 = pg.image.load(r"c:/Users/ktnrg/OneDrive/Документы/Python/pygame/crappy bird/pipe.png")
background_photo = pg.transform.scale(background_photo, (WIN_WIDTH, WIN_HEIGHT))
photo = pg.transform.scale(photo, (side, side))
pipe = pg.transform.scale(pipe, (pipe.get_width() // 2, pipe.get_height() // 2))
pipe2 = pg.transform.scale(pipe2, (pipe2.get_width() // 2, pipe2.get_height() // 2))
photo_left = photo
photo_right = pg.transform.flip(photo, True, False)
photo_down_l = pg.transform.rotate(photo, 90)
photo_up_l = pg.transform.rotate(photo, -90)
photo_up_r = pg.transform.flip(photo_up_l, True, False)
photo_down_r = pg.transform.flip(photo_down_l, True, False)

jump_sound = "c:/Users/ktnrg/OneDrive/Документы/Python/pygame/crappy bird/jump.wav"
die_sound = "c:/Users/ktnrg/OneDrive/Документы/Python/pygame/crappy bird/die.wav"
point_sound = "c:/Users/ktnrg/OneDrive/Документы/Python/pygame/crappy bird/point.wav"
pause_sound = "c:/Users/ktnrg/OneDrive/Документы/Python/pygame/crappy bird/pause.mp3"

pause_white = pg.Surface((WIN_WIDTH, WIN_HEIGHT), pg.SRCALPHA)
pause_white.fill((255, 255, 255, 128))

dt = 0
timer = 0
prev_time = time.time()

start, jump, dead, paused, play_die_sound, sound_played = False, False, False, False, False, False
x = WIN_WIDTH / 4
y = (WIN_HEIGHT - side) / 2
vel_y = const_vel_y = 10
acceleration = const_acceleration = .5
score = 0
high_score = 0

camera_x = 0
camera2_x = background_photo.get_width()
pipe_x = WIN_WIDTH
pipe_y = random.randint(WIN_HEIGHT - 250, 400)
up_pipe_y = pipe_y - 500
pipe2_x = pipe_x + 200
pipe2_y = random.randint(WIN_HEIGHT - 250, 400)
up_pipe2_y = pipe2_y - 500
pipe_speed = const_pipe_speed = 4
camera_speed = const_camera_speed = 1

pipe_rect = pg.Rect((pipe_x, pipe_y, 25, 250))
pipe2_rect = pg.Rect((pipe2_x, pipe2_y, 25, 250))
up_pipe_rect = pg.Rect((pipe_x, up_pipe_y, 25, 250))
up_pipe2_rect = pg.Rect((pipe2_x, up_pipe2_y, 25, 250))
photo_rect = pg.Rect((x, y, side, side))

press_space = font.render('Press SPACE to start', True, WHITE)
restart_screen_text = font.render('Press R or SPACE to restart', True, BLACK)
pause_text = font.render('Press ESC or P to continue', True, BLACK)

def inf_bg():
    global camera_x, camera2_x, const_camera_speed
    screen.blit(background_photo, (camera_x, 0))
    screen.blit(background_photo, (camera2_x, 0))
    camera_x -= camera_speed
    camera2_x -= camera_speed
    if camera_x < -background_photo.get_width():
        camera_x = background_photo.get_width()
    if camera2_x < -background_photo.get_width():
        camera2_x = background_photo.get_width()

def game_over():
    global pipe_speed, x, y, acceleration, vel_y, start
    pipe_speed = 0
    x -= 0
    y -= 0
    acceleration, vel_y = 0, 0
    screen.blit(pause_white, (0, 0))
    screen.blit(restart_screen_text, (100, WIN_HEIGHT / 2))

def pause_game():
    global paused
    while paused:
        screen.blit(pause_white, (0, 0))
        screen.blit(pause_text, (WIN_WIDTH / 4 - 100, WIN_HEIGHT / 2))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                    paused = False
        pg.display.update()
        clock.tick(FPS)
def collide():
    return photo_rect.colliderect(pipe_rect) or photo_rect.colliderect(up_pipe_rect) or photo_rect.colliderect(pipe2_rect) or photo_rect.colliderect(up_pipe2_rect) or y > WIN_HEIGHT - side

while running:
    score_text = font.render(f'Score: {score}', True, WHITE)
    highscore_text = font.render(f'Highscore: {high_score}', True, WHITE)
    inf_bg()
    if not start:
        sound_played = False
        score = 0
        pipe_speed = 0
        y = (WIN_HEIGHT - side) / 2
        pipe_x = WIN_WIDTH
        pipe_y = random.randint(WIN_HEIGHT - 250, 400)
        pipe2_y = random.randint(WIN_HEIGHT - 250, 400)
        pipe2_x = pipe_x + WIN_WIDTH / 2
        up_pipe_y = pipe_y - 500
        up_pipe2_y = pipe2_y - 500
        
        screen.blit(photo_right, (x, y))
        
        press_space_rect = pg.Surface((press_space.get_width(), press_space.get_height()), pg.SRCALPHA)
        press_space_rect.fill((0, 0, 0, 127))
        screen.blit(press_space_rect, (WIN_WIDTH / 4, WIN_HEIGHT * 3 / 4))
        screen.blit(press_space, (WIN_WIDTH / 4, WIN_HEIGHT * 3 / 4))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pg.mixer.Channel(1).play(pg.mixer.Sound(jump_sound))
                    jump = True
                    start = True
                    dead = False
                    pipe_speed = const_pipe_speed
                    acceleration = const_acceleration
                    vel_y = const_vel_y
        clock.tick(FPS)
    else:
        screen.blit(photo_right, (x, y))
        screen.blit(pipe, (pipe_x, pipe_y))
        screen.blit(pipe, (pipe_x, up_pipe_y))
        screen.blit(pipe2, (pipe2_x, pipe2_y))
        screen.blit(pipe2, (pipe2_x, up_pipe2_y))
        score_rect = pg.Surface((score_text.get_width(), score_text.get_height()), pg.SRCALPHA)
        score_rect.fill((0, 0, 0, 127))
        screen.blit(score_rect, (WIN_WIDTH - score_text.get_width(), 0))
        screen.blit(score_text, (WIN_WIDTH - score_text.get_width(), 0))
        highscore_rect = pg.Surface((highscore_text.get_width(), highscore_text.get_height()), pg.SRCALPHA)
        highscore_rect.fill((0, 0, 0, 127))
        screen.blit(highscore_rect, (WIN_WIDTH - highscore_text.get_width(), score_text.get_height()))
        screen.blit(highscore_text, (WIN_WIDTH - highscore_text.get_width(), score_text.get_height()))

        photo_rect.y = y
        pipe_rect.x = up_pipe_rect.x = pipe_x
        pipe_rect.y = pipe_y
        up_pipe_rect.y = up_pipe_y
        pipe2_rect.x = up_pipe2_rect.x = pipe2_x
        pipe2_rect.y = pipe2_y
        up_pipe2_rect.y = up_pipe2_y
        
        pipe_x -= pipe_speed
        pipe2_x -= pipe_speed
        
        if pipe_x < -25:
            pipe_x = WIN_WIDTH
            pipe_y = random.randint(WIN_HEIGHT - 250, 400)
            up_pipe_y = pipe_y - 400
        if pipe2_x < -25:
            pipe2_x = pipe_x + WIN_WIDTH / 2
            pipe2_y = random.randint(WIN_HEIGHT - 250, 400)
            up_pipe2_y = pipe2_y - 400
        if x == pipe_x or x == pipe2_x:
            pg.mixer.Channel(0).play(pg.mixer.Sound(point_sound))
            score += 1
            if score > high_score:
                high_score = score

        now = time.time()
        dt = now - prev_time
        prev_time = now

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not dead:
                    pg.mixer.Channel(1).play(pg.mixer.Sound(jump_sound))
                    start = True
                    jump = True
                    vel_y = const_vel_y
                    
                if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                    pg.mixer.Channel(2).play(pg.mixer.Sound(pause_sound))
                    paused = True
                if dead and (event.key == pg.K_r or event.key == pg.K_SPACE):
                    start = False
        if paused:
            pause_game()
        if jump:
            y -= vel_y
            vel_y -= acceleration
            if vel_y <= 0:
                jump = False
        if y < WIN_HEIGHT - side and jump is False:
            y += vel_y
            vel_y += acceleration 
            
        if y < 0:
            y = 0
            jump = False
            vel_y = 1
        if play_die_sound:
            pg.mixer.Channel(3).play(pg.mixer.Sound(die_sound))
            sound_played = True
        if collide():
            play_die_sound = True
            if sound_played:
                play_die_sound = False
            game_over()
            dead = True
        pg.display.update()
        clock.tick(FPS)