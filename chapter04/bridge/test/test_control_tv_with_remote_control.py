import pytest

from src.device import TV
from src.remote_control import RemoteControl


class TestTvWithRemoteControl:
    @pytest.fixture
    def tv(self):
        return TV()

    @pytest.fixture
    def remote_control(self, tv):
        tv_with_remote_control = RemoteControl(device=tv)

        return tv_with_remote_control

    def test_tv_turn_on(self, tv, remote_control):
        # 켜기
        remote_control.toggle_power()
        assert tv.is_enabled is True

    def test_tv_turn_off(self, tv, remote_control):
        # 껐다켜기
        remote_control.toggle_power()
        remote_control.toggle_power()
        assert tv.is_enabled is False

    def test_tv_volume_up(self, tv, remote_control):
        # 볼륨 줄이기
        remote_control.volume_up()
        assert tv.volume == 10

    def test_tv_volume_down(self, tv, remote_control):
        # 볼륨 늘리기
        remote_control.volume_up()
        remote_control.volume_down()
        assert tv.volume == 0

    def test_tv_volume_minimum_value_is_0(self, tv, remote_control):
        # 볼륨 최소값은 0
        remote_control.volume_down()
        assert tv.volume == 0

    def test_tv_volume_maximum_value_is_100(self, tv, remote_control):
        # 볼륨 최대값은 100
        for _ in range(11):
            remote_control.volume_up()
        assert tv.volume == 100

    def test_tv_channel_up(self, tv, remote_control):
        # 채널 올리기
        remote_control.channel_up()
        assert tv.channel == 2

    def test_tv_channel_down(self, tv, remote_control):
        # 채널 올리기
        remote_control.channel_up()
        remote_control.channel_down()
        assert tv.channel == 1

    def test_tv_channel_minimum_value_is_1(self, tv, remote_control):
        remote_control.channel_down()
        assert tv.channel == 1

    def test_tv_channel_maximum_value_is_99(self, tv, remote_control):
        for _ in range(99):
            remote_control.channel_up()
        assert tv.channel == 99
