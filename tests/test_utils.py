import unittest
from src.utils import generate_random_number, handle_input
import pygame

class TestUtils(unittest.TestCase):

    def test_generate_random_number(self):
        random_number = generate_random_number(1, 10)
        self.assertTrue(1 <= random_number <= 10)

    def test_handle_input_up(self):
        pygame.key.set_mods(0)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP))
        self.assertEqual(handle_input(), 'up')

    def test_handle_input_down(self):
        pygame.key.set_mods(0)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
        self.assertEqual(handle_input(), 'down')

    def test_handle_input_left(self):
        pygame.key.set_mods(0)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.assertEqual(handle_input(), 'left')

    def test_handle_input_right(self):
        pygame.key.set_mods(0)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        self.assertEqual(handle_input(), 'right')

    def test_handle_input_interact(self):
        pygame.key.set_mods(0)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.assertEqual(handle_input(), 'interact')

    def test_handle_input_confirm(self):
        pygame.key.set_mods(0)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
        self.assertEqual(handle_input(), 'confirm')

if __name__ == '__main__':
    unittest.main()
