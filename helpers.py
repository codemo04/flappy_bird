import pygame
from sprites import *
from move import *

def load_background(image_file):
    image = pygame.image.load(image_file)
    return image

def is_active(event):
    if event.type == pygame.QUIT:
        return False
    else:
        return True

def keys(character,event):
    key_pressed = False

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_UP:
            character.update_pos('UP')
            key_pressed = True

        elif event.key == pygame.K_DOWN:
            character.update_pos('DOWN')
            key_pressed = True

def render_pipes(speed,timer,image_list, group):

    if timer > speed * 1000:
        characteristics = spawn_pipe(image_list)
        pipe = Enemy(characteristics[0],characteristics[1], characteristics[2])
        group.add(pipe)
        return pipe

def text_to_screen(screen, text, position, color=(0,0,0)):
    size = 50

    pygame.font.init()
    text = str(text)
    font = pygame.font.SysFont('Arial', size)
    text = font.render(text, True, color)
    screen.blit(text, (position[0], position[1]))

def update_timer(timer, speed):
    if timer > speed * 1000:
        return 0
    else:
        return timer

def detect_collision(pipe_list, character):
    first_pipe = pipe_list[0]
    (left_p, top_p, width_p, height_p) = first_pipe.get_rect()
    (left_c, top_c, width_c, height_c) = character.get_rect()

    width_p += left_p
    width_c += left_c
    height_p += top_p
    height_c += top_c

    x_intersect = x_intersection(left_p, width_p, left_c, width_c)
    y_interect = y_interection(top_p, height_p, top_c, height_c)

    if x_intersect and y_interect:
        return True
    else:
        return False

def change_score(pipe_list,score,speed,pipe_speed):
    updated_score = update_score(pipe_list,score)
    if updated_score > score:
        change_level(score,pipe_speed)

    return (updated_score,pipe_speed)
