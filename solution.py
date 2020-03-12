import pygame
import random
from GUI import *

# STEP ONE: RENAME YOUR GAME
def set_name() -> str:
    """ Return a string containing the name for your game """

    # Delete the 'pass' above. Write your code below this line
    name = "Floopy Bird"
    return(name)


# STEP TWO: LOAD A BACKGROUND IMAGE
def get_background() -> str:
    """ Return a string containing the path to your background image.

    Remember computers need to know where every file is, not just its name. More
    specifically, the computer needs the path to that image!

    For your image to fit correctly with this game, make sure it's 700 x 700
    pixels in size """

    # Delete the 'pass' above. Write your code below this line

    file_name = "assets/images/background.png"
    return file_name


# STEP THREE: LOAD A BACKGROUND IMAGE
def get_gameover_background() -> str:
    """ Return a string containing the path to your "game over" background image.

    Remember computers need to know where every file is, not just its name. More
    specifically, the computer needs the path to that image!

    For your image to fit correctly with this game, make sure it's 700 x 700
    pixels in size """

    # Delete the 'pass' above. Write your code below this line

    file_name = "assets/images/game-over.jpg"
    return file_name


# STEP FOUR: LOAD A CHARACTER IMAGE
def get_character() -> str:
    """ Return a string containing the path to your character image.

    Remember computers need to know where every file is, not just its name. More
    specifically, the computer needs the path to that image!

    For your image to fit correctly with this game, make sure it's 255 x 255
    pixels in size """

    # Delete the 'pass' above. Write your code below this line

    file_name = "assets/images/bird.png"
    return file_name


# STEP FIVE: MOVE THE SPRITE DOWN
def sprite_down(sprite_position: list) -> list:
    """ Return a list of new x and y coordinates for the character sprite. In
    flappy bird, the bird is always moving down and it's up to the player to
    move it upwards. Let's focus on making the bird travel downward.

    In game design, we make a sprite move by specifying a new location for it to
    travel to. Be careful to not have the sprite go off the screen.

    REMINDER: In Python, the top left corner of the screen is the point (0,0).
    The bottom right corner of the screen is (600,600)

    HINT: If we need the sprite to move down, do we need to do anything with
    the x coordinate? """

    # Delete the 'pass' above. Write your code below this line

    fall_amount = 10
    # #Delete the 'pass' above. Write your code below this line

    if sprite_position[1] >= 600:
        sprite[1] = 600
    else:
        sprite_position[1] = sprite_position[1] + fall_amount

    return sprite_position


# STEP SIX: MOVE THE SPRITE UP
def move_sprite(key: str, sprite_position: list) -> list:
    """ Return a list of new x and y coordinates for the character sprite based
    on which key is pressed. Let's focus on making the bird travel up if the up
    arrow key is pressed. If the player is pressing the up arrow key, the
    parameter key will be 'UP'.

    In game design, we make a sprite move by specifying a new location for it to
    travel to. Be careful to not have the sprite go off the screen.

    REMINDER: In Python, the top left corner of the screen is the point (0,0)
    and the bottom right corner is (600,600)

    HINT: If we need the sprite to move up, do we need to do anything with
    the x coordinate? """

    # Delete the 'pass' above. Write your code below this line

    jump_amount = 60

    if key == 'UP' and sprite_position[1] >= 0:
        sprite_position[1] -= jump_amount

    return sprite_position


# STEP SEVEN: SPAWN A PIPE
def spawn_pipe(pipes: list) -> list:
    """ Time to add some pipes to this game! `pipes` is a list of file paths for
    two pipe images. The list looks like this:

    ["assets/images/pipe_upside_down.png", "assets/images/pipe.png"]

    We want to randomly select one of these 2 pipes to spawn. Furthermore, we
    want to specify the size of each pipe (width, height). Given below are two
    different sizes. `large` is a long configuration of a pipe and `small` is a
    short configuration of the pipe. We want to randomly select the size as
    well.

    Lastly, we need to specify the location for each pipe to spawn. We want the
    pipe to spawn on the right corner of the screen. The right-side-up pipes
    will want to start on the bottom of the screen and the upside-down pipe will
    want to start on the top of the screen.

    Return a list containing the pipe name, a list of the pipe's size
    [width,height], and a list containing the pipe's spawn position [x,y].
    """

    # Delete the 'pass' above. Write your code below this line

    # size = [x,y]
    large = [100, 400]
    small = [100, 300]
    possible_sizes = [large, small]

    # Pick a random pipe image
    pipe = random.choice(pipes)
    # Pick a random pipe size
    size = random.choice(possible_sizes)

    # If the pipe is upside down make it start on the bottom of the screen
    if pipe == "assets/images/pipe_upside_down.png":
        start_position = [600, 0]
    else:
        start_position = [600, 450]

    return [pipe, size, start_position]


