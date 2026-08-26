import sys
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0.0
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for sprite in asteroids:
            if sprite.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit(1)
        for sprite in asteroids:
            for shot in shots:
                if sprite.collides_with(shot):
                    log_event("asteroid_shot")
                    sprite.split()
                    shot.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000

if __name__ == "__main__":
    main()
