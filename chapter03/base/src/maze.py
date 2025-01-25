class Maze:
    def __init__(self):
        self._rooms = {}
    
    def add_room(self, room):
        self._rooms[room._room_number] = room
    
    def room_no(self, room_number):
        return self._rooms.get(room_number)
