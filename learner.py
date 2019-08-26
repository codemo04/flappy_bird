import pygame
### ADD ANY IMPORTS BELOW THIS LINE ###
import random

### STEP ONE: RENAME YOUR GAME ###
def name_your_game() -> str:

    name = "Floopy Bird"
    return(name)

### STEP TWO: LOAD A BACKGROUND IMAGE ###
def get_background() -> str:
    file_name = "assets/images/background.png"
    return file_name

def get_character() -> str:
    file_name = "assets/images/bird.png"
    return file_name

### STEP THREE: MOVE THE SPRITE ###
def sprite_down(sprite_position: list) -> list:

    if sprite_position[1] != 460:
        sprite_position[1] += 20

    return sprite_position

def move_sprite(key: str, sprite_position: list) -> list:

    if key == 'UP':
        #Checking to make sure the character doesn't go off screen
        if sprite_position[1] != 0:
            sprite_position[1] -= 50

    return sprite_position

### STEP FOUR: MAKE PIPES MOVE ACROSS THE SCREEN ###
def spawn_pipe(pipes: list) -> list:

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

def move_pipe(pipe_position: list, pipe_speed: float) -> list:

    pipe_position[0] -= pipe_speed
    return pipe_position

### STEP SIX: CHECK FOR COLLISIONS ###
def x_intersection(rect1_left: float, rect1_right: float, rect2_left: float,
    rect2_right: float) -> bool:

    if rect1_left < rect2_right and rect1_right > rect2_left:
        return True
    else:
        return False

def y_interection(rect1_top: float, rect1_bottom: float, rect2_top: float,
    rect2_bottom: float) -> bool:

    if rect1_top < rect2_bottom and rect1_bottom > rect2_top:
        return True
    else:
        return False

### ADD ON: KEEP SCORE ###
def update_score(pipe_list: list, score: int) -> int:

    for pipe in pipe_list:
        position = pipe.get_position()

        #Remove pipe from list if it went off screen
        if position[0] <= 0:
            pipe_list.remove(pipe)
            score += 1

    return score

### ADD ON: MAKE THE GAME GET FASTER ###
def change_level(score: int, pipe_speed: float) -> float:

    #Everytime score incremented by 5, make level faster
    if score % 5 == 0 and score != 0:
        pipe_speed += 5

    return pipe_speed

### ADD ON: ADD MUSIC TO YOUR GAME###
def get_game_audio() -> str:
    music_file = "assets/sounds/Nitro Fun.mp3"
    return music_file

def get_gameover_audio() -> str:
    music_file = "assets/sounds/game over.mp3"
    return music_file
