import pygame
import sys
import os
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Gestione del testo")

bkgPath = os.path.join(os.path.dirname(__file__), 'img/background-game.png')
characterPath = os.path.join(os.path.dirname(__file__), 'img/wizard.png')

# Caricamento dell'immagine
bkg = pygame.image.load(bkgPath)
wizard = pygame.image.load(characterPath)

# Ridimensionamento immagine
bkg = pygame.transform.scale(bkg, (800, 600))

wizard = pygame.transform.scale(wizard, (200, 200))

# Caricare il nostro font
font = pygame.font.Font(None, 36)

# Render del testo
testo = font.render('Benvenut* nel nostro gioco', True, (0, 0, 0))



pygame.display.flip()

# ESERCIZIO
# caricare un'immagine di sfondo (es. paesaggio) e posizionare sopra di essa un'immagine di un personaggio.


# Crea un oggetto Clock per gestire il frame rate
orologio = pygame.time.Clock()

# Imposta il frame rate desiderato (ad esempio 60 FPS)
frame_rate = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # pygame.KEYDOWN
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    
    screen.fill((255, 255, 255))

    # Posizionamento dell'immagine
    # screen.blit(bkg, (0, 0))
    # screen.blit(wizard, (350, 350))

    screen.blit(testo, (100, 50))
    
    orologio.tick(frame_rate)
    
    
    
    pygame.display.update()