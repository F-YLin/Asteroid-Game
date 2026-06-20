import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # creating a group to hold objects for asteroids
    asteroids = pygame.sprite.Group()
    # creating a group to hold objects that could be updated
    updatable = pygame.sprite.Group()
    # creating a group to hold objects that could be drawn
    drawable = pygame.sprite.Group()

    # Player here is the name of the class, not an instance
    # this will add future Player instances into one of the two different groups
    Player.containers = (updatable, drawable)
    # do the same for Asteroid class, ensure each of its instance automatically add to these groups upon creation
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    player_1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    clock =  pygame.time.Clock()
    dt = 0.0 		#store decimal number of seconds

   # the main game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return

        screen.fill("black")

        # used to call instance with draw method. Now call draw on each drawable by looping through the group "drawable
        # player_1.draw(screen)
        for thing in drawable:
            thing.draw(screen)

        # used to call instance with update method. Now call update() on groups
        # player_1.update(dt)
        updatable.update(dt)

        pygame.display.flip()


        # at the end of each iteration of the game loop
        # call .tick() method on the clock object, passing 60 and save the return value divided by 1000 into dt
        # the .tick() method returns the amount of time that passed since the last time it was called, the delta time
        dt = clock.tick(60)/1000

        # print out dt to for testing purpose
        # print(dt)

        # Print-out for testing purposes
        #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
        #print(f"Screen width: {SCREEN_WIDTH}")
        #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
