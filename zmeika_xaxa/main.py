import pygame
from settings import *
from logic import *



pygame.init()
pygame.display.set_caption("змейка ползает по заминированному полю и собирает яблоки")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
def restart_game():
    snake = [[300, 225]]
    direction = "up"
    score = 0
    apple = create_apple()
    return snake, direction, apple, score







snake, direction, apple, score = restart_game()
game_state = "PLAY"







running = True
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
    
    draw_game(screen, snake, apple, score)
            
            
            
    
    pygame.display.update()
clock.tick(FPS)