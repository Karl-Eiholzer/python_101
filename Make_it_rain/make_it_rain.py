'''Import necessary libraries'''

import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))

'''Set parameters'''
xpos = 50

'''Main Body'''

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_RIGHTBRACKET]
        xpos += 1
    if pressed_keys[K_LEFTBRACKET]
        xpos -= 1
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,255,0),(xpos,200),20)
    pygame.display.update()