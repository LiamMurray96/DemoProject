import pygame
larghezza, altezza = 800, 600

pygame.init()

screen = pygame.display.set_mode((larghezza, altezza))
clock = pygame.time.Clock()
running = True
dt = 0

bkg = pygame.image.load(bkgPath)
#posizionamento immagine
screen.blit(bkg, (0,0))
screen.blit(wizard, (350, 350))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()