import pytest

from src.device import Radio
from src.remote_control import RemoteControl


class TestRadioWithRemoteControl:
    @pytest.fixture
    def radio(self):
        return Radio()

    @pytest.fixture
    def remote_control(self, radio):
        radio_with_remote_control = RemoteControl(device=radio)

        return radio_with_remote_control

    def test_radio_turn_on(self, radio, remote_control):
        # 켜기
        remote_control.toggle_power()
        assert radio.is_enabled is True

    def test_radio_turn_off(self, radio, remote_control):
        # 껐다켜기
        remote_control.toggle_power()
        remote_control.toggle_power()
        assert radio.is_enabled is False

    # 볼륨 관련 테스트 (ids 사용)
    @pytest.mark.parametrize(
        "actions, expected",
        [
            (["volume_up"], 1),
            (["volume_up", "volume_down"], 0),
            (["volume_down"], 0),
            (["volume_up"] * 101, 10),
        ],
        ids=[
            "volume_up_once",  # 볼륨 1번 올리기
            "volume_up_then_down",  # 볼륨 올리고 내리기
            "volume_down_minimum_value_0",  # 최소값 확인
            "volume_up_maximum_value_10",  # 최대값 확인
        ],
    )
    def test_radio_volume(self, radio, remote_control, actions, expected):
        for action in actions:
            getattr(remote_control, action)()
        assert radio.volume == expected

    # 채널 관련 테스트 (ids 사용)
    @pytest.mark.parametrize(
        "actions, expected",
        [
            (["channel_up"], 1010),
            (["channel_up", "channel_down"], 1000),
            (["channel_down"], 1000),
            (["channel_up"] * 990, 9900),
        ],
        ids=[
            "channel_up_once",  # 채널 1번 올리기
            "channel_up_then_down",  # 채널 올리고 내리기
            "channel_down_minimum_value_1000",  # 최소값 확인
            "channel_up_maximum_value_9900",  # 최대값 확인
        ],
    )
    def test_radio_channel(self, radio, remote_control, actions, expected):
        for action in actions:
            getattr(remote_control, action)()
        assert radio.channel == expected
