from typing import Protocol


class Device(Protocol):
    """ "장비"를 의미하는 Implementor"""

    MAX_VOLUME: int
    MIN_VOLUME: int

    MIN_CHANNEL: int
    MAX_CHANNEL: int

    VOLUME_SCALE: int
    CHANNEL_SCALE: int

    def is_enabled(self) -> bool: ...

    def enable(self) -> None: ...

    def disable(self) -> None: ...


class TV(Device):
    """ "TV"를 의미하는 ConcreteImplementor

    Notes:
        객체를 생성하면 볼륨은 0, 채널은 0, 꺼진 상태.

    """

    MIN_VOLUME = 0
    MAX_VOLUME = 100

    MIN_CHANNEL = 1
    MAX_CHANNEL = 99

    VOLUME_SCALE = 10  # 볼륨은 10 단위로 증가 (최대 100)
    CHANNEL_SCALE = 1  # 채널은 10 단위로 증가 (최대 99)

    def __init__(self):
        self._enabled: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL

    @property
    def volume(self):
        return self._volume

    @property
    def channel(self):
        return self._channel

    def mute(self):
        self._volume = 0

    def volume_down(self):
        """Scaling Factor를 Device 내부에서 적용 (세부 구현 변경)"""
        self._volume = max(self._volume - self.VOLUME_SCALE, self.MIN_VOLUME)

    def volume_up(self):
        """Scaling Factor를 Device 내부에서 적용 (세부 구현 변경)"""
        self._volume = min(self._volume + self.VOLUME_SCALE, self.MAX_VOLUME)

    def channel_down(self):
        """Scaling Factor를 Device 내부에서 적용 (세부 구현 변경)"""
        self._channel = max(self._channel - self.CHANNEL_SCALE, self.MIN_CHANNEL)

    def channel_up(self):
        """Scaling Factor를 Device 내부에서 적용 (세부 구현 변경)"""
        self._channel = min(self._channel + self.CHANNEL_SCALE, self.MAX_CHANNEL)

    @property
    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False


class Radio(Device):
    """라디오를 의미하는 ConcreteImplementor"""

    MIN_VOLUME = 0
    MAX_VOLUME = 10

    MIN_CHANNEL = 1000
    MAX_CHANNEL = 9900

    VOLUME_SCALE = 1  # 볼륨은 1 단위로 증가 (최대 10)
    CHANNEL_SCALE = 10  # 채널은 10 단위로 증가 (최대 9900)

    def __init__(self):
        self._enabled = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    @property
    def volume(self):
        return self._volume

    @property
    def channel(self):
        return self._channel

    def mute(self):
        self._volume = 0

    def volume_down(self):
        """Scaling Factor를 Device 내부에서 적용 (세부 구현 변경)"""
        self._volume = max(self._volume - self.VOLUME_SCALE, self.MIN_VOLUME)

    def volume_up(self):
        """Scaling Factor를 Device 내부에서 적용 (세부 구현 변경)"""
        self._volume = min(self._volume + self.VOLUME_SCALE, self.MAX_VOLUME)

    def channel_down(self):
        """Scaling Factor를 Device 내부에서 적용 (세부 구현 변경)"""
        self._channel = max(self._channel - self.CHANNEL_SCALE, self.MIN_CHANNEL)

    def channel_up(self):
        """Scaling Factor를 Device 내부에서 적용 (세부 구현 변경)"""
        self._channel = min(self._channel + self.CHANNEL_SCALE, self.MAX_CHANNEL)

    @property
    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False
