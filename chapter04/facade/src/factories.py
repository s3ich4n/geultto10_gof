from chapter04.facade.src.codecs import (
    OggCompressionCodec,
    Mpeg4CompressionCodec,
)


class CodecFactory:
    def extract(self, file):
        filename = file.filename
        print(f"CodecFactory: 파일 형식 분석 중: {filename}")

        if filename.endswith(".ogg"):
            print("CodecFactory: Ogg 포맷 감지됨")
            return OggCompressionCodec()
        elif filename.endswith(".mp4"):
            print("CodecFactory: MP4 포맷 감지됨")
            return Mpeg4CompressionCodec()
        else:
            print(f"CodecFactory: 알 수 없는 형식: {filename}")
            # 기본값으로 MP4 코덱 반환
            return Mpeg4CompressionCodec()

    def create_codec(self, format_type):
        print(f"CodecFactory: {format_type} 코덱 생성 중...")
        if format_type == "mp4":
            return Mpeg4CompressionCodec()
        elif format_type == "ogg":
            return OggCompressionCodec()
        else:
            print(f"CodecFactory: 지원하지 않는 형식: {format_type}")
            return None
