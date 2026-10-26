import random

from objects.circleshape import CircleShape

from utils.constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from utils.logger import log_event

class Asteroid(CircleShape):
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        degree = random.uniform(20,50)
        ast_1v = self.velocity.rotate(degree)
        ast_2v = self.velocity.rotate(-degree)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
        ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
        ast_1.velocity += ast_1v * 1.2
        ast_2.velocity += ast_2v * 1.2