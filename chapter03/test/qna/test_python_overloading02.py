from functools import singledispatchmethod

import pytest

class Calculator:
    @singledispatchmethod
    def add(self, data1, data2):
        raise NotImplementedError("Cannot process data of unknown type!")
    
    # 그마저도 한 타입만 체크. 그래서 이름이 `single dispatch`
    @add.register(int)
    def _(self, data1, data2):
        return data1 + data2

    @add.register(str)
    def _(self, data1, data2):
        return data1 + data2


def test_calc_int():
    calc = Calculator()

    result = calc.add(1, 2)

    assert result == 3


def test_calc_str():
    calc = Calculator()

    result = calc.add("1", "2")

    assert result == "12"


def test_single_dispatch_limitation():
    calc = Calculator()
    
    # 런타임에 뭐가 들어올 지 몰라서, 일단 연산을 시키기 때문에 에러가 날 수 있음
    with pytest.raises(TypeError):
        calc.add(1, "2")  # int + str는 불가능. 그걸 TypeError로 잡음
    
    with pytest.raises(TypeError):
        calc.add("1", 2)  # str + int도 불가능. 그걸 TypeError로 잡음
    
    with pytest.raises(TypeError):
        calc.add(1, [1,2,3])  # int + list도 불가능. 그걸 TypeError로 잡음
