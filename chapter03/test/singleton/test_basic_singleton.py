class PrinterManager:
    """

    Notes.
        Python에서는:
            - private 접근 제어자가 없음 (단지 _나 __로 네이밍 컨벤션만 있음)
            - __new__를 private으로 만들 수 없음
            - 객체 생성을 완전히 제한할 수 없음
        따라서 Python에서는 주로:
            - 문서화를 통해 get_instance() 사용을 권장
            - _instance와 같이 언더스코어 prefix로 내부 사용 변수임을 표시
            - 코드 리뷰나 컨벤션을 통해 올바른 사용을 유도
    """

    _instance = None

    def __new__(cls):
        """PrinterManager 객체 생성 시 호출되는 매직 메소드"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.printer_queue = []  # 초기화
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            cls._instance.printer_queue = []  # 초기화
        return cls._instance


def test_printer_manager_singleton():
    # 첫 번째 인스턴스 생성
    manager1 = PrinterManager.get_instance()

    # 두 번째 인스턴스 생성
    manager2 = PrinterManager.get_instance()

    # 동일한 인스턴스인지 확인 (id 비교)
    assert manager1 is manager2

    # 직접 생성해도 같은 인스턴스인지 확인
    manager3 = PrinterManager()
    assert manager1 is manager3

    # 객체의 상태 변경이 모든 참조에 반영되는지 확인
    manager1.printer_queue.append("test_doc")
    assert manager2.printer_queue == ["test_doc"]
    assert manager3.printer_queue == ["test_doc"]

    # printer_queue가 동일한 리스트 객체를 참조하는지 확인
    assert id(manager1.printer_queue) == id(manager2.printer_queue)


def test_printer_manager_initialization():
    # 모든 인스턴스를 초기화
    PrinterManager._instance = None

    # 새로운 인스턴스 생성
    manager = PrinterManager.get_instance()

    # printer_queue가 빈 리스트로 초기화되었는지 확인
    assert isinstance(manager.printer_queue, list)
    assert len(manager.printer_queue) == 0


def test_multiple_operations():
    manager1 = PrinterManager.get_instance()
    manager2 = PrinterManager.get_instance()

    # manager1으로 작업 수행
    manager1.printer_queue.append("doc1")
    manager1.printer_queue.append("doc2")

    # manager2의 queue도 동일한지 확인
    assert manager2.printer_queue == ["doc1", "doc2"]

    # manager2로 작업 수행
    manager2.printer_queue.clear()

    # manager1의 queue도 비워졌는지 확인
    assert len(manager1.printer_queue) == 0
