import pygame

class Obstacle:
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def collision(self,dot):
		#Assume a class called dot with positions x and y
		if (dot.pos.x > self.x) and (dot.pos.x < self.x + self.width) and (dot.pos.y > self.y) and (dot.pos.y < self.y + self.height):
			return True
		return False 

	def show(self,screen):
		surface = pygame.Surface((self.width,self.height))
		surface = surface.convert()
		# pygame.draw.rect(surface, (233,43,56), pygame.Rect(30, 30, 60, 60))
		surface.fill((233,43,56))
		screen.blit(surface,(self.x,self.y))