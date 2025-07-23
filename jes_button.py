import pygame
from jes_shapes import centerText
import time

class Button:
    def __init__(self,ui,pdim,pnames,pfunc):
        self.dim = pdim  # Dim is a list of 4 parameters: x, y, width, height
        self.names = pnames
        self.setting = 0
        self.timeOfLastClick = 0
        self.func = pfunc
        ui.buttonList.append(self)
        
    def drawButton(self, screen, font):
        x, y, w, h = self.dim
        name = self.names[self.setting]
        
        sliderSurface = pygame.Surface((w/1.7,h/2), pygame.SRCALPHA, 32)
        sliderSurface.fill((30,150,230))
        if name == "Turn off Autogen" or name[:4] == "Stop" or name[:4] == "Hide":
            sliderSurface.fill((128,255,255))
        centerText(sliderSurface, name, w/3.4, (h/3.4)-1, (0,0,0), font)
            
        screen.blit(sliderSurface,((x/1.523)+447,y+70))
        
    def click(self):
        self.setting = (self.setting+1)%len(self.names)
        self.timeOfLastClick = time.time()
        self.func(self)