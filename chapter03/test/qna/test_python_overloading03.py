from multipledispatch import dispatch
import pytest

class Calculator:
    @dispatch(int, int)
    def add(self, data1, data2):
        return data1 + data2

    @dispatch(str, str)
    def add(self, data1, data2):
        return data1 + data2

def test_calc_valid():
    calc = Calculator()
    
    # 정상 케이스
    assert calc.add(1, 2) == 3
    assert calc.add("Hello, ", "World!") == "Hello, World!"

def test_calc_invalid():
    calc = Calculator()
    
    # 타입이 맞지 않는 경우 NotImplementedError 발생.
    # 기존 TypeError와는 달랐다는 점에 주의.
    # 다른 타입은 구현을 안해서 NotImplementedError인 것.
    with pytest.raises(NotImplementedError):
        calc.add(1, "2")  # int + str
    
    with pytest.raises(NotImplementedError):
        calc.add("1", 2)  # str + int
    
    with pytest.raises(NotImplementedError):
        calc.add(1, [1,2,3])  # int + list
