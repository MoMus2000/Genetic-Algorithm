import pygame
import math

#Creating a 2d vector to get magnitude and compute distance

class Force:
    def __init__(self,xx,yy,limit=0):
        self.x = xx
        self.y = yy
        self.limit = limit

    def add(self,other_force):
        self.x = self.x + other_force.x
        self.y = self.y + other_force.y
        mag = self.magnitude(self)


    @staticmethod
    def distance(pvec1, pvec2):
        x_dist = pvec1.x - pvec2.x
        y_dist = pvec1.y - pvec2.y
        return math.sqrt(x_dist * x_dist + y_dist * y_dist)

    @staticmethod
    def angle(theta=0):
        x = Force(math.cos(theta),math.sin(theta))
        return Force(math.cos(theta),math.sin(theta))

    @staticmethod
    def magnitude(pvec):
        mag = math.sqrt(math.pow(pvec.x,2) + math.pow(pvec.y,2))
        return mag








