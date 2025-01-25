# GoF의 디자인 패턴 요약

글또 10기에서 GoF 디자인 패턴 스터디를 시작. 이를 작성하고 글로 남긴다.

- [x] 1장
- [x] 2장
- [ ] 3장
    - [x] Abstract Factory
    - [x] Builder
    - [ ] Factory Method
    - [ ] Prototype
    - [ ] Singleton 
- [ ] 4장
    - [ ] Adapter
    - [ ] Bridge
    - [ ] Composite
    - [ ] Decorator
    - [ ] Facade
    - [ ] Flyweight
    - [ ] Proxy 
- [ ] 5장
    - [ ] Chain of Responsibility
    - [ ] Command
    - [ ] Interpreter
    - [ ] Iterator
    - [ ] Mediator
    - [ ] Memento
    - [ ] Observer
    - [ ] State
    - [ ] Strategy
    - [ ] Template Method
    - [ ] Visitor 
- [ ] 6장

# 환경구성

## pre-requisites

1. python `^3.12.6` (`.python-version` 파일 참고)
1. poetry, pyenv

## 설치

```shell
pyenv local
poetry env use python
poetry install
```

# 테스트 구동

## 예시 - 추상 팩토리 테스트

```shell
cd chapter03/abstract_factory
pytest -v

========================================== test session starts ===========================================
platform darwin -- Python 3.12.6, pytest-8.3.4, pluggy-1.5.0 -- {PYTHON_PATH}/python
cachedir: .pytest_cache
rootdir: {GIT_ROOT_DIR}/chapter03/abstract_factory
configfile: pytest.ini
testpaths: test
collected 5 items                                                                                        

test/test_maze_components.py::TestMazeComponents::test_room_initialization PASSED                  [ 20%]
test/test_maze_components.py::TestMazeComponents::test_room_side_setting PASSED                    [ 40%]
test/test_maze_components.py::TestMazeComponents::test_door_connection PASSED                      [ 60%]
test/test_maze_creation.py::test_create_normal_maze PASSED                                         [ 80%]
test/test_maze_creation.py::test_create_enchanted_maze PASSED                                      [100%]

=========================================== 5 passed in 0.01s ============================================
```
