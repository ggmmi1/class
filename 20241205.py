# for ~ in range 
dan = 3
a = []
for i in range(1,10):
    a.append(dan * i)
    print(f"{dan} x {i} = {a[i-1]}")

# for ~ in 리스트 
dan = [[3, 1],
       [3, 2],
       [3, 3],
       [3, 4],
       [3, 5],
       [3, 6],
       [3, 7],
       [3, 8],
       [3, 9]
]
for x, y in dan:
    print(f"{x}*{y}={x*y}")
    
# for ~ in ??
dan = [[3, 1],
       [3, 2],
       [3, 3],
       [3, 4],
       [3, 5],
       [3, 6],
       [3, 7],
       [3, 8],
       [3, 9]
]
for i in dan:
    print(f"{i[0]} * {i[1]} = {i[0]*i[1]}")

#함수
def f(x):
    result = x**2 + 2*x +1
    return result

print(f(3))

#함수 기본 구조
def say_hello():
    print("hello")
    print("hello")
    print("hello")
say_hello()

#변수 범위
x = 10    #전역변수
def func():
    #같은 이름의 변수 선언시
    x = 20  #x는 func의 지역 변수
    print(x) #func의 지역 변수 출력
    
func()
print(x)  #전역 변수 출력

#변수 범위
x = 10    
def func2():
    print("func2",x)

def func():
    x = 20  
    print("func",x)   
    func2()
    
func()
print("main", x)  

func2()

def func3(x):
    print("func3", x)

func3(3)

#실습1 두 수(2,2)를 매개변수 전달하여 서로 같으면 곱하고, 서로 다르면 더하는 함수를 정의하고 호출하는 프로그램을 작성하시오
def func(x,y):
    if x == y:
        print(f"결과(곱하기): {x*y}")
    else:
        print(f"결과(더하기): {x+y}")
func(2,2)
func(2,3)

#실습2 주문 상품 가격이 2만원 미만이면 배송비 2500 포함이고, 아니면 배송비를 포함하지 않는 프로그램
def func(x,y):
    if x*y < 20000:
        return x*y + 2500
    else:
        return x*y
a = int(input("개당 가격: "))
b = int(input("수량: "))
print(f"총합: ", func(a,b),"원")
        
#리스트를 매개변수로 새로운 리스트 만등기
def times(a):
    a2 = [i*2 for i in a]
    return a2

v2 = times([1,2,3,4,5])
print(v2)

#여러개
def sum_mul(a,b):
    sum = a+b
    mul = a*b
    return sum, mul

s,m = sum_mul(2,3)
print(s, m)

#실습3 자판기 프로그램 함수화

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
#조건 1
def check_machine():
    print(f"남은 음료수:{vending_machine}")
    
#조건2
def is_drink():
    bev = input("원하는 음료")
    if bev in vending_machine:
        print(f"{bev}가 있습니다.")
    else:
        print(f"{bev}가 없어요")

#조건 3
def add_drink(beverage):
    print(f"{beverage}를 추가")
    vending_machine.append(beverage)
    print(f"남은 음료수:{vending_machine}")
    
#조건 4
def remove_drink(beverage):
    if beverage in vending_machine:
        print(f"{beverage}를 삭제")
        vending_machine.remove(beverage)
    else:
        print(f"{beverage}는 없어요")
    print(f"남은 음료수:{vending_machine}")  
    
check_machine()
is_drink()
add_drink("콜라")
remove_drink("생수")  



#실습4 백준 10828
import sys
line = int(sys.stdin.readline())

stack = []
for i in range(line):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            
#실습 4 함수 이용
import sys
input = sys.stdin.readline 

n = int(input().strip())
stack = []

def push(p):
    stack.append(p)

def pop():
    if len(stack) != 0:
        print(stack.pop())
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) != 0:
        print(stack[-1])  
    else:
        print(-1)

for _ in range(n):
    command = input().strip().split()
    if command[0] == 'push' and len(command) > 1:  
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'top':
        top()


#전역 변수의 유효 범위
def oneUp():
    global x
    x = x + 1
    return x

x = 0
print(oneUp())
print(oneUp())
print(oneUp())



#실습5 1-30까지의 자연수 중 배수와 배수의 개수를 계산하는 함수를 정의

import glob

def c(n):
    global count
    count = 0
    for i in range(1, 31):
        if i % n == 0:
            print(i, end=" ")
            count += 1
            
    print(f"{n}의 배수 개수: {count}")
c(3)


   
