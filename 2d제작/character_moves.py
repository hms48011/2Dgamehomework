from pico2d import*

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

def handle_evnts():
    global running
    global x

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x = x+10
            elif event.key == SDLK_LEFT:
                x = x-10
            elif event.key == SDLK_ESCAPE:
                running = False


running = True
x=0
frame = 0



while (running):
    handle_evnts()
    clear_canvas()
    grass.draw_now(400, 30)
    character.clip_draw(frame*100,0,100,100,x,90)
    update_canvas()
    frame = (frame +1)%8
    delay(0.01)
    get_events()

close_canvas()