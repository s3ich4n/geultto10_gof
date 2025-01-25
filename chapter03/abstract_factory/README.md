# ABSTRACT FACTORY

추상 팩토리 패턴.

# Intent

구체적인 클래스를 지정하지 않고 연관되거나 의존적인 객체의 집합을 생성하기 위한 인터페이스를 제공한다

# aka.

키트(_kit_)

# Motivation

Motif[^1] 나 Presentation Manager[^2](이하 PM) 같은 GUI 툴킷(현대 GUI라고 하자면 Qt나 GTK, 윈도우즈의 WPF같은 것)을 생각해보자. 근간이 되는 프레임워크는 여러 룩앤필 표준을 지원할 수 있으며, 스크롤바, 윈도우, 버튼 등의 UI 위젯에 대해 서로 다른 외관과 동작을 정의한다. 이 때, 하드코딩해서는 룩앤필의 변화를 대응하기 어렵다.

따라서 각각의 위젯을 생성하기 위한 인터페이스만 선언한다. `WidgetFactory` 정도로 생성하고, 이를 구현하는 concrete class는 아래와 같을 것이다:

- `MotifWidgetFactory`: Motif용 룩앤필을 구현하는 구현체를 로드
- `PMWidgetFactory`: PM용 룩앤필을 구현하는 구현체를 로드

실제 실행시에는, 프로그램 실행 시 상황에 맞게[^3] 팩토리를 알아서 결정하게 할 수 있다는 것이다. 다시 말해 클라이언트는 추상 클래스에 의해 정의된 인터페이스에만 종속될 뿐, 특정 구체 클래스에는 종속되지 않는다.

# Applicability

아래 상황에 적합하다:

- 시스템이 제품(객체)들이 어떻게 생성되고, 구성되고, 표현되는지와 독립적이어야 할 때.
    - 예: UI 시스템이 특정 위젯 라이브러리(Motif, Qt 등)의 구체적인 구현에 의존하지 않아야 할 때
- 시스템이 여러 제품군 중 하나로 구성되어야 할 때.
    - 예: 애플리케이션이 Motif나 Presentation Manager 중 하나의 룩앤필로 구성되어야 할 때
- 관련된 제품 객체들의 집합이 함께 사용되도록 설계되었고, 이 제약을 강제해야 할 때.
    - 예: Motif 버튼은 반드시 Motif 스크롤바, Motif 메뉴 등과 함께 사용되어야 할 때
- 제품들의 클래스 라이브러리를 제공하면서, 구현이 아닌 인터페이스만 공개하고 싶을 때.
    - 예: 위젯 라이브러리를 만들 때 사용자에게 구체적인 구현은 숨기고 위젯 생성을 위한 인터페이스만 제공하고 싶을 때

# Structure

![refactoring.guru의 Abstract Factory 그림](https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure-2x.png)

# Participants

- `AbstractFactory` (`WidgetFactory`)
    - 추상 제품 객체들을 생성하기 위한 인터페이스를 정의
- `ConcreteFactory` (`MotifWidgetFactory`, `PMWidgetFactory`)
    - 구체적인 제품 객체를 생성하는 연산을 구현
- `AbstractProduct` (`Window`, `ScrollBar`)
    - 제품 객체의 종류에 대한 인터페이스를 정의
- `ConcreteProduct` (`MotifWindow`, `MotifScrollBar`)
    - 구체적인 팩토리가 생성할 제품 객체를 정의
    - `AbstractProduct` 인터페이스를 구현
- `Client`
    - `AbstractFactory`와 `AbstractProduct` 클래스에 선언된 인터페이스만을 사용

# Collaborations

- ConcreteFactory 클래스의 단일 인스턴스가 런타임에 생성
- 구체 팩토리는 특정한 구현을 가진 제품 객체들을 생성
- 다른 제품 객체들을 생성하려면 클라이언트는 다른 구체적인 팩토리를 사용해야 함
    - 예: `MotifWidgetFactory`의 인스턴스가 하나 생성되어 Motif 스타일의 모든 위젯을 생성하며, PM 스타일의 위젯이 필요하다면 `PMWidgetFactory` 를 사용해야 함
- AbstractFactory는 제품 객체의 생성을 자신의 ConcreteFactory 서브클래스에게 위임
    - 예: WidgetFactory는 실제 위젯 생성을 `MotifWidgetFactory`나 `PMWidgetFactory`와 같은 구체적인 서브클래스에게 위임

# Consequences[^4]

- 구체 클래스의 분리
- 제품군 교체의 용이성
- 제품 간 일관성 보장
- 새로운 종류의 제품 추가의 어려움

# Implementation

1. Factories as Singletons (싱글톤으로서의 팩토리)
    - `ConcreteFactory`는 제품군당 하나의 인스턴스만 필요하므로, 싱글톤 패턴으로 구현하는 것이 좋음
2. Creating the Products (제품 생성 방법)
    - Factory Method 패턴을 사용하는 방법
    - Prototype 패턴을 사용하는 방법
        - 새로운 제품군마다 새로운 concrete factory를 만들 필요가 없어짐
        - 프로토타입 인스턴스를 복제하는 방식
    - 클래스를 직접 저장하는 방법 (Smalltalk, Objective-C 같은 언어에서)
3. Defining Extensible Factories (확장 가능한 팩토리 정의)
    - 새로운 종류의 제품을 추가하기 위한 유연한 방법 제시
    - 파라미터를 통해 생성할 객체 종류를 지정
    - 단, 이 방식은 타입 안전성과 trade-off 관계에 있음

# Sample Code

# Known Uses

- Qt

# Related Patterns

- 추상 팩토리 클래스는 Factory Method를 사용하여 구현할 수도, Prototype 을 사용하여 구현할 수도 있음
- 구체적인 팩토리는 종종 Singleton 으로 구현됨

[^1]: https://en.wikipedia.org/wiki/Motif_(software)
[^2]: https://en.wikipedia.org/wiki/Presentation_Manager
[^3]: 런타임에 결정되게 한다는 뜻
[^4]: 저는 굳이 장단점 형식으로 사족을 달지않았고 이유가 있습니다. 왜냐하면 패턴의 사용은 장단점으로 볼 게 아니라, 이 특징을 알고 트레이드오프 해야한다고 생각했기 때문입니다. 앞으로도 계속 그렇게 작성될 것 같습니다.