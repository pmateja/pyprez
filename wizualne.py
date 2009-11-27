#!/usr/bin/env python

import pygame
import sys

def input(prezentacja):
    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            running = 0 
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            #lewy przycisk myszy
            prezentacja.i += 1
            prezentacja.slajd(1)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            #srodkowy przycisk myszy
            prezentacja.tloy()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            prezentacja.i -= 1
            prezentacja.slajd(prezentacja.i)
            #prawy przycisk myszy
            pass
        else:
            pass
    pygame.quit()

class prez:
    x = 800
    y = 600
    tlo = [0,0,0]
    screen = ""
    i = 0
    dane = ""
    def __init__(self, dane=""):
        self.dane = dane
    def wymiary(self,x,y):
        self.x = x
        self.y = y
    def ekran(self):
        #self.screen = pygame.display.set_mode((self.x,self.y))
        pygame.init()
        modes = pygame.display.list_modes(32)
        self.screen = pygame.display.set_mode(modes[0])
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
    def slajd(self, i=0):
        a = self.dane.slajd[i]
        # Render the text
        font = pygame.font.Font(None, 26)
        tytul = font.render(a.tytul, True, (255,
        255, 255), (159, 182, 205))

        # Create a rectangle
        textRect = tytul.get_rect()

        # Center the rectangle
        textRect.centerx = self.screen.get_rect().centerx
        textRect.centery = self.screen.get_rect().centery

        # Blit the text
        self.screen.blit(tytul, (textRect.centerx, 20))

        font = pygame.font.Font(None, 26)
        tresc = font.render(a.tresc, True, (255,
        255, 255), (159, 182, 205))

        # Create a rectangle
        textRect = tresc.get_rect()

        # Center the rectangle
        textRect.centerx = self.screen.get_rect().centerx
        textRect.centery = self.screen.get_rect().centery

        # Blit the text
        self.screen.blit(tresc, textRect)
        #-----------------------------------
        toWrite = a.tresc
        wordsToWrite = toWrite.rstrip().split(" ") #Get rid of the newline char and split on spaces
        currLine = ""
        numLines = 0
        maxAllowedWidth = 800
        maxWidthFound = 0
        lines = []
        color = (1,1,1)
        bgcolor = (255,255,255)
        for word in wordsToWrite:
            currLine = currLine + " " + word #Add the next word to the line

            if ((font.size(currLine))[0] > maxAllowedWidth): #Check if the width of the line exceeds the set limit

                if (font.size(currLine))[0] > maxWidthFound: #Get the maximum line width found
                    maxWidthFound = (font.size(currLine))[0]

                lines.append (font.render(currLine, 1, color)) #Add the rendered line to a list
                currLine = ""
                numLines = numLines + 1

        if currLine != "": #Once we exit the loop, we will probably still have a line to be rendered
            lines.append (font.render(currLine, 1, color))
            currLine = ""
            numLines = numLines + 1

        #self.image = pygame.Surface((maxWidthFound + 20, numLines * textFont.get_height() + 20)) #Create a surface of the appropriate size

        for lineNum in range(numLines): 
            self.screen.blit(lines[lineNum], (10,lineNum * font.get_height() + 10))
    #-------------------------------------
        pygame.display.update()


if __name__ == "__main__":

    import parser
    mm = open("test.xml")
    prezentacja = parser.xml2obj(mm)
    a = prez(prezentacja)
    a.ekran()
    input(a)
