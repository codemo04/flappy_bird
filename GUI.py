import pygame
from sprites import *
from learner import *
from helpers import *
import os

def main() -> None:
    """This is the main loop responsible for rendering a pygame window. This
    loop also carries out all major game logic. Many learner functions are
    called in this loop. See if you can see some of the ones you have written!"""

    #CONSTANTS
    dir_name = os.path.dirname(__file__)
    is_game_over = False
    active = True
    pipe_list = []
    pipe_images = [os.path.join(dir_name,"assets/images/pipe.png"),
        os.path.join(dir_name,"assets/images/pipe_upside_down.png")]
    scaling  = 2
    pipe_speed = 25
    timer = 0
    speed = 2
    score = 0
    game_music_file = os.path.join(dir_name,get_game_audio())
    game_over_sound = os.path.join(dir_name,get_gameover_audio())

    #PYGAME INITILIZATIONS
    pygame.display.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((700,700))
    caption = name_your_game()
    if caption is not None:
        pygame.display.set_caption(caption)
    background_image = get_background()
    background = load_background(os.path.join(dir_name,background_image))
    game_over_background = load_background(os.path.join(dir_name,"assets",
        "images","game-over.jpg"))
    player = pygame.sprite.Group()
    pipes = pygame.sprite.Group()
    time = pygame.time.Clock()
    pygame.mixer.music.load(game_music_file)
    pygame.mixer.music.play(-1)

    #RENDER CHARACTER
    character_image = get_character()
    character = Player(os.path.join(dir_name,character_image),(100,100),(0,300))
    player.add(character)

    #MAIN GAME LOOP
    while active and not is_game_over:

        events = pygame.event.get()

        for event in events:
            active = is_active(event)
            keys(character,event)

        player.update()

        new_render = render_pipes(speed, timer, scaling, pipe_images, pipes)
        if new_render != None:
            pipe_list.append(new_render)

        score, pipe_speed = change_score(pipe_list,score,speed,pipe_speed)

        if len(pipe_list) > 0:
            is_game_over = detect_collision(pipe_list, character)

        timer = update_timer(timer,speed,scaling)
        #Update everything seen on screen
        pipes.update(pipe_speed)
        #Push background image to screen
        screen.blit(background, [0,0])
        text_to_screen(screen, "Score is: " + str(score), (500,0))
        #Draw player image onto screen
        player.draw(screen)
        #Draw pipe images onto screen
        pipes.draw(screen)
        pygame.display.flip()
        #Update timer to new time
        timer += time.tick()


    if is_game_over == True:
        pygame.mixer.music.load(game_over_sound)
        pygame.mixer.music.play(-1)
        pipes.remove()
        character.kill()
        screen.blit(game_over_background, [0,0])

        while active:
            events = pygame.event.get()

            for event in events:
                active = is_active(event)

            text_to_screen(screen, "Final Score is: " + str(score),
                (230,600),(255,255,255))
            pygame.display.flip()

    else:
        pygame.quit()


if __name__ == '__main__':
    main()
