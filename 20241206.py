#함수 기본 매개변수
def pr_str(txt, count=1, count2=2): 
    for i in range(count):
        print(txt)
        print(count2)
        
pr_str("Hello", 3, 2)
pr_str("Hello", 3)
print()
pr_str("Hello")
print()
# pr_str() #txt='12'

print(1,2,3,4)
pr_str("234", count2=2)

#함수의 가변 매개변수
def calc_avg(*numbers): #numbers 가변 인자로 여러개의 값을 튜플로 묶어서 함수에 전달
    # print(type(numbers)) 
    print(numbers)  #numbers의 타입 출력
    return sum(numbers)/len(numbers)

print(calc_avg(1,2)) #결과 1.5
print(calc_avg(1,2,3,4,5)) #결과 3.0

def a ():
    return 1,2
print(a())


#가변 키워드 매개변수
def introduce(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    for i in kwargs:
        print(f"{i}")
        
introduce(name="Alice", age=25, city="New York")

#sorted
list = [2,4,1,4,6]
list.sort()
print("list", list)
list2 = [2,4,1,4,6]
print("sorted list2", sorted(list2))
print("list2", list2)

# 3번째로 작은 값의 인덱스를 구하라
# 정렬하고 그 값을 원본에서 찾으면 된다. 이문제가 있을때 sort()쓰면 안 됨.

print(eval("1+2"))

#함수 사용하지 않고 반올림 하는 방법 0.5 더하가 
print(int(4.6+0.5)) 

print(round(4.5))
print(round(2.547))
print(round(2.547, 1))
print(round(2.547, 2))
print(round(127, -1))
print(round(127, -2))

#제곱 방법
print(2**3) #1
print(pow(2,3)) #2

# 재귀함수 - 자기 자신을 호출
def hello():
    print("hello")
    hello()
    
hello()  #이와 같이 하면 무한 반복되기 때문에 종료조건을 만들어야 함

#종료 조건 설정하기 
def hello():
    global cnt
    cnt += 1
    if cnt<4: #종료 조건 필수
        print("Hello")
        hello()
cnt = 0
hello()

#팩토리얼 구하기
n = 5  #반복문 1
fac = 1
for i in range(1, n+1):
    fac *= i
print(fac)
     
def fac(n): #재귀함수 이용 2
    if n == 1:   
        return 1
    return n * fac(n-1)
print(fac(5))

#실습 재귀 함수호 피보나치 구하기 
#조건 F_n = F_n-1 + F_n-2
# F_1 = F_2 = 1 
#피보나치 수  tn 1,1,2,3,5,8,13, ...

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(10))

#위에는 300과 같은 큰 수를 넣었을때 오래 걸림 최적화 방법
#방법 2 반복문 이용



def fibo(n):
    if n <= 2:
        return 1
    
    a, b = 1, 1  
    for _ in range(3, n + 1):
        a, b = b, a + b  
    return b

print(fibo(1))   
print(fibo(4))   
print(fibo(300)) 

#방법 3 memory 이용
memory = {1: 1, 2: 1}  # 초기화

def fibo_memoization(n):
    if n in memory:  # 메모리에 이미 값이 있으면 반환
        number = memory[n]
    else:  # 없으면 계산해서 메모리에 저장
        number = fibo_memoization(n-1) + fibo_memoization(n-2)
        memory[n] = number  # 계산한 값을 메모리에 저장
    return number

print(fibo_memoization(300))  # 300번째 피보나치 수 출력

#람다식
#일반함수
add = lambda x,y:x+y #add는 함수가 됨
print(type(add))
print(add(1,2))  #함수도 변수에 넣을 수 있다.

def add2(x,y):
    return x+y

add3 = add2
print(add2(1,2))
print(add3(1,2))


#람다 함수를 매개 변수로 전달하기   

def call_3(func):
    for i in range(3):
        func()
        
call_3(lambda:print("hi") )
call_3(lambda:print("hello") )

#callback

def download( startCallback, endedCallback):
    startCallback()
    #download
    print("download 중")
    endedCallback()
    
download(lambda:print("다운로드 시작."), lambda:print("완료되었습니다."))

#map
list(map(int, {"1", "2", "3"}))

result = map(lambda x:3*x, [1,2,3,4])
print(list(result))


#람다 filter() #주어진 함수를 반복 가능한 객체의 각 요소에 적용하여 그 결과가 True인 요소들만 필터링하여 새로운 리스트를 생성하는 함수
li = [ -5,1,2,-11,76]

value = list(filter(lambda x:x<0, li))    
print(value) #[-5, -11]

value = list(filter(lambda x:x>10, li))    
print(value) #[-5, -11]

#실습 li = [-5,1,2,-11,76] 2배 후 3 이상인 것만 출력 1줄로
li = [-5,1,2,-11,76]

print(list(filter(lambda x: x >= 3, map(lambda x: x * 2, li))))

#실습 li = [-5,1,2,-11,76] 2배 후 3 이상인 것만 출력 1줄로
li = [-5,1,2,-11,76]

print(list(filter(lambda x: x >= 3, map(lambda x: x * 2, li))))


#코딩 테스트1 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다. 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(arr):
    result = []  
    for num in arr:  
        if num >= 50 and num % 2 == 0:  
            result.append(num // 2)  
        elif num < 50 and num % 2 != 0:  
            result.append(num * 2)  
        else:
            result.append(num)  
    return result  

#코딩 테스트2 문자열 myString이 주어집니다. myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(myString):
    return[len(s) for s in myString.split('x')]

#코딩 테스트3 어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.
# 문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.
def solution(str1, str2):
    answer = 0
    
    if str1 in str2:
        answer = 1
    
    return answer
       