import pygame as pg , sys
from Button import *

pg.init()
clock = pg.time.Clock()
running = True

window = pg.display.set_mode((1024, 600))
window.fill((0, 0, 0))

#loading image's
start_img = pygame.image.load('start.png').convert_alpha()
exit_img = pygame.image.load('exit.png').convert_alpha()

#define the button     x    y              size
start_button = Button(440, 270, start_img, 0.8)
exit_button = Button(450, 420, exit_img, 0.8)

while running:
    clock.tick(60)
    window.fill((0, 0, 0))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
    #                    suface       
    if start_button.draw(window):
        print("start")
    if exit_button.draw(window):
        sys.exit()

    pg.display.flip()

pg.quit()