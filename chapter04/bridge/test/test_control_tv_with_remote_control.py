import pytest

from src.device import TV
from src.remote_control import RemoteControl


class TestTvWithRemoteControl:
    @pytest.fixture
    def tv(self):
        return TV()

    @pytest.fixture
    def remote_control(self, tv):
        return RemoteControl(device=tv)

    # 전원 관련 테스트
    def test_tv_turn_on(self, tv, remote_control):
        remote_control.toggle_power()
        assert tv.is_enabled is True

    def test_tv_turn_off(self, tv, remote_control):
        remote_control.toggle_power()
        remote_control.toggle_power()
        assert tv.is_enabled is False

    # 볼륨 관련 테스트 (ids 사용)
    @pytest.mark.parametrize(
        "actions, expected",
        [
            (["volume_up"], 10),  # 볼륨 1번 올리기
            (["volume_up", "volume_down"], 0),  # 볼륨 올리고 내리기
            (["volume_down"], 0),  # 최소값은 0
            (["volume_up"] * 11, 100),  # 최대값은 100 (10씩 증가, 11번 호출)
        ],
        ids=[
            "volume_up_once",
            "volume_up_then_down",
            "volume_down_minimum_value_0",
            "volume_up_maximum_value_100",
        ],
    )
    def test_tv_volume(self, tv, remote_control, actions, expected):
        for action in actions:
            getattr(remote_control, action)()
        assert tv.volume == expected

    # 채널 관련 테스트 (ids 사용)
    @pytest.mark.parametrize(
        "actions, expected",
        [
            (["channel_up"], 2),  # 채널 1번 올리기
            (["channel_up", "channel_down"], 1),  # 채널 올리고 내리기
            (["channel_down"], 1),  # 최소값은 1
            (["channel_up"] * 99, 99),  # 최대값은 99
        ],
        ids=[
            "channel_up_once",
            "channel_up_then_down",
            "channel_down_minimum_value_1",
            "channel_up_maximum_value_99",
        ],
    )
    def test_tv_channel(self, tv, remote_control, actions, expected):
        for action in actions:
            getattr(remote_control, action)()
        assert tv.channel == expected
