class BitrateReader:
    def read(self, filename, source_codec):
        print(f"BitrateReader: {filename} 비트레이트 읽는 중...")
        return "비트레이트 데이터"

    def convert(self, buffer, destination_codec):
        print("BitrateReader: 비트레이트 변환 중...")
        return "변환된 비트레이트 데이터"


class AudioMixer:
    def fix(self, chunks):
        print("AudioMixer: 오디오 믹싱 중...")
        return "믹싱된 오디오"
