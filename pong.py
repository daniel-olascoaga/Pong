import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
WINDOW_HOR = 800
WINDOW_VER = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class PelotaPong:
    def __init__(self, surface):
        # --- Atributos de la clase ---
        self.surface = surface

        # Dimensiones de la pelota
        self.radio = 15

        # Posicion de la pelota
        self.x = WINDOW_HOR / 2
        self.y = WINDOW_VER / 2

        # Imagen de la pelota
        # self.image = [self.surface, GRAY, [self.x, self.y], self.radio]

        # Direccion de movimiento de la pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

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

class RaquetaPong:
    def __init__(self):

        # --- Atributos de la clase ---

        # --- Dimensiones de la raqueta ---
        self.ancho = 30
        self.alto = 120

        # --- Posicion de la raqueta
        self.x = 0
        self.y = (WINDOW_VER / 2) - (self.alto / 2)

        # --- Direccion de movimiento de la raqueta ---
        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y

def main():
    # Inicialización de pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    window = pygame.display.set_mode((WINDOW_HOR, WINDOW_VER))
    pygame.display.set_caption('Pong')

    #instaciación
    pelota = PelotaPong(window)

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = WINDOW_HOR - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        window.fill(BLACK)
        pygame.draw.circle(window, WHITE, [pelota.x, pelota.y], pelota.radio)
        pygame.draw.rect(window, WHITE, [raqueta_1.x, raqueta_1.y, raqueta_1.ancho, raqueta_1.alto])
        pygame.draw.rect(window, WHITE, [raqueta_2.x, raqueta_2.y, raqueta_2.ancho, raqueta_2.alto])

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()