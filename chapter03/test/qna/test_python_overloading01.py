import pytest

class Calculator:
    def add(self, a, b):
        return a + b
    
    # 같은 이름으로 다른 메소드 정의 시도
    def add(self, a, b, c):  # 이전 add 메소드를 덮어씌움
        return a + b + c

def test_method_overloading():
    calc = Calculator()
    
    # 두 개의 인자를 받는 add는 이미 덮어씌워졌으므로 
    # TypeError가 발생해야 함
    with pytest.raises(TypeError) as exc_info:
        result = calc.add(1, 2)
    
    # 에러 메시지 검증
    assert "add() missing 1 required positional argument" in str(exc_info.value)
    
    # 세 개의 인자를 받는 add는 정상 작동
    assert calc.add(1, 2, 3) == 6

def test_method_signature():
    # Calculator 클래스의 add 메소드가 하나만 존재하는지 확인
    methods = [method for method in dir(Calculator) if method == "add"]
    assert len(methods) == 1
