from src.device import Device


class RemoteControl:
    """ "제어"의 큰 개념의 Abstraction.

    큰 개념에서 정의한 안정적인 인터페이스를 균일하게 제공하는 것이 핵심이다.

    """

    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled:
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self):
        self._device.volume_down()

    def volume_up(self):
        self._device.volume_up()

    def channel_down(self):
        self._device.channel_down()

    def channel_up(self):
        self._device.channel_up()


class AdvancedRemoteControl(RemoteControl):
    """추가 제어에 대한 RefinedAbstraction."""

    def mute(self):
        self._device.mute()
