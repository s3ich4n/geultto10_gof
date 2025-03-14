# MRO 분석을 위한 코드
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {self.__class__.__name__}: {message}")


class SerializerMixin:
    def serialize(self):
        return {
            attr: getattr(self, attr)
            for attr in self.__dict__
            if not attr.startswith("_")
        }


class GameStateMixin:
    def save_state(self):
        self.log("Saving state...")
        return {"state": self.serialize()}


class Door(LoggerMixin, SerializerMixin, GameStateMixin):
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2
        self.is_open = False


# MRO 출력
print("Method Resolution Order for Door:")
for cls in Door.__mro__:
    print(f"  -> {cls.__name__}")
