import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
WINDOW_HOR = 800
WINDOW_VER = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class PelotaPong():
    def __init__(self, surface):

        # --- Atributos de la clase ---
        self.surface = surface
        self.color = WHITE

        # Dimensiones de la pelota
        self.radio = 15

        # Posicion de la pelota
        self.x = WINDOW_HOR / 2
        self.y = WINDOW_VER / 2

        # Direccion de movimiento de la pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])
       
    def fill(self):
        pygame.draw.circle(self.surface, self.color, [self.x, self.y], self.radio)

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= 0:
            self.dir_x = -self.dir_x
        if self.x + self.radio >= WINDOW_HOR:
            self.dir_x = -self.dir_x
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.radio >= WINDOW_VER:
            self.dir_y = -self.dir_y
    
    def reiniciar(self):
        self.x = WINDOW_HOR / 2 - self.radio / 2
        self.y = WINDOW_VER / 2 - self.radio / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])

class RaquetaPong():
    def __init__(self, surface):

        # --- Atributos de la clase ---
        self.surface = surface
        self.color = WHITE

        # --- Dimensiones de la raqueta ---
        self.ancho = 30
        self.alto = 120

        # --- Posicion de la raqueta
        self.x = 0
        self.y = (WINDOW_VER / 2) - (self.alto / 2)

        # --- Direccion de movimiento de la raqueta ---
        self.dir_y = 0

    def fill(self, x):
        self.x = x
        pygame.draw.rect(self.surface, self.color, [self.x, self.y, self.ancho, self.alto])

    def mover(self):
        self.y += self.dir_y

        if self.y <= 0:
            self.y = 0
        
        if self.y + self.alto >= WINDOW_VER:
            self.y = WINDOW_VER - self.alto

    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3

        elif self.y < pelota.y:
            self.dir_y = 3

        else:
            self.dir_y = 0
        
        self.y += self.dir_y

    def golpear(self, pelota):
        if (pelota.x < self.x + self.ancho 
        and pelota.x > self.x 
        and pelota.y + pelota.radio > self.y
        and pelota.y < self.y + self.alto):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho

    def golpear_ia(self, pelota):
        if (pelota.x > self.x
        and pelota.x < self.x + self.ancho
        and pelota.y + pelota.radio > self.y
        and pelota.y < self.y + self.alto):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.radio

def main():
    # Inicialización de pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    window = pygame.display.set_mode((WINDOW_HOR, WINDOW_VER))
    pygame.display.set_caption('Pong')

    #instaciación
    pelota = PelotaPong(window)

    raqueta_1 = RaquetaPong(window)
    pos_raqueta_1 = 60

    raqueta_2 = RaquetaPong(window)
    pos_raqueta_2 = WINDOW_HOR - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_ia(pelota)

        window.fill(BLACK)
        pelota.fill()
        raqueta_1.fill(pos_raqueta_1)
        raqueta_2.fill(pos_raqueta_2)

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_DOWN:
                    raqueta_1.dir_y = 5
            
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_UP:
                    raqueta_1.dir_y = 0
                if event.type == pygame.K_DOWN:
                    raqueta_1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()