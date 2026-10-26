import pygame

from objects.circleshape import CircleShape
from utils.constants import LINE_WIDTH

class Asteroid(CircleShape):
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt