import pygame
import random
import time
import math
import os

def add_points(a,b):
    return [a[i]+b[i] for i in range(len(a))]

def within(a,b,c,d,point):
    return a[0] < point[0] < b[0] and a[1] < point[1] < b[1]



class background:
    def __init__(self,pos,square_size) -> None:
        self.pos = pos
        self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class assault:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'assault'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class sniper:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'sniper'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class recon:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'recon'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class tank:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'tank'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class plane:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'plane'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class main:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'main'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class farm:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'farm'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class mine:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'mine'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class factory:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'factory'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class airport:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.UT = 'airport'
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)


