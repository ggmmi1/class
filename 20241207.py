#함수 안에 함수 가능
def b():
    def c():
        print("c")
    c()
b()

#리스트를 문자로 변환
1 = ["p", "y", "t","h","o","n"]
print("".join(1)) #.join 기준을  합친것 

#코딩 테스트 1
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

#함수 선언 
def solution(arr, divisor): #arr: 정수 배열(숫자들이 모인 리스트) divisor: 나누는 기준이 되는 정수 
    #결과를 저장할 빈 리스트 생성
    answer = [] # 이 리스트는 조건에 맞는 숫자들(즉, divisor로 나누어떨어지는 숫자들)을 저장하는 역할로 처음에는 아무 값도 없으므로 빈 리스트로 시작
    
    for num in arr: #arr의 원소를 하나씩 꺼내 변수 num에 저장하여 반복문 , 예를 들어, arr = [5, 9, 12]라면, num은 차례대로 5, 9, 12가 된다.
        if num % divisor == 0: #현재 숫자 num을 divisor로 나눈 나머지가 0인지 확인, 나머지가 0이면, num은 divisor로 나누어떨어진다는 뜻이다.
            answer.append(num) #조건을 만족하는 숫자 num을 answer리스트에 추가
            
    if len(answer) == 0: #answer 리스트의 길이가 0인지 확인, divisor로 나누어 떨어지는 숫자가 하나도 없다는 뜻
            answer = [-1] #결과로 [-1]을 반환하도록 리스트 [-1]로 설정
            
    return sorted(answer) #sorted(answer): answer리스트를 오름차순으로 정렬, retrun:최동결과 확인

#다른 방법으로 예시
print (1 if 1<0 else 0)
print("abc" if 1<0 else "bcd" )

if 1<0:
    print("abc")
else:
    print("bcd")


#코딩 테스트 2
#정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)): #j가 항상 i+1로 시작하도록 설정 : 동일한 인덱스에서 숫자를 선택하지 않도록 하기 위함
            answer.append(numbers[i] + numbers[j]) #두 수를 더하고 결과를 저장
    answer = sorted(set(answer)) #set(answer)리스트를 집합 자료형으로 변환하여 중복된 값을 제거/sorted 중복이 제거된 집합을 다시 리스트 변환, 오름차순으로 정렬 
                                 #set은 순서를 보장하지 않아 sorted 사용
    return answer

#다른 방법
def solution(numbers):
    answer = set()
    l = len(numbers)
    for i in range(l-1):
        for j in range(i+1, l):
            answer.add(numbers[i]+numbers[j])
    return sorted(answer)
            

#코딩 테스트 3 
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성

def solution(x):
    n = sum(int(num) for num in str(x))  #str(x)는 x를 문자열로 바꾸는 과정 #for 반복문은 str(x)에서 각 자릿수를 하나씩 가져온다. ex) x = 18 일 경우 str(18)은 num = '1'과 num = '8'을 차례대로 가져옴 int(num) 정수로 변환
    if x % n != 0: # %나머지를 구하는 연산자 x % n은 x를 n으로 나눈 나머지 , 나머지가 0이 아니면 false를 반환
        answer = False
    else:
        answer = True
    return answer

#다른 방법 
def solition(x):
    s = str(x)
    sum = 0
    for i in s:
        sum += int(i)
    return x % sum == 0   


# 코딩 테스트 4
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요. s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

def solution(s):
    sor = sorted(s, reverse=True) #sorted 주어진 리스트 정렬해 새로운 리스트를 반환, reverse=True 내림차순 정렬
    answer = ''.join(sor) #join() 함수는 리스트의 요소들을 하나의 문자열로 합치는 함수입니다.''.join(sorted_s)는 sorted_s 리스트에 있는 문자들을 하나로 합쳐서 문자열을 만듭니다.예를 들어, sorted_s = ['Z', 'r', 'b', 'a', 'e']라면 ''.join(sorted_s)는 "Zrbae"를 반환합니다.
    return answer

#다른 방법
def solution(s):
    return ''.join(sorted(s, reverse=True))

#zip 사용 방법
a =[1,2,3,4]
b = ["a","b","c","d"]
c = list(zip(a,b))
print(c)
d = dict(zip(a,b))
print(d)

# 코딩 테스트 5 #추억 점수

def solution(name, yearning, photo):
    answer = []
    info = dict(zip(name, yearning)) #zip(name, yearning) 두 리스트를짝지어 튜플 생성, dict() 이용하여 튜플들을 딕셔너리로 변환
    
    for people in photo: #배열의 각 사진을 순차적으로 처리하는 반복문
        score = 0 #각 사진에 등장하는 사람들의 그리움 점수를 합산하려면 score를 0으로 초기화 하고 그리운 점수 더해 나간다
        
        for person in people:
            score += info.get(person, 0) #info.get(person, 0)는 info 딕셔너리에서 person(사람)에 해당하는 그리움 점수를 가져온다.
        answer.append(score) #그리움 점수를 score에 더해준다.
        
    return answer

# 다른 방법

def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for people in photo:  
        score = 0
        
        for person in people:  
            score += dic.get(person, 0)  
        
        answer.append(score)  
    
    return answer


# 코딩 테스트 6 #숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.예를 들어, t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.

def solution(t, p):
    answer = 0
    lp = len(p)  
    
    for i in range(len(t) - lp + 1):
         if t[i:i+lp] <= p:
            answer += 1
    return answer