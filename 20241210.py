#실습 Supermarket 클래스
#조건1 클래스를 선언할 때 인자로 location, name, product, customer 받기
#조건2 location: 위치, name:가게 이름, product:파는 물건, customer: 고객의 수

class Supermarket:
    count = 0

    def __init__(self, location, name, product, customer):
        self.__location = location
        self.__name = name
        self.__product = product
        self.__customer = int(customer)  # 문자열을 정수로 변환
        Supermarket.count += 1
        
    def print_location(self): #조건3 print_location(): 위치를 출력하는 함수
        print(f"위치 = {self.__location}")
        
    def change_category(self, product): #조건4 change_category(): 받은 인자로 파는 물건 바꾸는 함수
        self.__product = product
        
    def show_list(self): #조건5 show_list(): 현재 파는 물건 출력
        print(f"파는 물건 = {self.__product}")
        
    def enter_customer(self): #조건6 enter_customer(): 손님의 수를 1씩 늘리는 함수
        self.__customer += 1
        
    def show_info(self): #조건7 show_info(): 가게 이름, 위치, 파는 물건, 손님 수 모두 출력
        print(f"가게 이름 = {self.__name}, 위치 = {self.__location}, 파는 물건 = {self.__product}, 손님 수 = {self.__customer}")
        
    def show_supermarket_count(self): #조건8 show_supermarket_count(): 슈퍼마켓 클래스 인스턴스 개수 출력
        print(Supermarket.count)
          
        
mart = Supermarket('응암', '홈플러스', '멸칼', '100')  
mart.show_list()
mart.change_category('불닭')
mart.show_list()
mart.enter_customer()
mart.show_info()
mart.show_supermarket_count()

#클래스 상속
class Country:
    def __init__(self):
        self.name = "나라이름"
        self.population = "인구"
        self.capital = "수도"
        
    def show(self):
        print("국가 클래스의 메소드입니다")

class Korea(Country):
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print("국가 이름:",self.name)     
        
country = Korea("대한민국")
country.show()
print(country.name)
country.show_name()

#메서드 오버라이딩
class Country:
    def __init__(self):
        self.name = "나라이름"
        self.population = "인구"
        self.capital = "수도"
        
    def show(self):
        print("국가 클래스의 메소드입니다")

class Korea(Country):
    def __init__(self,name,population, capital):
        self.name = name
        self.population = population
        self.capital = capital
        
    def show_detail(self):
        print(f"국가의 이름은 {self.name}, 인구는 {self.population}, 수도는 {self.capital}")
           
        
country = Korea("대한민국", "5천만", "서울")
country.show_detail()

# 실습 2 다음과 같은 조건을 만족하는 MinLimitCalculator 클래스 만들기
#조건1 Calculator 클래스 상속 받는다.
#조건3 sub() 메서드를 오버라이딩 하여 2번 조건을 만족시킬 것 

class Calculator():
    def __init__(self):
        self.value = 100
        
    def sub(self, value):
        self.value -= value
        
class MinLimitCalculator(Calculator):
    def sub(self, value):
        if self.value - value < 0: #조건2 value 값이 음수가 안되게 제한한다.
            self.value = 0
        else:
            self.value -= value

cal = MinLimitCalculator()
cal.sub(20)  
cal.sub(90)  
print(cal.value)  




    
      
