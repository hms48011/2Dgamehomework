from pico2d import*
import game_framework

name = "main_state"
image = None

def enter():
    global image
    open_canvas()

def exit():
    global image
    del (image)
    close_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE): game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.quit()

