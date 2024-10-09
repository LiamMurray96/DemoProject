import pygame
import sys

from sprite import Personaggio, Stone
pygame.init()
# Definisci le dimensioni della finestra
dimensioni = (800, 600)

# Crea una finestra di gioco
screen = pygame.display.set_mode(dimensioni)

# Imposta il titolo della finestra
pygame.display.set_caption("Menu")

# Crea un oggetto Clock per gestire il frame rate
orologio = pygame.time.Clock()

# Imposta il frame rate desiderato (ad esempio 60 FPS)
frame_rate = 60

font = pygame.font.Font(None, 36)

def main_menu():
    while True:
        # Gestione degli eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    start_game()

                if exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
            # Creazione della schermata iniziale
            text_start = font.render('Inizia', True, "white")
            text_instructions = font.render('Istruzioni', True, "white")
            text_exit = font.render('Esci', True, "white")

            # Definiamo i nostri bottoni
            start_button = pygame.Rect(150, 200, 200, 50)
            instructions_button = pygame.Rect(150, 270, 200, 50)
            exit_button = pygame.Rect(150, 340, 200, 50)
                    
            
            # Riempi la finestra con il colore di sfondo
            screen.fill("white")

            # Disegna rettangoli sullo schermo
            pygame.draw.rect(screen, "blue", start_button)
            pygame.draw.rect(screen, "blue", instructions_button)
            pygame.draw.rect(screen, "blue", exit_button)

            screen.blit(text_start, (160, 210))  # Posiziona il testo nel rettangolo
            screen.blit(text_instructions, (160, 280))
            screen.blit(text_exit, (160, 350))

            pygame.display.update()


personaggio = Personaggio(400, 300)
gruppo_personaggio = pygame.sprite.Group()
gruppo_personaggio.add(personaggio)

stone1 = Stone(400, 500)
stone2 = Stone(600, 200)
stone3 = Stone(200, 100)
gruppo_stones = pygame.sprite.Group()
gruppo_stones.add([stone1, stone2, stone3])

fontScore = pygame.font.Font(None, 24)


def start_game():
    score = 0
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
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    personaggio.cambia_velocita(-5, 0)
                if event.key == pygame.K_RIGHT:
                    personaggio.cambia_velocita(5, 0)
                if event.key == pygame.K_UP:
                    personaggio.cambia_velocita(0, -5)
                if event.key == pygame.K_DOWN:
                    personaggio.cambia_velocita(0, 5)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    personaggio.cambia_velocita(5, 0)
                if event.key == pygame.K_RIGHT:
                    personaggio.cambia_velocita(-5, 0)
                if event.key == pygame.K_UP:
                    personaggio.cambia_velocita(0, 5)
                if event.key == pygame.K_DOWN:
                    personaggio.cambia_velocita(0, -5)

        screen.fill("blue")
        
        gruppo_personaggio.update()
        gruppo_stones.update()

        gruppo_personaggio.draw(screen)
        gruppo_stones.draw(screen)
        
        
        # Logica di collisione tra personaggio e sasso
        if pygame.sprite.spritecollide(stone1, gruppo_personaggio, False):
            score+=1
            stone1.kill()
        if pygame.sprite.spritecollide(stone2, gruppo_personaggio, False):
            score+=1
            stone2.kill()
        if pygame.sprite.spritecollide(stone3, gruppo_personaggio, False):
            score+=1
            stone3.kill()
        
        score_text = font.render(f'Punteggio: {score}', True, "white")
        screen.blit(score_text, (10, 10))
        # Aggiorna il display
        pygame.display.update()

        # Limita il frame rate al valore specificato
        orologio.tick(frame_rate)



if __name__ == "__main__":
    main_menu()






