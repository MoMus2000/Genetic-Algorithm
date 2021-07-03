import pygame
from Force import Force
#Define a size and define a vector for later operations
#Use size to create a pygame circle

class Goal:

    def __init__(self,x,y):
        self.pos = Force(x,y)
        self.size = 20

    def display(self,screen):
        surf1 = pygame.Surface((self.size*2,self.size*2))
        surf1 = surf1.convert()
        pygame.draw.circle(surf1, (233,43,56), (self.size-1,self.size-1), self.size)
        screen.blit(surf1,(self.pos.x-self.size,self.pos.y-self.size))


