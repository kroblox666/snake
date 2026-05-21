import pygame
from settings import *
from logic import *

pygame.init()
pygame.display.set_caption("змейка ползает по заминированному полю и собирает яблоки")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def restart_game():
    snake = [[400, 200]]
    direction = "up"
    score = 0
    apple = create_apple()
    return snake, direction, apple, score

snake, direction, apple, score = restart_game()
game_state = "PLAY"

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
                
                
            if event.key == pygame.K_r and game_state == "GAMEOVER":
                snake, direction, apple, score = restart_game()
                game_state = "PLAY"
                
    if game_state == "PLAY":
        new_heade = list(snake[0])
        if direction == "up":
            new_heade[1] -= SIZE
        if direction == "down":
            new_heade[1] += SIZE
        if direction == "right":
            new_heade[0] += SIZE
        if direction == "left":
            new_heade[0] -= SIZE
            
        snake.insert(0, new_heade)
        if snake[0] == apple:
            score += 1
            apple = create_apple()
        else:
            snake.pop()
            
        if chek_collision(snake):
            game_state = "GAMEOVER"
        
            
    draw_game(screen, snake, apple, score)
    if game_state == "GAMEOVER":
        font = pygame.font.SysFont("Arial", 48)
        msg = font.render("ТЫ ПРОИГРАЛ😈", True, (255, 255, 0))
        screen.blit(msg, [WIDTH//6, HEIGHT//2.5])

    pygame.display.update()
    clock.tick(FPS)