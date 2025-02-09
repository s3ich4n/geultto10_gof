# SINGLETON

# Intent

클래스의 인스턴스가 오직 하나만 존재하도록 보장하고, 이에 대한 전역적인 접근점을 제공

# aka.

# Motivation

클래스가 딱 하나의 인스턴스를 존재하게 하고싶기 때문.

전역변수는 객체에 대한 접근을 가능하게 하지만, 여러 객체가 인스턴스화 되는 것을 막지 못한다.

```python
class PrinterManager:
    def __init__(self):
        self.printer_queue = []

    def add_to_queue(self, document):
        self.printer_queue.append(document)


# 전역 변수로 프린터 매니저를 선언
global_printer_manager = PrinterManager()

# 다른 개발자가 실수로 새로운 인스턴스를 만들 수 있음
another_printer_manager = PrinterManager()  # 이것을 막을 수 없음!
yet_another_manager = PrinterManager()  # 이것도 막을 수 없음!
```

따라서 클래스 자체가 자신의 유일한 인스턴스를 추적하게 한다.

- 생성을 막고 클래스 자신을 통해서만 접근하게 하기 위함

# Applicability

- 클래스의 인스턴스가 정확히 하나만 존재해야 하고, 잘 알려진 접근점을 통해 클라이언트들이 이 인스턴스에 접근할 수 있어야 할 때
- 유일한 인스턴스가 서브클래싱으로 확장 가능해야 하고, 클라이언트가 코드 수정 없이 확장된 인스턴스를 사용할 수 있어야 할 때

# Structure

![refactoring.guru의 Singleton 그림](https://refactoring.guru/images/patterns/diagrams/singleton/structure-en-2x.png)

# Participants

클라이언트가 유일한 인스턴스에 접근할 수 있게 해주는 Instance 연산을 정의한다. Instance는 클래스 연산
자신의 유일한 인스턴스를 생성하는 책임을 가질 수 있다

# Collaborations

클라이언트는 오직 Singleton의 Instance 연산을 통해서만 Singleton 인스턴스에 접근할 수 있다

# Consequences

1. 단일 인스턴스에 대한 통제된 접근
    - 싱글턴 클래스가 유일한 인스턴스를 캡슐화하여 클라이언트의 접근을 엄격하게 제어 가능
2. 동작과 구현의 정제 가능
    - 싱글턴 클래스를 상속할 수 있어 확장이 용이
    - 런타임에 필요한 확장된 클래스의 인스턴스로 애플리케이션을 구성 가능
3. 인스턴스 수의 유연한 변경
    - 필요한 경우 싱글턴 클래스의 인스턴스를 여러 개 허용하도록 쉽게 변경 가능
    - 애플리케이션에서 사용하는 인스턴스 수를 제어 용이
    - 싱글턴 인스턴스에 접근하는 연산만 수정하면 됨

# Implementation

C++ 예시 대신 포인트만 놓고 보자면

"유일 인스턴스를 어떻게 보장할 것인가?" 를 구현해야 한다는 점이 핵심임.

# Sample Code

파이썬에선 모듈 시스템을 통해 전역상태를 사용하고 있으므로 달리 구현할 필요성을 못 느낌

필요하면, 메타클래스나 `__new__` magic method를 이용할 수 있다.

## 모듈시스템 활용예시 - 로깅

```python
# logger.py
import logging


def setup_logger():
    logger = logging.getLogger('app')
    if not logger.handlers:  # 중복 핸들러 방지
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


# 모듈 레벨에서 logger 설정
app_logger = setup_logger()

# user_service.py
from logger import app_logger


class UserService:
    def create_user(self, user_data):
        app_logger.info(f"Creating new user with data: {user_data}")
        try:
            # 사용자 생성 로직
            app_logger.info(f"Successfully created user: {user_data['username']}")
        except Exception as e:
            app_logger.error(f"Failed to create user: {str(e)}")
            raise


# payment_service.py
from logger import app_logger


class PaymentService:
    def process_payment(self, amount):
        app_logger.info(f"Processing payment of {amount}")
        try:
            # 결제 처리 로직
            app_logger.info("Payment processed successfully")
        except Exception as e:
            app_logger.error(f"Payment processing failed: {str(e)}")
            raise
```

이런 식으로 보일 수 있다:

```
2025-02-09 10:15:30,123 - app - INFO - Creating new user with data: {'username': 'john_doe', 'email': 'john@example.com'}
2025-02-09 10:15:30,456 - app - INFO - Successfully created user: john_doe
2025-02-09 10:15:31,789 - app - INFO - Processing payment of 100.00
2025-02-09 10:15:32,012 - app - INFO - Payment processed successfully
```

# Known usages

- 로깅 시스템
- 설정 및 구성관리
- DB연결 풀
- 앱 컨텍스트 (E.g., Spring에서의 `ApplicationContext` 같은 것)

# Related patterns

많은 다른 패턴들이 싱글턴 패턴에 기반하여 작성된다. 