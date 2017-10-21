from pico2d import*
import game_framework
import title_state

name = 'main_stage'
image = None
main_change = True

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

open_canvas()

def enter():
    global boy,grass
    open_canvas()
    boy = Boy()
    grass = Grass()

def exit():
    global boy,grass
    del(boy)
    del(grass)
    close_canvas()


grass = Grass()
boy = Boy()

running = True

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_ESCAPE:
                running = False

def update():
    global main_change

    if (main_change == False):
        main_change = True
        game_framework.change_state(title_state)
    boy.update()

    delay(0.01)
    handle_events()

def draw():
    global image
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
