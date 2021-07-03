import pygame
from Dot import Dot
from Force import Force
from Dna import DNA
import random

#Collection of dot objects

class Population:
    def __init__(self,population_size=100,starting_pos_x=175,starting_pos_y=300):
        self.pop_arr = []

        for i in range(population_size):
            dot = Dot(starting_pos_x,starting_pos_y)
            self.pop_arr.append(dot)

        self.fitness = 0
        self.fitnessSum = 0
        # self.bestSteps = len(self.pop_arr[0].brain.directions)
        self.best_dot = 0
        self.generation = 1
        self.best_steps = 0


    def show(self,screen):
        for dot in self.pop_arr:
            dot.show(screen)

    def update(self,screen_width,screen_height,goal,obstacles):
        for dot in self.pop_arr:
            dot.update(screen_width,screen_height,goal,obstacles)

    #Iterate through the list and find the dot with the maximum fitness
    def select_best_dot(self):
        index = 0
        max_fitness = 0
        for idx, dot in enumerate(self.pop_arr):
            print(idx)
            fitness = dot.fitness
            if(fitness > max_fitness):
                max_fitness = fitness
                index = idx

        self.best_dot = index


    #Metric used to select probability of picking a parent based on fitness
    def sum_of_fitness(self):
        sum_fitness = 0
        for dots in self.pop_arr:
            sum_fitness+= dots.fitness
        self.fitnessSum = sum_fitness
        return sum_fitness

    def calculateFitness(self,Goal):
        for i in range (len(self.pop_arr)):
            self.pop_arr[i].calculate_fitness(Goal)

    #Method to create the next generation of dots
    def natural_selection(self):
        dots = []
        #Get the best dot
        self.select_best_dot()
        best_dot = self.pop_arr[self.best_dot]
        #create a child

        print(self.best_dot)
        child = best_dot.create_child()
        child.is_best = True

        print(child)
        dots.append(child)
        #Add other parents now based on fitness
        for i in range(1,len(self.pop_arr)):
            parent = self.get_parent()
            child2 = parent.create_child()
            dots.append(child2)

        self.pop_arr = dots.copy()
        self.generation +=1


    def get_parent(self):
        sum_fitness = self.sum_of_fitness()
        rand = random.uniform(0,sum_fitness)
        running_sum = 0
        for dots in self.pop_arr:
            running_sum += dots.fitness
            if running_sum > rand:
                return dots
        print("function broke")
        return self.pop_arr[0]


    def all_dead(self):
        for dot in self.pop_arr:
            if dot.is_dead == False and dot.reached_goal == False:
                return False
        return True

    def mutate_dot(self,mutation_rate):
        for i in range(1,len(self.pop_arr)):
            self.pop_arr[i].brain.mutate(mutation_rate)

















    