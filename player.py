import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

#Player class that inherits from CircleShape class
class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # A player will look like a triangle, even though we'll use a circle to represent its hitbox.
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # override draw() method from CircleShape class
    def draw(self, screen) -> None:
        #Draws a polygon on the given surface
        #https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    # add PLAYER_TURN_SPEED * dt to player's current rotation
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    # player moving method
    # will modify player's position
    # this is the provided method
    # vector math
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # shoot method
    def shoot(self) -> None:
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0,1)
        rotated_vector = shot.velocity.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
        shot.velocity += rotated_with_speed_vector

    #
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # rotate left (A)
        if keys[pygame.K_a]:
            self.rotate(0-dt)
        # rotate right (D)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # move up (W)
        if keys[pygame.K_w]:
            self.move(dt)
        # move down (S)
        if keys[pygame.K_s]:
            self.move(0-dt)

        # player shoots (SPACE_BAR)
        if keys[pygame.K_SPACE]:
            self.shoot()





