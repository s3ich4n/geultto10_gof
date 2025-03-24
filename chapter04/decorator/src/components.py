from abc import (
    ABC,
    abstractmethod,
)


# Component 인터페이스
class TextComponent(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_text(self):
        pass


# ConcreteComponent 클래스
class SimpleTextComponent(TextComponent):
    def __init__(self, text):
        self.text = text

    def draw(self):
        print(f"Drawing: {self.text}")

    def get_text(self):
        return self.text
