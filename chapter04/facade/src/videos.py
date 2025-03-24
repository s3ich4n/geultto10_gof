class VideoFile:
    def __init__(self, filename):
        self.filename = filename
        print(f"VideoFile: {filename} 파일 생성")

    def save(self):
        print(f"VideoFile: {self.filename} 저장 완료")
