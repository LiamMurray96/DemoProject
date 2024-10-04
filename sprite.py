import pygame
import sys

width, heigth = 800, 600
pygame.init()
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()
running = True
dt = 0

class Personaggio(pygame.sprite.Sprite):
    #costruttore classe
    def __init__(self, x, y):
        #chiamiamo il costruttore della super classe, in questo caso Sprite
        super().__init__()
        #carichiamo immagine personaggio
        self.image = pygame.image.load("img/morrigan.png")
        self.image = pygame.Surface.convert_alpha(self.image)
        #ridimensioniamo il personaggio
        self.image = pygame.transform.scale(self.image, (210, 200))

        #rettangolo di posizione e collegamento
        self.rect = self.image.get_rect()

        self.rect.topleft = (x,y)
        self.velocita_x = 0
        self.velocita_y = 0

        #self.mask = pygame.mask.from_surface(self, self.image)

    def update(self):
            self.rect.x += self.velocita_x
            self.rect.y += self.velocita_y
            #controllo limiti dello schermo
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > width:
                self.rect.right = width
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > heigth:
                self.rect.bottom = heigth

    def cambia_velocita(self, x, y):
        self.velocita_x += x
        self.velocita_y += y

#creazione dello sprite personaggio
personaggio = Personaggio(100, 100)
altropersonaggio = Personaggio(400, 400)

if personaggio.rect.colliderect(altropersonaggio.rect):
    screen.fill("red")

#gruppo di sprite per gestione facilitata
gruppo_di_personaggi = pygame.sprite.Group()
gruppo_di_personaggi.add(personaggio)
gruppo_di_personaggi.add(altropersonaggio)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
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

    gruppo_di_personaggi.update()

    screen.fill("purple")

    gruppo_di_personaggi.draw(screen)

    dt = clock.tick(60) / 1000

    pygame.display.update()

pygame.quit()