import random
from pygame.image import load
from pygame.math import Vector2

def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

def load_sprite(name, with_alpha=True):

    path = f"Assets/Sprites/{name}.png"

    loaded_sprite = load(path)


    if with_alpha:

        return loaded_sprite.convert_alpha()

    else:

        return loaded_sprite.convert()