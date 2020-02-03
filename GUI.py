import pygame
from sprites import *
from learner import *
from helpers import *
import os

def main() -> None:
    """This is the main loop responsible for rendering a pygame window. This
    loop also carries out all major game logic. Many learner functions are
    called in this loop. See if you can see some of the ones you have written!
    """

    ###CONSTANTS###
    dir_name = os.path.dirname(__file__)
    is_game_over = False
    active = True
    pipe_list = []
    pipe_images = [os.path.join(dir_name,"assets/images/pipe.png"),
        os.path.join(dir_name,"assets/images/pipe_upside_down.png")]
    scaling  = 2
    pipe_speed = 5
    timer = 0
    speed = 2
    score = 0
    #game_music_file = os.path.join(dir_name,get_game_audio())
    #game_over_sound = os.path.join(dir_name,get_gameover_audio())

    ###PYGAME INITILIZATIONS###
    pygame.display.init()
    #pygame.mixer.init()
    time = pygame.time.Clock()

    #DO NOT CHANGE THE DISPLAY SET MODE
    screen = pygame.display.set_mode((700,700))

    ###SET CAPTION FOR GAME###
    caption = set_name()
    if caption is not None:
        pygame.display.set_caption(caption)
    background_image = get_background()
    gameover_image = get_gameover_background()

    ###LOAD BACKGROUND IMAGE AND GAME OVER BACKGROUND###
    background = load_background(os.path.join(dir_name,background_image))
    game_over_background = load_background(os.path.join(dir_name,gameover_image))

    PLAYER = pygame.sprite.Group()
    PIPES = pygame.sprite.Group()

    #pygame.mixer.music.load(game_music_file)
    #pygame.mixer.music.play(-1)

    ###RENDER CHARACTER###
    character_image = get_character()
    character = Player(os.path.join(dir_name,character_image),(100,100),(0,300))
    PLAYER.add(character)

    #MAIN GAME LOOP
    while active and not is_game_over:

        events = pygame.event.get()
        key_pressed = False

        for event in events:
            active = is_active(event)
            key_pressed = keys(character,event)

        if key_pressed == False:
            PLAYER.update()

        new_render = render_pipes(speed, timer, scaling, pipe_images, PIPES)
        if new_render != None:
            pipe_list.append(new_render)

        score, pipe_speed = change_score(pipe_list,score,speed,pipe_speed)

        if len(pipe_list) > 0:
            is_game_over = detect_collision(pipe_list, character)

        timer = update_timer(timer,speed,scaling)
        #Update everything seen on screen
        PIPES.update(pipe_speed)
        #Push background image to screen
        screen.blit(background, [0,0])
        text_to_screen(screen, "Score is: " + str(score), (500,0))
        #Draw player image onto screen
        PLAYER.draw(screen)
        #Draw pipe images onto screen
        PIPES.draw(screen)
        pygame.display.flip()
        #Update timer to new time
        timer += time.tick()

    if is_game_over == True:
        #pygame.mixer.music.load(game_over_sound)
        #pygame.mixer.music.play(-1)
        PIPES.remove()
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