# STEP EIGHT: MOVE THE PIPES
def move_pipe(pipe_position: list, pipe_speed: float) -> list:
    """In a video game such as this one, it's common to think the character is
    moving forward. However it is the background that moves!

    By making the pipes move from right to left across the screen, it creates the
    illusion that it is the character which is moving.

    Similar to making the character move up and down, update the pipe's
    position using its speed. Return a list of pipe_position [x,y].

    REMINDER: In Python, the top left corner of the screen is the point (0,0)
    HINT: If we need the pipes to move left to right, do we need to do
    anything with the y coordinate?"""

    # Delete the 'pass' above. Write your code below this line

    pipe_position[0] -= pipe_speed
    return pipe_position


# STEP NINE: DETECT COLLISIONS
def x_intersection(rect1_left: float, rect1_right: float, rect2_left: float,
    rect2_right: float) -> bool:
    """ In Scratch, we checked if two objects were touching based on colour. In
    Python, however, things are a little bit different. In game design, we
    determine whether two objects are touching based on if they are occupying
    the same space at the same time.

    In this function, we want to check if two rectangles are occupying the same
    'x space'. Each parameter given represents an x coordinate on a rectangle.

    Return True if rect1 and rect2 are occupying the same x space, and False
    otherwise!

    HINT: Draw two rectangles touching. This may help you write the logic for
    it!
    """

    # Delete the 'pass' above. Write your code below this line

    if rect1_left < rect2_right and rect1_right > rect2_left:
        return True
    else:
        return False

def y_interection(rect1_top: float, rect1_bottom: float, rect2_top: float,
    rect2_bottom: float) -> bool:
    """ In this function, we want to check if two rectangles are occupying the
    same 'y space'. Each parameter given represents a y coordinate on a
    rectangle.

    Return True if rect1 and rect2 are occupying the same y space, and False
    otherwise!

    HINT: Draw two rectangles touching. This may help you write the logic for
    it!
    """

    # Delete the 'pass' above. Write your code below this line

    if rect1_top < rect2_bottom and rect1_bottom > rect2_top:
        return True
    else:
        return False


# ADD ON: KEEPING SCORE
def update_score(pipe_list: list, score: int) -> int:
    """Let's add a scoreboard to our flappy bird game! We need to return an
    updated score based on how many pipes our character has passed.

    pipe_list is a list of pipe objects. We need to iterate through them all
    using a loop and see if any of their x coordinates are negative. If they
    are negative that means the pipe has gone off the screen.

    For each pipe in `pipe_list`, use pipe.get_position() to get an [x,y] list
    for the location of that particular pipe.

    Once we have incremented the score by 1, make sure to remove that pipe from
    the list!

    The .remove() method may be helpful here.
    """

    # Delete the 'pass' above. Write your code below this line

    for pipe in pipe_list:
        position = pipe.get_position()
        # Remove pipe from list if it went off screen
        if position[0] <= 0:
            pipe_list.remove(pipe)
            score += 1

    return score


# ADD ON: MAKE THE GAME FASTER
def change_level(score: int, pipe_speed: float) -> float:
    """We want our game to get harder the longer a player plays. A cool way to
    do that is make our game get faster! Increase `pipe_speed` based on `score`.

    STUMPED? Increase the speed whenever the score is divisible by 5."""

    # Delete the 'pass' above. Write your code below this line

    if score % 5 == 0 and score != 0:
        pipe_speed += 2

    return pipe_speed


# ADD ON: ADD MUSIC TO YOUR GAME
def get_game_audio() -> str:
    """ Return a string with the location of a song you would like to
    play during your game!"""

    # Delete the 'pass' above. Write your code below this line

    music_file = "assets/sounds/Nitro Fun.mp3"
    return music_file


def get_gameover_audio() -> str:
    """Return a string with the location of a song or sound clip you
    would like to play when the game over screen is displayed"""

    # Delete the 'pass' above. Write your code below this line

    music_file = "assets/sounds/game over.mp3"
    return music_file


# DO NOT MODIFY THE LINE BELOW
if __name__ == "__main__":
    main(globals())
