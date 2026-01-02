import sys
import pygame # type: ignore
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        player.timer -= dt

        screen.fill("black")

        for i in asteroids:
            if i.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        
        for a in asteroids:
            for i in shots:
                if a.collides_with(i):
                    log_event("asteroid_shot")
                    a.split()
                    pygame.sprite.Sprite.kill(i)

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()