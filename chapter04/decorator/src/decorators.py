from chapter04.decorator.src.components import TextComponent


# Decorator 추상 클래스
class TextDecorator(TextComponent):
    def __init__(self, text_component):
        self.text_component = text_component

    def draw(self):
        self.text_component.draw()

    def get_text(self):
        return self.text_component.get_text()


# ConcreteDecorator 클래스 - 볼드 텍스트
class BoldDecorator(TextDecorator):
    def draw(self):
        print("Bold: ", end="")
        super().draw()

    def get_text(self):
        return f"<b>{super().get_text()}</b>"


# ConcreteDecorator 클래스 - 이탤릭 텍스트
class ItalicDecorator(TextDecorator):
    def draw(self):
        print("Italic: ", end="")
        super().draw()

    def get_text(self):
        return f"<i>{super().get_text()}</i>"
