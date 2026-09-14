import pygame
import sys 
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state, log_event
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver} Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH/ 2, y = SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers =(updatable)
    asteroidfield = AsteroidField()

    #Starting Game Loop
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if CircleShape.collides_with(player, asteroid) is True:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
