'''Classes Defined for Use in Main Application'''

import random, pygame, sys

class Raindrop:
    def __init__(self):
        self.x = random.randint(100,1000)
        self.y = -100

    def move(self):
        self.y += -.1

    def draw(self):
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x,self.y+10),1)