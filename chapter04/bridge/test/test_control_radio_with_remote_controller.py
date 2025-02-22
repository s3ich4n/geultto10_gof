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

    def test_radio_volume_up(self, radio, remote_control):
        # 볼륨 줄이기
        remote_control.volume_up()
        assert radio.volume == 1

    def test_radio_volume_down(self, radio, remote_control):
        # 볼륨 늘리기
        remote_control.volume_up()
        remote_control.volume_down()
        assert radio.volume == 0

    def test_radio_volume_minimum_value_is_0(self, radio, remote_control):
        # 볼륨 최소값은 0
        remote_control.volume_down()
        assert radio.volume == 0

    def test_radio_volume_maximum_value_is_10(self, radio, remote_control):
        # 볼륨 최대값은 10
        for _ in range(11):
            remote_control.volume_up()
        assert radio.volume == 10

    def test_radio_channel_up(self, radio, remote_control):
        # 채널 올리기
        remote_control.channel_up()
        assert radio.channel == 1010

    def test_radio_channel_down(self, radio, remote_control):
        # 채널 올리기
        remote_control.channel_up()
        remote_control.channel_down()
        assert radio.channel == 1000

    def test_radio_channel_minimum_value_is_1000(self, radio, remote_control):
        remote_control.channel_down()
        assert radio.channel == 1000

    def test_radio_channel_maximum_value_is_9900(self, radio, remote_control):
        for _ in range(990):
            remote_control.channel_up()
        assert radio.channel == 9900
