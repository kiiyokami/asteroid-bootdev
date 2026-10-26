import pygame

from utils.constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        
        # off-screen objects never come back; drop them so groups don't grow forever
        m = ASTEROID_MAX_RADIUS
        if not (-m <= self.position.x <= SCREEN_WIDTH + m and -m <= self.position.y <= SCREEN_HEIGHT + m):
            self.kill()

    def collides_with(self, other) -> bool:
        return self.position.distance_to(other.position) <= (self.radius + other.radius)