import pygame
import sys
from player import Player
from asteroid import Asteroid
from constants import *
from asteroidfield import *
from game_objects import *

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, shots)
    updatable.add(player)
    drawable.add(player)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        screen.fill((0, 0, 0))  
        
        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000   

    pygame.quit()  
    sys.exit()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()