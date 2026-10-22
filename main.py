import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state



def main():

    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        screen.fill("black")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
