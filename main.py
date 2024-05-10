import text
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock
run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill("black")
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_COMMA]:
        run_screen = pygame.display.set_mode((500, 500), 0, 32)
        
        
        text.read()
    
    
    pygame.display.flip()
            
pygame.quit()