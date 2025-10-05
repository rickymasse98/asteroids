# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        
        # Limit FPS to 60 and get delta time in seconds
        dt = (clock.tick(60))/1000  # seconds

if __name__ == "__main__":
    main()
