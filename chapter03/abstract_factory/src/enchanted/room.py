from .spell import Spell    # circular import issue resolved
from src.room import Room


class EnchantedRoom(Room):
    def __init__(self, room_no, spell: Spell):
        super().__init__(room_no)
        self.spell = spell

    def enter(self):
        print(f"마법의 방에 들어옴 (마법 수치: {self.spell.power})")
