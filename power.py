import pygame
import sys
from pygame.sprite import _Group

width, heigth = 800, 600
pygame.init()
screen = pygame.display.set_mode((width, heigth))
power_up_timer = None
power_up_duration = 3000
clock = pygame.time.Clock()
running = True
dt = 0

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/saetta")
        self.image = pygame.Surface.convert_alpha(self.image)
        self.image = pygame.transform.scale(self.iamge, (50, 50))

class Player(pygame.sprite.Sprite):
    #costruttore classe
    def __init__(self, x, y):
        #chiamiamo il costruttore della super classe, in questo caso Sprite
        super().__init__()
        #carichiamo immagine personaggio
        self.image = pygame.image.load("img/pacman_(2).png")
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
power_ups = pygame.sprite.Group()
player = Player(100, 100)

if pygame.sprite.collide_rect(player, power_Up):
    player.cambia_velocita(10, 0)
    power_up.kill()


if power_up_timer is not None:
    if pygame.time.get_ticks():
    power_up_timer > power_up_duration:
        player.cambia_velocita(5)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_LEFT:
                player.cambia_velocita(-5, 0)
            if event.key == pygame.K_RIGHT:
                player.cambia_velocita(5, 0)
            if event.key == pygame.K_UP:
                player.cambia_velocita(0, -5)
            if event.key == pygame.K_DOWN:
                player.cambia_velocita(0, 5)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.cambia_velocita(5, 0)
            if event.key == pygame.K_RIGHT:
                player.cambia_velocita(-5, 0)
            if event.key == pygame.K_UP:
                player.cambia_velocita(0, 5)
            if event.key == pygame.K_DOWN:
                player.cambia_velocita(0, -5)

    players.update()
    power_ups.update()

    screen.fill("purple")

    players.draw(screen)
    power_ups.draw(screen)

    dt = clock.tick(60) / 1000

    pygame.display.update()

pygame.quit()