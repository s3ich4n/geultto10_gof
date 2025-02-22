"""
이 테스트들은 다음을 검증합니다:

- LoggerMixin의 로그 형식과 레벨
- SerializerMixin의 직렬화 기능
- GameStateMixin의 상태 저장/복원 기능
- 세 믹스인이 함께 사용될 때의 통합 동작
"""

import json
from datetime import datetime
from typing import (
    Dict,
    Any,
)


# 1. LoggerMixin 예시
class LoggerMixin:
    def log(self, message: str, level: str = "INFO") -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{level}] {timestamp} - {self.__class__.__name__}: {message}")


class UserAccount(LoggerMixin):
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.log(f"New account created for {username}")

    def change_email(self, new_email: str) -> None:
        old_email = self.email
        self.email = new_email
        self.log(f"Email changed from {old_email} to {new_email}", "WARNING")


# 2. SerializerMixin 예시
class SerializerMixin:
    def to_dict(self) -> Dict[str, Any]:
        return {
            attr: getattr(self, attr)
            for attr in self.__dict__
            if not attr.startswith("_")
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


class Product(SerializerMixin):
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock


# 3. GameStateMixin 예시
class GameStateMixin:
    def save_state(self) -> Dict[str, Any]:
        if not hasattr(self, "to_dict"):
            raise NotImplementedError("Class must implement to_dict method")
        return {
            "timestamp": datetime.now().isoformat(),
            "class_name": self.__class__.__name__,
            "state": self.to_dict(),
        }

    def load_state(self, state: Dict[str, Any]) -> None:
        if state["class_name"] != self.__class__.__name__:
            raise ValueError("Invalid state for this class")
        for key, value in state["state"].items():
            setattr(self, key, value)


class GameCharacter(SerializerMixin, GameStateMixin, LoggerMixin):
    def __init__(self, name: str, level: int = 1, health: int = 100):
        self.name = name
        self.level = level
        self.health = health
        self.log(f"Character {name} created at level {level}")

    def take_damage(self, damage: int) -> None:
        old_health = self.health
        self.health = max(0, self.health - damage)
        self.log(f"Took {damage} damage. Health: {old_health} -> {self.health}")


def main():
    # LoggerMixin 테스트
    print("\n=== LoggerMixin Test ===")
    user = UserAccount("john_doe", "john@example.com")
    user.change_email("john.doe@newdomain.com")

    # SerializerMixin 테스트
    print("\n=== SerializerMixin Test ===")
    product = Product("Gaming Laptop", 1299.99, 10)
    print("Product as JSON:")
    print(product.to_json())

    # GameStateMixin 테스트 (SerializerMixin, LoggerMixin과 결합)
    print("\n=== GameStateMixin Test ===")
    character = GameCharacter("Hero", level=5, health=100)

    # 상태 저장
    initial_state = character.save_state()
    print("\nInitial state saved:", json.dumps(initial_state, indent=2))

    # 캐릭터 상태 변경
    character.take_damage(30)
    print("\nAfter taking damage:")
    print(character.to_json())

    # 이전 상태 복원
    print("\nRestoring to initial state...")
    character.load_state(initial_state)
    print("After state restored:")
    print(character.to_json())


if __name__ == "__main__":
    main()
