import pygame
from Obstacles import Obstacle
from Goal import Goal
from Dot import Dot
import random
from Population import Population

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGTH = 800

    FPSCLOCK = pygame.time.Clock()


    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))

    background = pygame.Surface(screen.get_size())
    background = background.convert()

    background_color = (255,255,255)

    background.fill(background_color)

    running = True

    obstacles = []

    obstacle = Obstacle(60,700,250,25)
    obstacle2 = Obstacle(200,300,575,25)
    obstacle3 = Obstacle(100,600,575,25)


    obstacles.append(obstacle)
    obstacles.append(obstacle2)
    obstacles.append(obstacle3)

    goal = Goal(200,20)

    pop = Population(100,500,700)
    
    i = 0 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(background,(0,0))
        goal.display(screen)

        for obstacle in obstacles:
            obstacle.show(screen)

        
        
        if(pop.all_dead() == True):
            i += 1
            pop.calculateFitness(goal)
            pop.natural_selection()
            pop.mutate_dot(0.01)
            

        else:
            pop.update(800,800,goal,obstacles)
            pop.show(screen)
        

        font = pygame.font.SysFont(None, 24)
        img = font.render(f"Generation {pop.generation}", True, (0,0,255))
        screen.blit(img, (20, 20))
            # print(pop.pop_arr[0].brain.directions[0].x,pop.pop_arr[0].brain.directions[0].y)
            
        # FPSCLOCK.tick(10)
        pygame.display.update()






if __name__ == '__main__':
    main()