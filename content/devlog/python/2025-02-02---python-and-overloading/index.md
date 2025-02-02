---
title: '파이썬에는 오버로딩이 없다고요?'
date: "2025-02-02T05:22:07.000Z"
template: "post"
draft: false
slug: "/devlog/python/2025-02-02-python-and-overloading"
category: "devlog"
tags:
  - "python"
  - "geultto"
description: '파이썬이 가지는 언어적 측면과 철학에서 다가오는 차이때문에 없습니다. 어떤 차이가 있고 어떤 개념에 차이가 있는지 파악 후 왜 오버로딩이 없나 살펴봅시다.'
socialImage: { "publicURL": "./media/sangdo-dong.jpg" }
---

[지난 글에 소개드린](https://blog.s3ich4n.me/devlog/python/2025-01-19-refactoring-and-design-pattern) 글또10기 디자인패턴 스터디를 통해 이야기를 나누다가, 파이썬에선 오버로딩이 되는지를 가만 생각해보았습니다.

# 오버로딩이 되던가..?

```java
class Calculator {
    int add(int a, int b) {
        return a + b;
    }
    
    String add(String a, String b) {
        return a + b;
    }
}
```

그러니까, 이런 코드가 도는지 말이죠. 두 `add` 메소드는 공존할까요?

```python
import pytest

class Calculator:
    def add(self, a, b):
        return a + b

    # 같은 이름으로 다른 메소드 정의 시도
    def add(self, a, b, c):
        return a + b + c
```

테스트코드를 짜고,

```python
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
```

...한번 테스트해봅시다.

```shell
$ pytest -v test/qna/test_python_overloading01.py
========================= test session starts ========================
platform darwin -- Python 3.12.6, pytest-8.3.4, pluggy-1.5.0 -- <PYTHONPATH>
cachedir: .pytest_cache
rootdir: <BASEDIR>
configfile: pytest.ini
collected 2 items

test_python_overloading01.py::test_method_overloading PASSED    [ 50%]
test_python_overloading01.py::test_method_signature PASSED      [100%]

========================== 2 passed in 0.00s =========================
```

주석으로 이미 작성했다시피, 테스트는 통과했습니다. `TypeError`가 런타임에 `raise`된 것이 캐치된 것이죠. 그렇다는 건 위의 자바코드와 같은 구성은 사용할 수 없다는 내용입니다. 😱🙀

그렇다면 왜 안되는걸까요?

# 먼저 파이썬의 특징을 살펴봅시다

파이썬에서의 타입에 대해 살펴보고, 파이썬 객체가 가지는 특징을 통해 오버로딩의 대체방안을 살펴봅시다.

## 초식 (1) - 동적 타입

아마도 동적타입에 대한 이야기는 들어보셨을 겁니다[^1]. 타입을 별도로 지정해줄 필요가 없다보니 이런 행동이 가능합니다:

```python
def test_dynamic_type():
    x = 10  # int 타입이었다가

    print(id(x))
    assert type(x) == int

    x = "hello"  # 문자열로도 바꿀 수 있고

    print(id(x))
    assert type(x) == str

    x = [1, 2, 3]  # 리스트로도 수정할 수 있습니다.
    print(id(x))
    assert type(x) == list

>>> python -vs test_dynamic_type.py
test_dynamic_type.py::test_dynamic_type 4356563592
4363171952
4363299584
PASSED
```

다시말해 이렇게 됩니다:

1. 새로운 객체가 생성되고
1. 변수 `x`는 이 새로운 객체를 가리키게 됩니다
1. 이전에 참조하던 객체와의 연결은 끊어집니다

``` python
x = 10        # x ----> [10] (id: 4356563592)
x = "hello"   # x ----> ["hello"] (id: 4363171952)
x = [1,2,3]   # x ----> [[1,2,3]] (id: 4363299584)
```

## 초식 (2) - Duck typing

그리고 파이썬은 Duck typing을 지원합니다. 아주 유명한 말이죠:

> 오리처럼 생기고, 오리처럼 헤엄치고, 오리처럼 우는 게 있다면 그건 오리일 가능성이 높다.

객체에 빗대자면 이렇게 되겠죠:

객체가 해당 타입에서 요구하는 모든 메서드와 속성을 가지고 있다면 그 타입으로 간주됩니다. 상속관계를 보지 않고 필요 메소드와 속성을 가지는지만 체크합니다.

```python
class Duck:
    def sound(self):
        return "꽥꽥"

class Dog:
    def sound(self):
        return "멍멍"

def make_sound(animal):
    # animal의 구체적인 타입은 중요하지 않음
    # sound() 메소드만 있으면 됨
    return animal.sound()

def test_duck_typing():
    assert make_sound(Duck()) == "꽥꽥"
    assert make_sound(Dog()) == "멍멍"
>>> python -vs test_duck_typing.py
test_duck_typing.py::test_duck_typing PASSED
```

즉, 앞서 살펴보았던 자바와 같은 정적 타입 언어는 컴파일 시점에 메서드 시그니처로 오버로딩을 결정합니다. 하지만 파이썬은 런타임에 메서드의 존재 여부만 확인하죠.

## 초식 (3) - The dunder methods

파이썬 클래스는 설계 시 dunder methods[^2] 를 이용하여 설계할 수도 있습니다[^3]. 이로 인해 파이썬은 특정 인터페이스를 구현하지 않고도 주요 타입에 대해 동작을 정해줄 수 있지요.

### 기본 dunder method를 살펴봅시다

예를 들어 이런 테스트를 한다고 합시다.

```python
import pytest

def test_dunder_methods():
    with pytest.raises(TypeError):
        1 + "2"     # 이걸 해주는 연산이 정의되지 않아서 안 되었던거고,
    
    assert str(1) + "2" == "12"     # 서로 맞는 타입끼리의 `__add__`는 있으니 가능한 것이지요

>>> pytest -vs test_dunder_methods()
test_dunder_methods.py::test_dunder_methods PASSED
```

### 예시를 살펴봅시다

그렇다면, 다양한 dunder를 직접 구현하고 이를 살펴봅시다. 예를들어, 길이를 표현하는 `Length` 라는 객체를 구상하고 이를 파이썬의 클래스로 표현해봅시다.

이 클래스는 아래와 같은 기능을 제공합니다:

- `Length` 클래스를 쓰고자 하는 이에게 값을 설명함
    - 단순 엔드유저를 위한 출력 기능
    - `Length` 클래스 개발 중 디버깅 등을 하기 위한 출력기능
- 값의 길이, 동등여부, less than 연산여부를 가릴 수 있음

```python
class Length:
    def __init__(self, meters):
        self.meters = meters

    def __str__(self):
        return f"{self.meters}m"      # print() 출력용
    
    def __repr__(self):
        return f"Length({self.meters})"  # 개발자용 상세 출력
    
    def __len__(self):
        return int(self.meters)       # len() 호출 시
    
    def __eq__(self, other):
        return self.meters == other.meters  # == 연산자
    
    def __lt__(self, other):
        return self.meters < other.meters   # < 연산자
```

이를 테스트하면 아래와 같겠죠.

```python
def test_custom_dunder():
    distance = Length(5)
    
    # __str__: 사용자(Length 사용자) 친화적 출력
    assert str(distance) == "5m"
    
    # __repr__: 개발자(Length 개발자)를 위한 상세 출력
    assert repr(distance) == "Length(5)"
    
    # __len__: len() 함수 지원
    assert len(distance) == 5
    
    # __eq__, __lt__: 비교 연산자 지원
    assert Length(5) == Length(5)
    assert Length(3) < Length(5)
>>> pytest -vs test_custom_dunder()
test_custom_dunder.py::test_custom_dunder PASSED
```

이런 식으로, 파이썬의 기본문법을 써서 내가 원하는 개념을 표현할 수 있게 됩니다.

## 파이썬의 특징 정리

언어의 특성이 가지는 구조적 설계방안으로 인해 오버로딩 불가능이 아닌, 구현 방법이 달랐던 것입니다.

1. 변수에 타입을 지정해주지 않아도 되고
2. 덕 타이핑의 개념이 지원되고
3. 파이썬의 문법을 그대로 활용할 수 있도록 dunder method를 구현하면[^4] 됩니다.

그렇지만 이런 부분이 문제가 있죠.

1. 런타임에 프로그램 크래쉬를 유발할 수 있다는 점
2. 명확성 감소 (파이썬이 추구하는 명확성이 떨어짐이 문제)
3. '되겠거니' 하다보니 유지보수가 힘들어짐 - 이런 코드가 쌓이면 코드의 예측이 어려움

# 그렇지만 타입을 아예 모르고 쓰고싶진 않아요...

파이썬은 이런 부분에 대해 충분히 인지하고 있었기 때문에 현재는 타입에 _힌트를 줄 수도_ 있고, 런타임 레벨에서 어느정도 강제할 수 있는 방안을 제공합니다. 이에 대해 하나씩 설명하고자 합니다.

## 타입 힌팅

> 파이썬 3.5부터 처음 나온 개념입니다.

타입 힌팅은 파이썬 코드에 타입 정보를 명시적으로 추가하는 방법입니다. 파이썬 3.5에서 처음 도입되었고, 코드의 가독성과 유지보수성을 높이는데 큰 도움을 줍니다.

파이썬 타입힌팅의 주요 특징은 아래와 같습니다:
- 런타임에는 영향을 주지 않음 (단순한 힌트일 뿐)
- IDE와 타입 체커가 코드 분석 시 활용
- 코드의 의도를 명확히 전달 가능

타입 힌팅은 아래와 같은 장점을 가집니다.

1. 코드 이해도 향상
    - 함수나 변수의 예상되는 타입을 바로 알 수 있음
    - 문서화 효과
2. 버그 조기 발견
    - IDE나 타입 체커가 타입 관련 오류를 사전에 발견
    - 런타임 에러를 줄일 수 있음
3. 리팩터링 용이성
- 타입 정보가 있어 안전한 코드 수정 가능
- 자동 완성 기능 강화

파이썬에서 타입힌팅은 다양한 방법으로 기재할 수 있습니다.

- 실제 구동할 코드에 타입힌팅을 주는 법(가장 널리 알려진 타입힌팅, 이쪽을 사용)
- `.pyi` 파일 등에 기록하는 것
    - 기존 파일을 그대로 두고 타입 힌팅만 제공합니다
    - CPython 인터페이스에 주로 사용됩니다
    ```python
    # mylib.pyi
    def add(a: int, b: int) -> int: ...
    def greet(name: str) -> str: ...
    ```
- `py.typed` 파일로 기록하는 것
    - 패키지가 타입 힌트를 공식제공함을 알리는 마커 파일입니다
    - 패키지 루트에 두고 정적 타입 체커가 이를 인식하게 합니다

이렇다보니 보통은 실제 구동코드에 타입힌팅을 주는 부분이 더 익숙합니다. 본 문서에서는 이 내용을 짚고 넘어가려 합니다.

### 타입 힌팅을 어떻게 하나요?

파이썬 공식문서의 예시를 살펴볼까요.

```python
def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."
```

함수 시그니처를 이렇게 힌팅할 수 있습니다. `float` 타입을 받고 `str` 타입을 리턴하는 형식이죠.

타입에 대한 힌트도 줄 수 있습니다.

```python
Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

아니면 아예 이런식으로 `TypeAlias` 를 써줄 수도 있지요.

```python
from typing import TypeAlias

Vector: TypeAlias = list[float]
```

### 타입힌팅 심화

1. TypeVar로 제네릭 타입 만들기

`TypeVar`는 파이썬에서 제네릭 타입을 정의할 때 사용하는 특별한 타입입니다. Java의 제네릭과 유사한 역할을 하며, 타입의 재사용성과 유연성을 높여줍니다.

```python
from typing import TypeVar, List, Sequence

T = TypeVar('T')  # 어떤 타입이든 될 수 있는 타입 변수

def first(lst: Sequence[T]) -> T:
    if not lst:
        raise ValueError("Empty sequence")
    return lst[0]

# 사용 예시
numbers: List[int] = [1, 2, 3]
first_num: int = first(numbers)  # T는 int로 추론됨

strings: List[str] = ["hello", "world"]
first_str: str = first(strings)  # T는 str로 추론됨
```

`bound` 값을 추가하여 타입을 제한할 수도 있습니다.

```python
# bound를 이용한 타입 제한
class Animal:
    def feed(self) -> None:
        pass

class Dog(Animal):
    def bark(self) -> None:
        print("멍멍!")

# Animal이나 Animal의 서브클래스만 허용
BoundT = TypeVar('BoundT', bound=Animal)

def take_care(animal: BoundT) -> BoundT:
    animal.feed()  # Animal의 메소드는 항상 사용 가능
    return animal

# 사용 예시
dog = Dog()
take_care(dog)  # OK
take_care("cat")  # 타입 체커 에러: str은 Animal의 서브타입이 아님
```

2. 제약 조건이 있는 TypeVar

특정 타입들로만 제한하고 싶을 때는 `TypeVar`에 제약 조건을 걸 수 있습니다:

```python
from typing import TypeVar, Union, List

# str이나 bytes 타입만 허용
StrOrBytes = TypeVar('StrOrBytes', str, bytes)

def concat(x: StrOrBytes, y: StrOrBytes) -> StrOrBytes:
    return x + y

# 이렇게 하면 됨
result1 = concat("Hello, ", "World")  # OK
result2 = concat(b"Hello, ", b"World")  # OK

# 이건 타입 체커가 에러를 발생시킴
# result3 = concat(1, 2)  # Error: int는 허용되지 않음
```

3. overload 데코레이터 활용하기

`@overload` 데코레이터를 사용하면 함수가 여러 타입 시그니처를 가질 수 있음을 타입 체커에 알려줄 수 있습니다. 런타임에는 영향을 주지 않지만, 개발 시점에 타입 안전성을 보장하는데 도움을 줍니다.

```python
from typing import overload, Union

class StringProcessor:
    @overload
    def process(self, value: str) -> str: ...
    
    @overload
    def process(self, value: list[str]) -> list[str]: ...
    
    def process(self, value: Union[str, list[str]]) -> Union[str, list[str]]:
        if isinstance(value, str):
            return value.upper()
        return [v.upper() for v in value]

def test_string_processor():
    processor = StringProcessor()
    
    # 둘 다 타입 체크를 통과함
    result1: str = processor.process("hello")  # "HELLO"
    result2: list[str] = processor.process(["hello", "world"])  # ["HELLO", "WORLD"]
```

4. 선택적 매개변수와 기본값

`Optional` 표기를 통해 필요한 값을 추가적으로 쓸 수 있게 표기할 수도 있습니다. 그리고 기본값도 줄 수 있지요.

```python
from typing import Optional

def greet(name: str, title: Optional[str] = None) -> str:
    if title:
        return f"Hello, {title} {name}!"
    return f"Hello, {name}!"

result1 = greet("Alice", "Ms.")  # "Hello, Ms. Alice!"
result2 = greet("Bob")  # "Hello, Bob!"
```

5. Union 타입과 Literal 타입

Literal 은 말 그대로(_literally_) 동일한 문자열이 오기를 기대하는 타입입니다.

Union은 이 값 중 하나의 값을 선택하겠다라는 의미로 사용합니다. 파이썬 3.11부터는 `|` 연산자로 표기할 수도 있지요.

```python
from typing import Union, Literal

# 특정 문자열만 허용하는 타입
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

def log(
    message: str,
    level: LogLevel,
    code: Union[int, str]
    # 파이썬 3.11 이상부터는
    # code: int | str 도 가능합니다.
) -> None:
    print(f"[{level}] {code}: {message}")

# 모두 유효한 호출입니다.
log("System starting", "INFO", 100)
log("File not found", "ERROR", "E404")

# 타입 체커가 에러를 발생시키는 경우
# log("Test", "INVALID", 200)  # Error: "INVALID"는 LogLevel에 없으니 안되죠.
```

6. 콜백 함수의 타입 힌팅

파이썬의 모든 것은 객체이므로, 이를 `Callable` 이라는 이름으로 매개변수로 받을 수 있게 힌트를 줄 수 있습니다. 이를 이용한 예시는 아래와 같습니다:

```python
from typing import Callable, TypeVar

T = TypeVar('T')
R = TypeVar('R')

# Callable의 특징을 기재함
def map_list(func: Callable[[T], R], items: list[T]) -> list[R]:
    return [func(item) for item in items]

# 사용 예시
numbers = [1, 2, 3]
squares = map_list(lambda x: x * x, numbers)  # [1, 4, 9]
```

7. 클래스 메서드와 프로퍼티

`Protocol` 로 클래스 정의를 미리 흉내낼 때는 이렇게 프로퍼티를 미리 정의할 수도 있습니다.

```python
from typing import ClassVar, Protocol

class DataProcessor(Protocol):
    MAX_ITEMS: ClassVar[int]  # 클래스 변수
    
    @property
    def item_count(self) -> int: ...
    
    def process(self, data: list[str]) -> None: ...

class CSVProcessor:
    MAX_ITEMS: ClassVar[int] = 1000
    
    def __init__(self) -> None:
        self._items: list[str] = []
    
    @property
    def item_count(self) -> int:
        return len(self._items)
    
    def process(self, data: list[str]) -> None:
        if len(data) > self.MAX_ITEMS:
            raise ValueError("Too many items")
        self._items.extend(data)
```

이러한 타입 힌팅을 활용하면 코드의 안정성을 높이고 개발자의 실수를 줄일 수 있습니다. IDE나 타입 체커를 통해 많은 오류를 사전에 발견할 수 있으며, 코드의 자동완성 기능도 더욱 정확해집니다.

### 타입힌팅 - Structural Subtyping으로

파이썬의 타입 힌팅은 시간이 지나면서 더 파이썬스러운 방식으로 발전했습니다. 위에서 보았던 예시를 다시 살펴볼까요?

```python
class Duck:
    def sound(self):
        return "꽥꽥"

class Dog:
    def sound(self):
        return "멍멍"

def make_sound(animal):
    # animal의 구체적인 타입은 중요하지 않음
    # sound() 메소드만 있으면 됨
    return animal.sound()

def test_duck_typing():
    assert make_sound(Duck()) == "꽥꽥"
    assert make_sound(Dog()) == "멍멍"
>>> python -vs test_duck_typing.py
test_duck_typing.py::test_duck_typing PASSED
```

이후 structural subtyping 이 도입되면서, 클래스가 특정 메서드들을 구현하기만 하면 자동으로 해당 타입으로 인식되도록 변경되었습니다. `Protocol` 클래스를 통해 새 인터페이스를 정의할 수도 있지요.

> 파이썬 3.8에서 처음 나온 개념입니다.

```python
from typing import Protocol

class Animal(Protocol):
    def sound(self) -> str:
        ...  # Protocol은 구현부 없이 메서드 시그니처만 정의

# make_sound에서, `Animal` 을 정의해주었으니
# 컴파일 타임에 Protocol이 요구하는 메소드/속성이 있는지 정적으로 확인한다
# 이제 Duck과 Dog는 자동으로 Animal 프로토콜을 구현한 것으로 인식한다!
def make_sound(animal: Animal) -> str:
    return animal.sound()
```

다만 이런 정적 타입 체커(static type checker)를 활용하면 실제 개발에만 도움을 줄 뿐, 기저에 있는 덕 타이핑 방식대로 동작하며 개발 시 문제를 잡을 수 있게 도움을 의미합니다.

### 타입힌팅을 도와주는 도구

앞서말했듯 타입 힌트를 도와주는 도구들을 통해 도움을 받을 수 있습니다. 가령 PyCharm 에서 저장 시 프로젝트의 모든 내 파이썬 파일에 대해 린트를 하는 등의 조치를 의미하죠. 때로는 타입이 맞지 않아 실제 코드를 잘못 사용하고있음을 알 수도 있습니다.

정적 타입 검사기로는 아래 작업을 수행할 수 있습니다:
    - 코드 실행 없이 타입 오류를 분석
    - MyPy, Pyright, Pyre 등이 대표적
    - PEP 484(타입 힌트) 및 PEP 544(Protocol) 같은 제안을 기반으로 동작

이런 도구들이 IDE와 결합되면 저장과 동시에 린팅, 타입검사 후 에러체크를 수행해주기도 합니다.

반면 런타임에 타입을 검사하는 건 `isinstance()` 나 `type()` 이 있습니다. 이런 부분도 적절히 코드에 잘 녹여내서 해결할 수 있지요.

### 타입 힌팅에 대한 예시

`pyproject.toml` 에 기재하는 타입 힌팅 및 린팅(Black 사용법)을 기존으로 간단한 예시를 설명드리고자 합니다. 

아래 설정은 다음과 같은 내용을 강제합니다:
1. 모든 함수에 타입 힌트 필수 (`disallow_untyped_defs = true`)
2. 불완전한 타입 힌트 불허 (`disallow_incomplete_defs = true`)
3. Any 타입 반환 시 경고 (`warn_return_any = true`)
4. 테스트 코드는 타입 힌트 옵션 (`[[tool.mypy.overrides]]` 섹션)

```toml
[tool.black]
line-length = 108
target-version = ['py311']
include = '\.pyi?$'

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true

[[tool.mypy.overrides]]
module = ["tests.*"]
disallow_untyped_defs = false

[tool.isort]
profile = "black"
multi_line_output = 3
```

black과 함께 사용하면 코드 스타일과 타입 안정성을 모두 확보할 수 있습니다.

# 진짜 오버로딩을 하려면 어떻게 해야해요..?

이런 특성대신 실제 오버로딩을 활용하고자 한다면 파이썬 기본제공 도구를 사용하거나, 서드파티 라이브러리를 사용하여 해결할 수 있습니다.

## `@singledispatch` 활용

실제 목적으로서의 오버로딩을 구현하기 위해선 `functools` 의 `@singledispatch` 를 이용할 수 있습니다. 예를 들어 아래와 같은 계산기가 있다고 가정합시다.

```python
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
```

이런 식으로 변경 후, 아래와 같이 사용할 수 있습니다:

```python
def test_calc_int():
    calc = Calculator()

    result = calc.add(1, 2)     # int 값 만을 받는 것은 허용

    assert result == 3
```

```python
def test_calc_str():
    calc = Calculator()

    result = calc.add("1", "2")     # str 값도 허용

    assert result == "12"
```

하지만, 파이썬 특유의 연산으로도 안 되는 건(프로토콜에 정의되지 않은 건) `TypeError` 가 납니다.

```python
def test_single_dispatch_limitation():
    calc = Calculator()
    
    # 런타임에 뭐가 들어올 지 몰라서, 일단 연산을 시키기 때문에 에러가 날 수 있음
    with pytest.raises(TypeError):
        calc.add(1, "2")  # int + str는 불가능. 그걸 TypeError로 잡음
    
    with pytest.raises(TypeError):
        calc.add("1", 2)  # str + int도 불가능. 그걸 TypeError로 잡음
    
    with pytest.raises(TypeError):
        calc.add(1, [1,2,3])  # int + list도 불가능. 그걸 TypeError로 잡음
```

### 한계점?

`@singledispatch` 는 하나의 타입만 체크합니다. 그래서 [`multipledispatch`](https://pypi.org/project/multipledispatch/) 를 사용한다면, `TypeError` 가 아니라 `NotImplementedError` 를 raise 할 수 있습니다.

```python
from multipledispatch import dispatch   # 이렇게 multipledispatch를 쓰면
import pytest

class Calculator:
    @dispatch(int, int)      # 여러 타입을 쓸 수 있습니다.
    def add(self, data1, data2):
        return data1 + data2

    @dispatch(str, str)
    def add(self, data1, data2):
        return data1 + data2
```

```python
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
```

# 끝으로

정리하면 아래와 같습니다:

파이썬은 덕 타이핑과 구조적 타이핑을 지원하는 언어이므로, 전통적인 오버로딩 개념이 잘 맞지 않습니다. 그러나 `@singledispatch`, `Protocol`, `TypeVar` 등을 활용하면 타입 체크를 강화할 수도 있습니다.

언어가 지니는 특징과 구현방안을 이해한다면 보다 그 언어가 추구하는 방향으로 코드를 짤 수 있을 것입니다.

[^1]: https://en.wikipedia.org/wiki/Type_system 을 함께 살펴보면 더욱 좋습니다.
[^2]: https://docs.python.org/3/glossary.html#term-special-method 를 의미합니다. dunder(_double underscore_) methods, special methods, 매직 메소드(_magic methods_) 라고 부르기도 합니다.
[^3]: https://docs.python.org/3/reference/datamodel.html#special-method-names 을 참고해 주세요.
[^4]: 이를 프로토콜 구현이라고 부르기도 합니다.
