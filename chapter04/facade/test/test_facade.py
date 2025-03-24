from chapter04.facade.src.converter import VideoConverter


def test_video_coverter():
    # 컨버터를 만들고
    converter = VideoConverter()

    # 명령만 내리면
    mp4 = converter.convert("test.ogg", "mp4")

    # 파일이 나온다.
    mp4.save()
