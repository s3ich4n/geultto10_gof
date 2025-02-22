import pytest
from src.device import (
    Radio,
    TV,
)
from src.remote_control import AdvancedRemoteControl


class TestDeviceWithAdvancedRemoteControl:
    @pytest.fixture
    def radio(self):
        return Radio()

    @pytest.fixture
    def tv(self):
        return TV()

    @pytest.fixture
    def radio_remote_control(self, radio):
        radio_with_remote_control = AdvancedRemoteControl(device=radio)

        return radio_with_remote_control

    @pytest.fixture
    def tv_remote_control(self, tv):
        tv_with_remote_control = AdvancedRemoteControl(device=tv)

        return tv_with_remote_control

    def test_tv_mute(self, tv, tv_remote_control):
        # 볼륨 줄이기
        tv_remote_control.volume_up()
        tv_remote_control.volume_up()
        tv_remote_control.volume_up()
        tv_remote_control.volume_up()

        tv_remote_control.mute()
        assert tv.volume == 0

    def test_radio_mute(self, radio, radio_remote_control):
        # 볼륨 줄이기
        radio_remote_control.volume_up()
        radio_remote_control.volume_up()
        radio_remote_control.volume_up()
        radio_remote_control.volume_up()

        radio_remote_control.mute()
        assert radio.volume == 0
