'''Import necessary libraries'''
import pygame, sys, random
from pygame.locals import *
pygame.init()

'''Set parameters'''

'Clock Settings'
clock = pygame.time.Clock()
raindrop_spawn_time=0

'Screen Size'
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))

'Start Conditions'
xpos = 0.5
trade_yield = .9
raindrops = []

'Captions'
pygame.display.set_caption("Transaction Data Visualization")

'''Class for Raindrop'''

class Raindrop:
    def __init__(self):
        self.x = random.randint(screen_width*.1,screen_width*1)
        self.y = 0

    def move(self):
        self.y += 2
        self.x += -.2

    def draw(self):
        pygame.draw.line(screen,(0,102,104),(self.x,self.y),(self.x,self.y+20),1)

    def end_reached(self):
        return self.y > screen_height*trade_yield

'''Main Body'''
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    'Rain Generation'
    raindrops.append(Raindrop())

    screen.fill((255,255,255))

    i=0
    while i < len(raindrops):
        raindrops[i].move()
        raindrops[i].draw()
        end_flag = False
        if raindrops[i].end_reached():
            end_flag = True
        if end_flag:
            del raindrops[i]
            i-=1
        i+=1
    pygame.display.update()

'''     'Circle Movement'
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_RIGHT]:
        xpos += 0.01
    if pressed_keys[K_LEFT]:
        xpos -= 0.01
    
    pygame.draw.circle(screen,(0,255,0),(int(screen_width*xpos),200),20) '''
    