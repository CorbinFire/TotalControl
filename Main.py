import pygame
import random
import time
import math
import os
from classes import *

pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
width,hieght = info.current_w,info.current_h
square_size = [width,width] if width < hieght else [hieght,hieght]
add_to_each_point = [0,(hieght-width)/2] if width < hieght else [(width-hieght)/2,0]
wn = pygame.display.set_mode([width,hieght],pygame.RESIZABLE)

print(square_size)
Home = True
Main = False
Tutorial = False
Shop = False
while Home:
    time.sleep(0.001)
    Mouse = pygame.mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Home = False
    wn.fill((0,0,0))
    wn.blit(background([0,0],square_size).im,add_to_each_point)
    pygame.display.flip()