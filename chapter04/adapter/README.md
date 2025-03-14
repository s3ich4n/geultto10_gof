# ADAPTER

# Intent

클래스의 인터페이스를 클라이언트가 기대하는 다른 인터페이스로 변환.

어댑터를 통해 호환되지 않는 인터페이스를 함께 작동할 수 있게 조율.

# aka.

Wrapper

# Motivation

가정:

- 그래픽 요소를 배치해서 그림과 다이어그램을 만드는 드로잉 에디터를 제작 중

구성요소:

- 그래픽 객체 인터페이스 - `Shape` 클래스 (추상클래스)
- 선을 그리는 클래스(`LineShape`), 다각형을 그리는 클래스 (`PolygonShape`)

하고싶은 것:

- 텍스트를 그리는 클래스 (`TextShape`)를 추가하고 싶다.

제약조건:

- 텍스트 편집에는 `TextView` 라는 클래스가 있지만, 이 메소드는 그리는 기능도 고려하여 설계한 것이 아니라 호환이 불가하다.

해결책:

1. `Shape`의 인터페이스와 `TextView`의 구현을 상속받는다
2. `TextShape` 안에 `TextView` 인스턴스를 합성하고 `TextView` 의 인터페이스를 기반으로 `TextShape`를 구현한다

해결책 - 정리:

- `TextShape` 에서 둘의 속성을 모두 가지기 위해
    - `Shape`를 상속받고 인터페이스 구현
    - `TextView` 인스턴스를 합성(_composition_) 하고 (텍스트 기능을 쓰기위해)
    - 텍스트 기능을 쓰려면 `createManipulator()` 를 구현해서 씀 - `Manipulator` 추상클래스의 구현체 중 텍스트에 맞는 일부를 구현하라는 뜻

# Applicability

아래와 같을 때 적절함

1. 기존 클래스의 인터페이스가 필요한 인터페이스와 맞지 않을 때
1. 관련 없는 클래스들과도 협력 가능한 재사용 클래스가 필요할 때
1. (객체 어댑터의 경우) 여러 서브클래스를 각각 상속받기보다는 한번에 적응시켜야 할 때

# Structure

- 클래스 어댑터의 경우

![refactoring.guru의 Class Adapter 예시](https://refactoring.guru/images/patterns/diagrams/adapter/structure-class-adapter-indexed-2x.png)

- 객체 어댑터의 경우

![refactoring.guru의 Object Adapter 예시](https://refactoring.guru/images/patterns/diagrams/adapter/structure-object-adapter-indexed-2x.png)

# Participants

Target (`Shape`)

- 클라이언트가 사용하는 도메인 특화 인터페이스를 정의

Client (`DrawingEditor`)

- Target 인터페이스를 준수하는 객체들과 협력

Adaptee (`TextView`)

- 적응이 필요한 기존 인터페이스를 정의

Adapter (`TextShape`)

- Adaptee의 인터페이스를 Target 인터페이스에 맞게 변환

# Collaborations

1. 클라이언트는 어댑터 인스턴스의 operations를 호출.
1. 어댑터는 그 요청을 수행하기 위해 Adaptee의 연산을 호출.

# Consequences

클래스 어댑터:

1. 구체적인 어댑터 클래스에 종속되어 Adaptee의 모든 서브클래스에 적용이 어려움
2. Adaptee를 상속받기 때문에 일부 동작을 오버라이드 가능
3. 단일 객체만 사용하므로 포인터 참조가 추가로 필요 없음

객체 어댑터:

1. 하나의 어댑터로 여러 Adaptee(서브클래스 포함) 처리 가능
2. 모든 Adaptee에 한 번에 기능 추가 가능
3. Adaptee 동작 오버라이드가 더 어려움 (서브클래싱 필요)

**주요 고려사항:**

1. 어댑터의 작업 범위
    - 단순 인터페이스 변환부터 완전히 다른 연산 세트 지원까지 다양
    - Target과 Adaptee 인터페이스의 유사성에 따라 작업량 결정
2. 플러그가능 어댑터
    - 클래스 재사용성을 높이기 위해 인터페이스 적응을 내장
    - 예: TreeDisplay 위젯이 다양한 트리 구조를 표시할 수 있도록 함
3. 양방향 어댑터
    - 서로 다른 클라이언트가 객체를 다르게 봐야 할 때 유용
    - 예: Unidraw와 QOCA 시스템 통합 사례
    - 다중 상속을 통해 양쪽 인터페이스 모두 지원 가능

**핵심 시사점:**

1. 어댑터 유형 선택 시 확장성과 유연성을 고려해야 함
2. 재사용성을 높이려면 인터페이스 적응을 클래스 내부에 구현하는 것이 좋음
3. 양방향 어댑터는 서로 다른 시스템 통합 시 유용한 해결책이 될 수 있음

# Implementation

위 어댑터 구현의 다양한 접근법이 있음:

1. 추상 연산 사용 (클래스 어댑터)

- 추상 메서드를 정의하고 서브클래스에서 구현
- 가장 전통적인 방식이지만 유연성이 낮음


2. 위임 객체 사용 (객체 어댑터 - 합성 활용)

- 별도의 인터페이스를 통해 기능을 위임
- 런타임에 어댑터 교체 가능
- 더 유연하지만 추가 객체 필요


3. 매개변수화된 어댑터 (객체 어댑터 - 객체를 직접 주입)

- 함수나 람다를 통해 동작을 주입
- 가장 유연하고 간단한 방식
- 단순한 변환에 적합

# Sample Code

`adapter/src`, `adapter/test` 참조

## 코드 소개

1. pegs, holes 모듈: Adapter 패턴을 적용하기 위한 예시
    - pegs: 말뚝을 나타내는 클래스 (둥근 말뚝, 네모 말뚝)
    - holes: 원형 구멍을 나타내는 클래스 (둥근 구멍)
    - adapter: pegs와 holes를 연결하는 어댑터 클래스
2. adapter 모듈
    - 네모 말뚝 어댑터

# Known usages

비슷한 목적의 기능을 한데모아 처리해야할 때 사용

1. 결제 시스템 통합 - 인터페이스 구성 후 구현체를 어댑터로 연결
2. 다양한 데이터 소스(CSV, JSON, XML) 통합 후 통일된 인터페이스로 제공

# Related patterns

ADAPTER는 기존 인터페이스를 변경하는 것이 주 목적

- BRIDGE: 구조는 비슷하나 목적이 다름. 인터페이스와 구현부를 분리하는 것이 목적
- DECORATOR: 인터페이스 변경 없이 기능을 추가하며, 재귀적 합성 가능
- PROXY: 대리자 역할을 하되 인터페이스는 변경하지 않음
