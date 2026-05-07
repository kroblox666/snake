from settings import *
import random
import pygame
def create_apple():
    x = random.randint(0, (WIDTH-SIZE)//SIZE) * SIZE
    y = random.randint(0, (HEIGHT-SIZE)//SIZE) * SIZE
    return [x, y]



def draw_game(screen, snake, apple, score):
    screen.fill("black")
    
    pygame.draw.rect(screen, "red", (apple[0], apple[1], SIZE, SIZE))
    
    for i, segment in enumerate(snake):
        pygame.draw.rect(screen, "green", (segment[0], segment[1], SIZE, SIZE))