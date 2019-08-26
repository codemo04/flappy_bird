import pygame
from sprites import *
from learner import *
from helpers import *
import os

def main():
    dir_name = os.path.dirname(__file__)
    #CONSTANTS
    is_game_over = False
    active = True
    pipe_list = []
    pipe_images = [os.path.join(dir_name,"assets","images","pipe.png"),os.path.join(dir_name,"assets","images","pipe_upside_down.png")]
    scaling  = 2
    pipe_speed = 25
    timer = 0
    speed = 2
    score = 0
    music_file = os.path.join(dir_name,"assets","sounds",get_audio())
    game_over_sound = os.path.join(dir_name,"assets","sounds","game over.mp3")

    #PYGAME INITILIZATIONS
    pygame.display.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((700,700))
    caption = name_your_game()
    if caption is not None:
        pygame.display.set_caption(caption)
    background = load_background(os.path.join(dir_name,"assets","images","background.png"))
    game_over_background = load_background(os.path.join(dir_name,"assets","images","game-over.jpg"))
    player = pygame.sprite.Group()
    pipes = pygame.sprite.Group()
    time = pygame.time.Clock()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)

    #RENDER CHARACTER
    character = Player(os.path.join(dir_name,"assets","images","bird.png"),(100,100),(0,300))
    player.add(character)

    #MAIN GAME LOOP
    while active and not is_game_over:
        key_pressed = False
        events = pygame.event.get()

        for event in events:
            active = is_active(event)
            keys(character,event)

        if key_pressed is False:
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

            text_to_screen(screen, "Final Score is: " + str(score), (230,600),(255,255,255))
            pygame.display.flip()

    else:
        pygame.quit()
        #pygame.mixer.music.stop()

if __name__ == '__main__':
    main()
