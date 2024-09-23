import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

#carico font
font = pygame.font.Font(None, 50)

#render testo
testo = font.render('Benvenuti nel nostro gioco', True, "black")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    screen.blit(testo, (250, 200))
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()
