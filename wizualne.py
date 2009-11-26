#!/usr/bin/env python

import pygame

def input(prezentacja):
    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #lewy przycisk myszy
            prezentacja.tlox()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            #srodkowy przycisk myszy
            prezentacja.tloy()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            prezentacja.tloz()
            #prawy przycisk myszy
            pass
        else:
            pass

class prez(object):
    x = 800
    y = 600
    tlo = [0,0,0]
    screen = ""
    def __init__(self,x,y):
        self.wymiary(x,y)
    def wymiary(self,x,y):
        self.x = x
        self.y = y
    def ekran(self):
        self.screen = pygame.display.set_mode((self.x,self.y))
        pygame.display.set_caption('PyPrez')
        self.screen.fill((0,0,0))
        pygame.display.flip()
        self.tlo[0] += 1
    def tlox(self):
        self.tlo[0] += 10 % 100
        self.screen.fill(self.tlo)
        pygame.display.flip()
    def tloy(self):
        self.tlo[1] += 10 % 100
        self.screen.fill(self.tlo)
        pygame.display.flip()
    def tloz(self):
        self.tlo[2] += 10 % 100
        self.screen.fill(self.tlo)
        pygame.display.flip()



a = prez(640, 480)
a.ekran()
input(a)