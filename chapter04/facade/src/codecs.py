class OggCompressionCodec:
    def __init__(self):
        print("OggCompressionCodec 초기화")

    def compress(self, video_file):
        print(f"OggCompressionCodec: {video_file.filename} 압축 중...")
        return "압축된 Ogg 데이터"


class Mpeg4CompressionCodec:
    def __init__(self):
        print("Mpeg4CompressionCodec 초기화")

    def compress(self, video_file):
        print(f"Mpeg4CompressionCodec: {video_file.filename} 압축 중...")
        return "압축된 MPEG4 데이터"
