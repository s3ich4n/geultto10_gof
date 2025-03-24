from chapter04.facade.src.factories import CodecFactory
from chapter04.facade.src.readers import (
    BitrateReader,
    AudioMixer,
)
from chapter04.facade.src.videos import VideoFile


class VideoConverter:
    def __init__(self):
        self.codec = CodecFactory()
        self.bitrate_reader = BitrateReader()
        self.audio_mixer = AudioMixer()

    def convert(self, filename, format_to_convert):
        file = VideoFile(filename)
        print(
            f"VideoConverter: 변환 시작 - {filename}를 {format_to_convert} 형식으로 변환"
        )

        # 비디오 파일 생성
        file = VideoFile(filename)

        # 소스 코덱 추출
        source_codec = self.codec.extract(file)

        # 대상 코덱 생성
        destination_codec = self.codec.create_codec(format_to_convert)

        # 비트레이트 읽기 및 변환
        buffer = self.bitrate_reader.read(filename, source_codec)
        result = self.bitrate_reader.convert(buffer, destination_codec)

        # 결과 처리
        result = self.audio_mixer.fix(result)

        print(
            f"VideoConverter: 변환 완료 - {filename}를 {format_to_convert} 형식으로 변환"
        )

        # 변환된 파일을 새 VideoFile 객체로 반환
        new_filename = filename.split(".")[0] + "." + format_to_convert
        converted_file = VideoFile(new_filename)
        return converted_file
