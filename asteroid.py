import pygame.draw
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    # constructor
    def __ini__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # override draw() method from CircleShape class
    def draw(self, screen) -> None:
        # draws a circle on the given surface
        # https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    # override update() method from CircleShape class
    # moves at a constant speed in a straight line
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
