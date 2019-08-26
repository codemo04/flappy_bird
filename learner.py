import pygame
### ADD ANY IMPORTS BELOW THIS LINE ###
import random

### STEP ONE: RENAME YOUR GAME ###
def name_your_game():

    name = "Floopy Bird"
    return(name)

### STEP TWO: LOAD A BACKGROUND IMAGE ###
def load_background_image():
    pass

### STEP THREE: MOVE THE SPRITE ###
def sprite_down(sprite_position):

    if sprite_position[1] != 460:
        sprite_position[1] += 20

    return sprite_position

def move_sprite(key, sprite_position):
    #print(sprite_position)

    if key == 'UP':
        #Checking to make sure the character doesn't go off screen
        if sprite_position[1] != 0:
            sprite_position[1] -= 50

    return sprite_position

### STEP FOUR: MAKE PIPES MOVE ACROSS THE SCREEN ###
def spawn_pipe(pipes):

    #size = (x,y)
    large = (100,400)
    small = (100,300)

    #Pick a random pipe image
    pipe = random.choice(pipes)
    #Pick a random pipe size
    size = random.choice([large, small])

    #If the pipe is upside down make it start on the bottom of the screen
    if pipe == "assets/images/pipe_upside_down.png":
        start_position = (600,0)
    else:
        start_position = (600,450)

    return [pipe, size, start_position]

def move_pipe(pipe_position, pipe_speed):

    pipe_position[0] -= pipe_speed
    return pipe_position

### STEP SIX: CHECK FOR COLLISIONS ###
def x_intersection(rect1_left, rect1_right, rect2_left, rect2_right):

    if rect1_left < rect2_right and rect1_right > rect2_left:
        return True
    else:
        return False

def y_interection(rect1_top, rect1_bottom, rect2_top, rect2_bottom):

    if rect1_top < rect2_bottom and rect1_bottom > rect2_top:
        return True
    else:
        return False

### ADD ON: KEEP SCORE ###
def update_score(pipe_list, score):

    for pipe in pipe_list:
        position = pipe.get_position()

        #Remove pipe from list if it went off screen
        if position[0] <= 0:
            pipe_list.remove(pipe)
            score += 1

    return score

### ADD ON: MAKE THE GAME GET FASTER ###
def change_level(score, pipe_speed):

    #Everytime score incremented by 5, make level faster
    if score % 5 == 0 and score != 0:
        pipe_speed += 5

    return pipe_speed

### ADD ON: ADD MUSIC TO YOUR GAME###
def get_audio():
    music_file = "Nitro Fun.mp3"
    return music_file
