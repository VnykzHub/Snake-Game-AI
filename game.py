# game.py  
import pygame  
import random  

SCREEN_WIDTH = 480  
SCREEN_HEIGHT = 480  
  
GRIDSIZE = 20  
GRID_WIDTH = SCREEN_WIDTH // GRIDSIZE  
GRID_HEIGHT = SCREEN_HEIGHT // GRIDSIZE  
  
UP = (0,-1)  
DOWN = (0,1)  
LEFT = (-1,0)  
RIGHT = (1,0)  

class Snake:  
    def __init__(self):  
        self.length = 1  
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]  
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  
        self.color = (0,255,0) # Green  
  
    def get_head_position(self):  
        return self.positions[0]  
  
    def move(self):  
        cur = self.get_head_position()  
        x,y = self.direction  
        new = (((cur[0]+(x*GRIDSIZE))%SCREEN_WIDTH), (cur[1]+(y*GRIDSIZE))%SCREEN_HEIGHT)  
        if len(self.positions) > 2 and new in self.positions[2:]:  
            self.reset()  
        else:  
            self.positions.insert(0, new)  
            if len(self.positions) > self.length:  
                self.positions.pop()  
  
    def reset(self):  
        self.length = 1  
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]  
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  
  
    def draw(self, surface):  
        for p in self.positions:  
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRIDSIZE,GRIDSIZE))  
  
class Food:  
    def __init__(self):  
        self.position = (0,0)  
        self.color = (255,0,0) # Red  
        self.randomize_position()  
  
    def randomize_position(self):  
        self.position = (random.randint(0, GRID_WIDTH-1)*GRIDSIZE, random.randint(0, GRID_HEIGHT-1)*GRIDSIZE)  
  
    def draw(self, surface):  
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRIDSIZE,GRIDSIZE))  
