import random
import pygame
class Button():
    def __init__(self,x,y,pos,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos
        
        def clicked(self,pos)
        self.pos = pygame.mouse.get_pos()
        if self.pos[0]> self.x and self.x +self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
            return False
        class Rpsgame():
            def _init_(self):
                pygame.init()
                self.screen = pygame.display.set_mode((960,640))
                pygame.display.set_caption('RPS Smasher')
                self.by = pygame.image.load('Rps Smasher')
                self.bg = pygame.image.load("bg.png")
                self.r_btn = pygame.image.load('r_btn.png').convert_alpha()