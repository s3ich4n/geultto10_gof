import json
from datetime import datetime
from unittest.mock import patch

import pytest
from freezegun import freeze_time

from .mixin_example02 import (
    UserAccount,
    Product,
    GameCharacter,
)


# Fixtures
@pytest.fixture
def user_account():
    return UserAccount("test_user", "test@example.com")


@pytest.fixture
def product():
    return Product("Test Product", 99.99, 10)


@pytest.fixture
def game_character():
    return GameCharacter("Test Hero", level=1, health=100)


# LoggerMixin Tests
class TestLoggerMixin:
    @patch("builtins.print")
    def test_log_format(self, mock_print):
        with freeze_time("2024-02-22 10:00:00"):
            user = UserAccount("test_user", "test@example.com")
            expected_log = "[INFO] 2024-02-22 10:00:00 - UserAccount: New account created for test_user"
            mock_print.assert_called_with(expected_log)

    @patch("builtins.print")
    def test_log_levels(self, mock_print):
        user = UserAccount("test_user", "test@example.com")
        mock_print.reset_mock()  # 생성자의 로그를 초기화

        user.log("Test message", "WARNING")
        mock_print.assert_called_once()
        call_args = mock_print.call_args[0][0]
        assert "[WARNING]" in call_args
        assert "UserAccount: Test message" in call_args


# SerializerMixin Tests
class TestSerializerMixin:
    def test_to_dict(self, product):
        expected_dict = {"name": "Test Product", "price": 99.99, "stock": 10}
        assert product.to_dict() == expected_dict

    def test_to_json(self, product):
        json_data = product.to_json()
        assert isinstance(json_data, str)

        # JSON이 파싱 가능한지 확인
        parsed_data = json.loads(json_data)
        assert parsed_data["name"] == "Test Product"
        assert parsed_data["price"] == 99.99
        assert parsed_data["stock"] == 10


# GameStateMixin Tests
class TestGameStateMixin:
    def test_save_state(self, game_character):
        state = game_character.save_state()

        assert "timestamp" in state
        assert state["class_name"] == "GameCharacter"
        assert state["state"]["name"] == "Test Hero"
        assert state["state"]["level"] == 1
        assert state["state"]["health"] == 100

    def test_load_state(self, game_character):
        # 상태 변경 전 저장
        initial_state = game_character.save_state()

        # 상태 변경
        game_character.health = 50
        game_character.level = 2

        # 이전 상태 복원
        game_character.load_state(initial_state)

        assert game_character.health == 100
        assert game_character.level == 1

    def test_load_state_invalid_class(self, game_character):
        invalid_state = {
            "timestamp": datetime.now().isoformat(),
            "class_name": "InvalidClass",
            "state": {},
        }

        with pytest.raises(ValueError, match="Invalid state for this class"):
            game_character.load_state(invalid_state)


# Integration Tests
class TestMixinIntegration:
    @patch("builtins.print")
    def test_character_damage_logging(self, mock_print, game_character):
        game_character.take_damage(30)

        # 로그 확인
        log_call = mock_print.call_args[0][0]
        assert "Took 30 damage" in log_call
        assert "Health: 100 -> 70" in log_call

    def test_character_state_serialization(self, game_character):
        # 데미지 적용
        game_character.take_damage(30)

        # 상태 저장
        state = game_character.save_state()

        # 직렬화된 상태 확인
        assert state["state"]["health"] == 70

        # JSON 직렬화 테스트
        json_data = game_character.to_json()
        parsed_data = json.loads(json_data)
        assert parsed_data["health"] == 70
