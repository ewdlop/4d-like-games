import unittest
from src.map import Tile, Room, Map

class TestTile(unittest.TestCase):
    def test_tile_initialization(self):
        tile = Tile(True, False)
        self.assertTrue(tile.walkable)
        self.assertFalse(tile.transparent)

class TestRoom(unittest.TestCase):
    def test_room_initialization(self):
        room = Room(1, 2, 3, 4)
        self.assertEqual(room.x, 1)
        self.assertEqual(room.y, 2)
        self.assertEqual(room.width, 3)
        self.assertEqual(room.height, 4)

    def test_room_center(self):
        room = Room(1, 2, 3, 4)
        self.assertEqual(room.center(), (2, 4))

    def test_room_intersect(self):
        room1 = Room(1, 2, 3, 4)
        room2 = Room(2, 3, 3, 4)
        room3 = Room(5, 6, 3, 4)
        self.assertTrue(room1.intersect(room2))
        self.assertFalse(room1.intersect(room3))

class TestMap(unittest.TestCase):
    def setUp(self):
        self.map = Map(10, 10)

    def test_map_initialization(self):
        self.assertEqual(self.map.width, 10)
        self.assertEqual(self.map.height, 10)
        self.assertEqual(len(self.map.tiles), 10)
        self.assertEqual(len(self.map.tiles[0]), 10)

    def test_create_room(self):
        room = Room(1, 1, 3, 3)
        self.map.create_room(room)
        for x in range(1, 4):
            for y in range(1, 4):
                self.assertTrue(self.map.tiles[x][y].walkable)

    def test_create_h_tunnel(self):
        self.map.create_h_tunnel(1, 3, 5)
        for x in range(1, 4):
            self.assertTrue(self.map.tiles[x][5].walkable)

    def test_create_v_tunnel(self):
        self.map.create_v_tunnel(1, 3, 5)
        for y in range(1, 4):
            self.assertTrue(self.map.tiles[5][y].walkable)

    def test_generate_map(self):
        self.map.generate_map(5, 2, 4, 10, 10)
        walkable_tiles = sum(tile.walkable for row in self.map.tiles for tile in row)
        self.assertGreater(walkable_tiles, 0)

if __name__ == "__main__":
    unittest.main()
