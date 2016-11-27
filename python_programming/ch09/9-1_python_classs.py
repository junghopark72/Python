class BookReader:
    country = 'South Korea'
    def __init__(self, name):
        self.name = name
    def read_book(self):
        print(self.name + ' is reading a Book !!')


# 2.클래스 정의 및 불러오기
# __main__ : 현재 클래스가 생성된 위치 -> 파이썬 실행 최상단 레벨의 코드에서 실행됨
# self : 자바의 this 와 같은 의미이나 모든 method 선언시 첫번째 매개변수로 지정해야 됨

# 3.클래스 초기화 함수 __init__()
# __init__ : 객체 인스턴스 초기화 함수로 재정의(오버라이딩) 가능 -> 디폴트 매개변수 지정시 사용

# 4.클래스 변수와 인스턴스 변수
# 클래스 변수 : 모든 인스턴스에서 같은 값을 공유할 때 사용 가능 -> 객체마다 다른 값을 갖지 않는다.
# 인스턴스 변수 : 객체가 인스턴스화 될 때마다 새로운 값이 할당되며, 서로 다른 객체 간에는 값을 공유할 수 없다.

class Dog:
       
    def __init__(self, name):
        self.name = name
        self.tricks = []            # 인스턴스 변수 선언
    
    def add_trick(self, trick):
        self.tricks.append(trick)
