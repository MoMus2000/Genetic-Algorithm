import pygame
import random
import math
from Force import Force

# Responsible for adujusting the acceleration and proving driving directions to the dots
# Consists of the acceleration vectors applied to the dots
# It can initialise, clone and mutate itself
class DNA:
	#Initialization of the first batch of DNA
	def __init__(self, size=100):
		self.directions = []
		self.step = 0

		for i in range(size):
			#360 degree directions
			angle = random.uniform(0,2* math.pi)
			direction = Force.angle(angle)
			self.directions.append(direction)

	def mutate(self,mutation_rate):
		for i in range(len(self.directions)):
			current_prob = random.uniform(0,1)
			if current_prob < mutation_rate:
				angle = random.uniform(0,2*math.pi)
				self.directions[i] = Force.angle(angle)


	# Essentially we are creating a shallow copy of directions and returning the child
	def create_child(self):
		dna = DNA(len(self.directions))
		dna.directions = self.directions.copy()
		return dna





