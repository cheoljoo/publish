- doctest도 좋으나, 그냥 unittest를 써라.

# doctest
- [Link](https://docs.python.org/ko/3/library/doctest.html#module-doctest)
  - doctest는 예상 출력에서 정확한 일치를 요구하는 것에 심각합니다. 단일 문자가 일치하지 않아도 테스트가 실패합니다.
- [Limitations of Doctest Module](https://www.geeksforgeeks.org/testing-in-python-using-doctest-module/)
  - The Doctest module in Python has some limitations:
    - Limited Test Coverage: Doctest relies heavily on docstrings, making it suitable mainly for testing small code snippets or simple functions. It may not cover all aspects of complex functions or classes.
    - Readability Issues: Test cases embedded within docstrings can sometimes clutter the documentation, leading to reduced readability, especially for larger projects with numerous tests.
    - Brittleness: Doctest tests are sensitive to changes in output formatting or minor code modifications, which can cause tests to fail unnecessarily. This brittleness makes maintenance challenging, especially in evolving codebases.
- example.py
```python
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

- result
```
$  python3 example.py    # 모두 성공이면 아무것도 보이지 않음

$  python3 example.py -v
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    [factorial(n) for n in range(6)]
Expecting:
    [1, 1, 2, 6, 24, 120]
ok
Trying:
    factorial(30)
Expecting:
    265252859812191058636308480000000
ok
Trying:
    factorial(-1)
Expecting:
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
ok
Trying:
    factorial(30.1)
Expecting:
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
ok
Trying:
    factorial(30.0)
Expecting:
    265252859812191058636308480000000
ok
Trying:
    factorial(1e100)
Expecting:
    Traceback (most recent call last):
        ...
    OverflowError: n too large
ok
2 items passed all tests:
   1 tests in __main__
   6 tests in __main__.factorial
7 tests in 2 items.
7 passed and 0 failed.
Test passed.
```

# unittest
```
import unittest
```

## [기본 설명](https://docs.python.org/ko/3/library/unittest.html)
- ```class TestStringMethods(unittest.TestCase):``` 와 같이 unittest.TestCase 를 상속하는 class들을 ```unitest.main()```에서 알아서 수행시켜줌. 
  - class안에 test로 시작하는 member function들을 수행시켜줌

- 테스트는 매우 많지만, 그것을 위한 사전 설정은 계속 반복될 수 있습니다. 다행히, setUp()이란 메서드를 작성하여 사전 설정 코드를 밖으로 분리해낼 수 있습니다. 테스트 프레임워크가 1개의 테스트마다 매번 자동으로 이것을 호출할 것입니다. 테스트 메서드가 실행되고 나서 정리하기 위해 tearDown() 메서드를 제공합니다:
```python
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def tearDown(self):
        self.widget.dispose()
```

- setUpClass 와 tearDownClass : 이것들은 반드시 클래스 메서드로 구현되어야 합니다:
```
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()
```

- 테스트를 위한 실행 환경을 테스트 픽스쳐(test fixture)라고 부릅니다. 개별 테스트 메서드를 실행하기 위해 고유한 테스트 픽스쳐에 해당하는 새로운 테스트 케이스 인스턴스가 생성됩니다. 따라서 setUp(), tearDown(), __init__()는 테스트 당 1번씩 실행됩니다.
- 테스트 건너뛰기는 단순히 skip() 데코레이터나 그것의 조건 변형 중 하나를 사용하거나, setUp()이나 테스트 메서드 안에서 TestCase.skipTest()를 호출하거나, SkipTest를 직접 발생시키면 됩니다.
### subtest
- 부분 테스트(subtest)를 사용하여 테스트 반복 구별 짓기
- 여러분의 테스트들이 아주 작은 부분에서만 다를 때, 예를 들어 몇몇 매개변수, unittest는 subTest() 컨텍스트 관리자를 사용하여 테스트 메서드의 바디 안에서 그것들은 구별 짓게 해줍니다.
```
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```

## test suite
- 테스트하려는 기능에 따라 테스트들을 같이 모아서 테스트 케이스 구현을 사용하는 것을 추천합니다. 이것을 위해 unittest는 메커니즘을 제공합니다: 테스트 묶음(test suite), 이것은 unittest의 TestSuite 클래스에 해당합니다. 대부분의 경우 unittest.main()이 테스트를 실행하기 위해 모듈의 모든 테스트 케이스를 수집하여 적절한 행동을 취할 것입니다.
```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

## coverage
- [Link](https://daco2020.tistory.com/260)
- sample (a.py)
  - ```
    import unittest

    class TestStringMethods(unittest.TestCase):

        def test_upper(self):
            self.assertEqual('foo'.upper(), 'FOO')

        def test_isupper(self):
            self.assertTrue('FOO'.isupper())
            self.assertFalse('Foo'.isupper())

        def test_split(self):
            s = 'hello world'
            self.assertEqual(s.split(), ['hello', 'world'])
            # check that s.split fails when the separator is not a string
            with self.assertRaises(TypeError):
                s.split(2)

    if __name__ == '__main__':
        unittest.main()
    ```
- pip install coverage
  - this is python ver 2
- coverage run -m unittest a     # if your file name is a.py
- coverage report
- coverage html 

# unittest.mock
- [mock object library](https://docs.python.org/ko/3/library/unittest.mock.html)
- mock은 테스트 스코프 내에서 모듈과 클래스 수준 어트리뷰트의 패치를 처리하는 patch() 데코레이터를 고유한 객체 생성을 위한 sentinel과 함께 제공합니다. 

## simple method
- patch() 데코레이터 / 컨텍스트 관리자는 테스트 대상 모듈에서 클래스나 객체를 쉽게 모킹할 수 있도록 합니다. 지정한 객체는 테스트 중에 모의 객체(또는 다른 객체)로 치환되고 테스트가 끝나면 복원됩니다:
```python
from unittest.mock import patch
@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
    module.ClassName1()
    module.ClassName2()
    assert MockClass1 is module.ClassName1
    assert MockClass2 is module.ClassName2
    assert MockClass1.called
    assert MockClass2.called
```
  - 참고 patch 데코레이터를 중첩할 때 모의 객체는 적용한 순서와 같은 순서로 데코레이트 되는 함수로 전달됩니다 (데코레이터가 적용되는 일반적인 파이썬 순서). 이것은 아래에서 위로 감을 뜻하므로, 위의 예에서 module.ClassName1에 대한 모의 객체가 먼저 전달됩니다.

- 데코레이터 patch()는 with 문에서 컨텍스트 관리자로 사용할 수도 있습니다:
```python
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, 2, 3)

mock_method.assert_called_once_with(1, 2, 3)
```

- 스코프 도중 딕셔너리에 값을 설정하고 테스트가 종료될 때 딕셔너리를 원래 상태로 복원하기 위한 patch.dict()도 있습니다:
```python
foo = {'key': 'value'}
original = foo.copy()
with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    assert foo == {'newkey': 'newvalue'}

assert foo == original
```

## magic method
- Mock은 파이썬 매직 메서드의 모킹을 지원합니다. 매직 메서드를 사용하는 가장 쉬운 방법은 MagicMock 클래스를 사용하는 것입니다. 다음과 같은 것을 할 수 있도록 합니다:
```python
mock = MagicMock()
mock.__str__.return_value = 'foobarbaz'
str(mock)   # 'foobarbaz'
mock.__str__.assert_called_with()
```

- Mock을 사용하면 함수(또는 다른 Mock 인스턴스)를 매직 메서드에 대입할 수 있고 적절하게 호출될 것입니다. MagicMock 클래스는 모든 매직 메서드(아마도, 모든 유용한 메서드)가 미리 만들어져 있는 Mock 변형일 뿐입니다.
- 다음은 평범한 Mock 클래스로 매직 메서드를 사용하는 예입니다:
```python
mock = Mock()
mock.__str__ = Mock(return_value='wheeeeee')
str(mock)   # 'wheeeeee'
```

## Mock 클래스
- Mock은 코드 전체에서 스텁과 테스트 이중화의 사용을 대체하기 위한 유연한 모의 객체입니다. 모의 객체는 콜러블이고 어트리뷰트에 액세스할 때 새 모의 객체로 어트리뷰트를 만듭니다 [1]. 같은 어트리뷰트에 액세스하면 항상 같은 모의 객체를 반환합니다. 모의 객체는 사용 방법을 기록하여, 코드가 모의 객체에 대해 수행한 작업에 대한 어서션을 만들 수 있도록 합니다.
- MagicMock은 Mock의 서브 클래스이며, 모든 매직 메서드가 미리 만들어져 사용할 준비가 되어있습니다. 콜러블이 아닌 변형도 있어서, 콜러블이 아닌 객체를 모킹할 때 유용합니다: NonCallableMock과 NonCallableMagicMock
- patch() 데코레이터를 사용하면 특정 모듈의 클래스를 Mock 객체로 쉽게 대체 할 수 있습니다. 기본적으로 patch()는 MagicMock을 생성합니다. patch()에 new_callable 인자를 사용하여 대체 Mock 클래스를 지정할 수 있습니다.

## 심화
- [Mocking하고자 하는 대상이 사용되는 곳을 경로로 잡아야한다](https://techblog.yogiyo.co.kr/%EB%8B%B9%EC%8B%A0%EC%9D%98-%EA%B0%9D%EC%B2%B4-mock%EC%9C%BC%EB%A1%9C-%EB%8C%80%EC%B2%B4%EB%90%98%EC%97%88%EB%8B%A4-98da3f8cba5b)
  - ![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8m0jlmI7o7yOs3AFY7iAag.png)
  - request_weather_api가 shopping_mall.utils 안에 선언/정의되어져있다고해도 , 이것을 사용할 곳이 shopping_mall/api.py 이면 사용하는 곳 기준인 @patch('shopping_mall.api.request_weather_api', return_value = { ... } ) 으로 선언해야 한다.
  - Detail Mocking 예제 Mocking 속의 Mocking : return_value.*.* 등과 같이 아래로 내려가면서 작성 필요
    - response.json() : method 같은 경우는 아래와 같이 두번 return_value 값을 작성해줘야한다.
      - ```requests_get_mock.return_value.json.return_value = {'amount': 70000, }```
    - Mock 객체 속 property [response.status_code]
      - ```requests_get_mock.return_value.status_code = HTTPStatus.OK```

# 기타
- [another good summary1](https://medium.com/@reetesh043/understanding-patch-decorators-in-pythons-unittest-framework-e802b2aa6f6d)