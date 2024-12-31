import random
import pygame

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def handle_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        return 'up'
    elif keys[pygame.K_DOWN]:
        return 'down'
    elif keys[pygame.K_LEFT]:
        return 'left'
    elif keys[pygame.K_RIGHT]:
        return 'right'
    elif keys[pygame.K_SPACE]:
        return 'interact'
    elif keys[pygame.K_RETURN]:
        return 'confirm'
    else:
        return None
