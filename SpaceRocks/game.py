# https://itch.io/game-assets/free/tag-space

import pygame

from models import GameObject
from utils import load_sprite
from models import Asteroid, Spaceship


class SpaceRocks:

    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()

        self.asteroids = [Asteroid((0, 0)) for _ in range(6)]
        self.spaceship = Spaceship((400, 300))


    def main_loop(self):

        while True:

            self._handle_input()

            self._process_game_logic()

            self._draw()


    def _init_pygame(self):

        pygame.init()

        pygame.display.set_caption("Space Rocks")


    def _handle_input(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT or (

                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

            ):

                quit()
        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_d]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_a]:
            self.spaceship.rotate(clockwise=False)
        if is_key_pressed[pygame.K_SPACE]:
            self.spaceship.brake()
        elif is_key_pressed[pygame.K_w]:
            self.spaceship.accelerate()
        elif is_key_pressed[pygame.K_s]:
            self.spaceship.reverse_accelerate()


    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)


    def _draw(self):
        self.screen.blit(self.background, (0, 0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)


    def _get_game_objects(self):
        return [*self.asteroids, self.spaceship]


