class Tile:
    def __init__(self, walkable, transparent):
        self.walkable = walkable
        self.transparent = transparent

class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def center(self):
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        return (center_x, center_y)

    def intersect(self, other):
        return (self.x <= other.x + other.width and
                self.x + self.width >= other.x and
                self.y <= other.y + other.height and
                self.y + self.height >= other.y)

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True, True) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def create_room(self, room):
        for x in range(room.x, room.x + room.width):
            for y in range(room.y, room.y + room.height):
                self.tiles[x][y] = Tile(True, True)

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y] = Tile(True, True)

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y] = Tile(True, True)

    def generate_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height):
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            w = random.randint(room_min_size, room_max_size)
            h = random.randint(room_min_size, room_max_size)
            x = random.randint(0, map_width - w - 1)
            y = random.randint(0, map_height - h - 1)

            new_room = Room(x, y, w, h)

            if num_rooms == 0:
                self.create_room(new_room)
            else:
                for other_room in rooms:
                    if new_room.intersect(other_room):
                        break
                else:
                    self.create_room(new_room)
                    (new_x, new_y) = new_room.center()
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()

                    if random.randint(0, 1) == 1:
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

            rooms.append(new_room)
            num_rooms += 1

    def display_map(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles[x][y].walkable:
                    print('.', end='')
                else:
                    print('#', end='')
            print()
