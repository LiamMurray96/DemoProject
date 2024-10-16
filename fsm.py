import math
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, direction):
        # Muove il giocatore in base alla direzione
        pass
# Modificare il codice per far si che l'NPC si muova verso il giocatore solo se la distanza è inferiore a un certo valore (100px)

class NPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def follow_player(self, player):
        if distance(player, self) < 100:
            if self.x < player.x:
                self.x += 1
            elif self.x > player.x:
                self.x += 1
            if self.y < player.y:
                self.y += 1
            elif self.y > player.y:
                self.y += 1

def distance(player, npc):
    return math.sqrt((player.x - npc.x) ** 2 + (player.y - npc.y) ** 2)