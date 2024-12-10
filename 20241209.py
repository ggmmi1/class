#코딩 테스트 콜라츠 수열 만들기 
def solution(n):
    def collat(x, sequence):
        sequence.append(x)  
        if x == 1: 
            return sequence
        elif x % 2 == 0:  
            return collat(x // 2, sequence)
        else: 
            return collat(3 * x + 1, sequence)

 
    answer = collat(n, [])
    return answer

#클래스 선언
a = dict() #클래스 만드는 방법
a = set() #이것도 클래스임

class b:
    pass #아무것도 안하고 넘어가겠다.

c = b() # c=객체(붕어빵 틀) b=클래스(붕어빵)
c2 = b()
c3 = b() 

#필드: 클래스를 정의할때 정의되는 변수
class Movie:
    title = "해리포터"
movie1 = Movie()
movie2 = Movie()

print(movie1.title)
print(movie2.title)
    
movie1.title = "인터스텔라"
print(movie1.title)
print(movie2.title)

#클래스 함수 메소드
class Movie:
    name = ''
    
    def print_msg(msg):
        print(msg)
    def modify(self, movie):
        self.name = movie
    def print_name(self):
        print(self.name)
        
    
movie1 = Movie()
movie2 = Movie()

Movie.print_msg("print 하기") 
# Movie.modify(movie1, "print 하기")
movie1.modify("print 하기3") #self는 자동 할당 
movie1.print_name()
movie2.modify("print하기4")
print("movie2.name", movie2.name)

#클래스 생성자
class Movie:
    def __init__(self):
        print("Hello")
        
movie = Movie()
   
#매개 변수가 있는 생성자 
class Movie:
    count = 0 #없어도 동작 가능 
    
    #def __init__(self, title="오징어게임", audence=300)
    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        
movie1 = Movie("해리포터",100)
movie2 = Movie("해리포터",200)

print(movie1.title, movie1.audience)
print(movie2.title, movie2.audience)

#movie3 = Movie() 위에 def 오겜을 넣으면 이걸로 출력 가능 

#클래스 변수, 인스턴스 변수
class Movie:
    count = 0 #클래스 변수 
    
    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        Movie.count += 1
        
movie1 = Movie("해리포터",100)
print(Movie.count)
movie2 = Movie("해리포터",200)

print(movie1.count)
print(movie2.count)
print(Movie.count)
Movie.count +=1
print(movie1.count)
print(movie2.count)
print(Movie.count)

#접근제어 __ 활용
class Movie:
    count = 0 #클래스 변수 , 모든 인스턴스에서 공유 
    
    def __init__(self, title, audience): # __init__은 생성자로 객체가 생성될 때 호출 
        self.__title = title #self.__title , self.__audience 는 인스턴스 변수  각 객체마다 고유하게 값을 가짐
        self.__audience = audience # __(더블 언더스코어)로 시작하는 변수는 프라이빗 변수로 외부에서 직접 접근할 수 없게 보호 
        Movie.count += 1 #Movie.count 클래스 변수로 새로운 객체가 생성될 때마다 1씩 증가 
        
    def get_title(self): #get_title, get_audienc getter 메서드는 프라이빗한 인스턴스 변수에 간접적으로 접근하기 위하여 사용 예를 들어 movie1.get_title()을 호출하면 movie1의 __title 값을 반환
        return self.__title #setter 매서드는 프라이빗한 인스턴스 변수의 값을 변경하기 위해 사용, 외부에서 직접 변수에 젒근하지 않고 메서드를 통해 데이터 수정을 허용
    def set_title(self, title):
        self.__title = title
    def get_audience(self):
        return self.__audience
        
movie1 = Movie("해리포터", 100) #movie1 객체를 생성하면서 __init__ 메서드 호출 , #두번째 인자인 100은 audience라는 매개 변수로 전달, 이값은 괸객수 또는 특정 속성의미 데이터 
#print(movie1.__title)
print(movie1.get_title())
#movie1.__title = "오겜" #__title 이용해서 새로 만든 것 (새로운 변수 생성) 그래서 바뀌지 않고 위에 해리포터랑 오겜도 같이 출력이 됨
#print(movie1.get_title())
#print(movie1.__title)
#print(movie1.__audience)
print(movie1.get_audience())

#실습 
class Myadd:
    __a = 1
    __b = 2
    
    def sum(self): # __a, __b의 합을 변환하는 메서드 #self는 클래스 내부에서 정의된 메서드가 호출된 특정 개체의 속성이나 메서드에 접근하기 위한 방법 __a, __b는 특정개체이기 때문에 self활용
        return self.__a + self.__b
        
    def set_a(self,a):
        self.__a = a
        
a = Myadd()
print(a.sum()) #3 #__a = 1, __b = 2 -> 출력3

a.set_a(3) #_a값 3으로 변경
print(a.sum()) #5

#정보 은닉 건강상태 클래스 만들기
class Health:
    def __init__(self, name):
        self.__name =name
        self.__hp = 100
    
    def get_name(self):
        return self.__name
    
    def setHp(self, hp):
        hp = max(hp, 0)
        hp = min(hp, 100)
        self.__hp =hp
        
    def getHp(self):
        return "hp: " + str(self.__hp)
    
    def exercise(self, hours):
        self.setHp(self.__hp + hours)
        print("{}시간 운동하다".format(hours))
        
    def drink(self, cups):
        self.setHp(self.__hp - cups)
        print("술을 {}잔 마시다".format(cups))
        
p1 = Health("나몸짱")
p1.setHp(100)
p1.exercise(5)
p1.drink(2)
print(f"{p1.get_name()} - {p1.getHp()}")
    
    
p2 = Health("나약")
p2.setHp(10)
p2.exercise(1)
p2.drink(12)
print(f"{p2.get_name()} - {p2.getHp()}")

#실습 1 사칙연산 클래스 만들기 
class FourCal:
    def __init__(self, a, b): #조건 1 인스턴스를 생성할 때 2개의 숫자를 class에 보낸다.
        self.__a = a
        self.__b = b
        
    def add(self): #조건 2 add 메서드는 두 수를 더한 결과물을 반환힌다.
        return self.__a + self.__b 
    def sub(self): #조건 3 sub 메서드는 두 수를 뺀 결과값을 반환한다.
        return self.__a - self.__b
    def mul(self): #조건 4 mul 메서드는 두 수를 곱한 결과값을 반환한다.
        return self.__a * self.__b
    def div(self): #조건 5 div 메서드는 두 수를 나눈 결과값을 반환한다.
        if self.__b == 0:
            return "None"
        return self.__a / self.__b
        
  
        
n = FourCal(4, 0)
print(n.add())
print(n.sub())
print(n.mul())
print(n.div())

#사번 자동 부여
class Employee:
    serial_num = 1000
    
    def __init__(self, name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name
        
    def __str__(self):
        return "사번 : {}, 이름 : {}" .format(self.id, self.name)
    
e1 = Employee("최사원")
print(e1)
  
e2 = Employee("안사원")
print(e2)

e3 = Employee("한사원")
print(e3)   
    
#객체 리스트
employee = [
    
    Employee('구름'),
    Employee('별'),
    Employee('행성'),
    Employee('달')
]

for i in employee:
     print(i)
     