from utils.constants import SHOT_RADIUS

from objects.circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x,y, SHOT_RADIUS)

