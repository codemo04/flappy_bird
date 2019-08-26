import pygame
### ADD ANY IMPORTS BELOW THIS LINE ###
import random

def name_your_game():
    """There is no input to this function. You just need to return what
    you would like your game to be called as a string"""
    name = "Floopy Bird"

    return(name)

def move_sprite(key,sprite_position):
    """Key represents which key is pressed. It can be any of the following:
    'UP' - Up arrow key
    'DOWN' - Down arrow key

    Position is a list [x position, y position]. x position is the x
    location of the sprite and y position is the y position of the sprite

    You need to change the position of the sprite on screen depending on which
    key is pressed

    Need to return the modified position list. Remember python treats the top
    of the screen as point (0,0). BUG FIX: stop the bird from going off the screen
    """
    #print(sprite_position)
    if key == 'UP':
        if sprite_position[1] != 0:
            sprite_position[1] -= 50

    return sprite_position

def sprite_down(sprite_position):
    """ In the game flappy bird, the bird is constantly going down and we use
    the up arrow key to keep it afloat. In the function make the bird always
    go down, but be sure that it doesn't fall off the screen!"""

    if sprite_position[1] != 520:
        sprite_position[1] += 20

    return sprite_position

def move_pipe(pipe_position,pipe_speed):
    """Key represents which key is pressed. It can be any of the following:
    'UP' - Up arrow key
    'DOWN' - Down arrow key

    Position is a list [x position, y position]. x position is the x
    location of the sprite and y position is the y position of the sprite

    You need to change the position of the sprite on screen depending on which
    key is pressed

    Need to return the modified position list. Remember python treats the top
    of the screen as point (0,0). BUG FIX: stop the bird from going off the screen
    """
    pipe_position[0] -= pipe_speed
    return pipe_position

def spawn_pipe(pipes):
    """Pipes is a list of images of two pipes. One that is facing upwards and
    another that is facing downwards.

    Need to return a pipe name and a size for the pipe and its start position
    """
    large = (100,400)
    small = (100,300)
    pipe = random.choice(pipes)
    size = random.choice([large,small])

    if pipe == "pipe_upside_down.png":
        start = (600,0)
    else:
        start = (600,450)

    return [pipe,size,start]

def x_intersection(rect1_left, rect1_right, rect2_left, rect2_right):
    """ Check two rectangles occupy the same space in the x axis rect1 refers
    to the first rectangle and rect2 refers to the second rectangle. Left and
    right refers to the left and right corners of the rectangle

    Return true if they occupy the same space, else return false"""
    if rect1_left < rect2_right and rect1_right > rect2_left:
        return True
    else:
        return False

def y_interection(rect1_top, rect1_bottom, rect2_top, rect2_bottom):
    """ Check two rectangles occupy the same space in the y axis rect1 refers
    to the first rectangle and rect2 refers to the second rectangle. top and
    bottom refers to the top and bottom corners of the rectangle

    Return true if they occupy the same space, else return false"""

    if rect1_top < rect2_bottom and rect1_bottom > rect2_top:
        return True
    else:
        return False

def update_score(pipe_list,score):
    """ Check if any pipe in the list of pipe objects has gone off the screen.
    If any pipe has it means that the bird has successfully passed it! Increment
    the score by 1 and return it. Also remove that pipe object from the list"""

    for pipe in pipe_list:
        position = pipe.get_position()
        if position[0] <= 0:
            pipe_list.remove(pipe)
            score += 1

    return score

def change_level(score,pipe_speed):

    if score % 5 == 0 and score != 0:
        pipe_speed += 1

    return pipe_speed
