import pygame
from Force import Force
import random
from Dna import DNA


class Dot:

    def __init__(self,x,y):
        self.pos = Force(x,y)
        self.vel  = Force(0,0,5)
        self.acc = Force(0,0)
        self.brain = DNA(400)
        self.is_best = False
        self.is_dead = False
        self.reached_goal = False
        self.fitness = 0


    def show(self,screen):
        dot_rad = 2
        if self.is_best:
            dot_rad = 4
            surf1 = pygame.Surface((dot_rad*2,dot_rad*2))
            surf1 = surf1.convert()
            pygame.draw.circle(surf1, (0,0,0), (dot_rad-1,dot_rad-1), dot_rad)
            screen.blit(surf1,(self.pos.x-dot_rad,self.pos.y-dot_rad))

        else:
            surf1 = pygame.Surface((dot_rad*2,dot_rad*2))
            surf1 = surf1.convert()
            pygame.draw.circle(surf1, (233,122,234), (dot_rad-1,dot_rad-1), dot_rad)
            screen.blit(surf1,(self.pos.x-dot_rad,self.pos.y-dot_rad))


    def move(self):
        if (len(self.brain.directions)>self.brain.step):
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step += 1
        else:
            pass
        self.vel.add(self.acc)
        self.pos.add(self.vel)


    # check screen boundaries, check for collision and check if reached goal
    def update(self,screen_width,screen_height,goal,obstacles):

        if self.reached_goal == False and self.is_dead == False:
            self.move()
            x = self.pos.x
            y = self.pos.y

            if x > screen_width-2 or y > screen_height-2 or x < 2 or y < 2:
                self.is_dead = True

            elif Force.distance(self.pos,goal.pos) < goal.size:
                self.reached_goal = True

            for obs in obstacles:
                if obs.collision(self):
                    self.is_dead = True


    #Calculate distance from the goal as fitness function
    def calculate_fitness(self,goal):
        try:
            self.fitness = 1.0/(Force.distance(self.pos,goal.pos)*Force.distance(self.pos,goal.pos))
        except:
            self.fitness = 0

    #Initialise a dot object and give it a brain i.e give it some direction vector
    def create_child(self):
        dot = Dot(500,700)
        dot.brain = self.brain.create_child()
        return dot







