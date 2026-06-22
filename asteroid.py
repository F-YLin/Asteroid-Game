import pygame.draw
from circleshape import CircleShape
from constants import *
from logger import *
import random



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

    # split() method to split asteroids when shots hit
    def split(self) -> None:
        self.kill()   # this particular asteroid is always killed, it splits into new smaller ones

        if self.radius < ASTEROID_MIN_RADIUS: # if too small, do not split
            return None

        # if large enough, split
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        smaller_asteroid1_vector = self.velocity.rotate(random_angle)      # for 1st asteroid, some random angle
        smaller_asteroid2_vector = self.velocity.rotate(0 - random_angle)  # for 2ed asteroid, negative angle
        new_radius  = self.radius - ASTEROID_MIN_RADIUS
        smaller_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid1.velocity = smaller_asteroid1_vector * 1.2
        smaller_asteroid2.velocity = smaller_asteroid2_vector * 1.2







