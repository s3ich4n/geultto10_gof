from src.door import Door


class EnchantedDoor(Door):
    def enter(self):
        if self._is_open:
            print("마법의 문을 통과")
        else:
            print("마법의 문이 닫혀있음!")
