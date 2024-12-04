
#튜플 만들기
t1 = (10, 20, 30)
print(type(t1))
print(t1)
print(t1[0]) 
## del t1[0] 안 됨
## t1[0] = 3 인 됨
del t1

t2 = (10)
t3 = (10,)
t4 = 10,20
print(type(t4))

#셋 만들기
set1 = {1,2,3}
print(set1)
set2 = set([1,2,3,3])
print(set2)
set2.add(4)
print(set2)
while len(set2) > 0 :
    a = set2.pop()
    print(a)
#거꾸로 나타내기
l1 = [1,2,3,4]
while len(l1) > 0 :
    a = l1.pop()
    print(a)
#정렬인데 랜덤 
set3 = set("apple")
print(set3)
while len(set3) > 0 :
    a = set3.pop()
    print(a)
    
#set 응용
name = ["1","2","3","2"]

for i in range(len(name)):
    if name.count(name[i]) > 1:
        print(name[i])
        #name.remove(name[i]) 제거하는 코드
        
name_set = set(name)
print(name_set)
name_list = list(name_set)
print(name_list)

#for 루프 이용해서 중복 제거하기 
n = ["1","2","3","2"]
a = []
for i in range(len(n)):
    if a.count(n[i]) < 1: #count랑 not in 같음 
       a.append(n[i])
n = a
print(n)

#딕셔너리
a = {}
print(type(a))
b = {1} #set()
print(type(b))
c = dict()
c = {1:'a','b':'b'}
print(c)
c[2] = 'c'
c['c'] = 2
print(c)
del c[2]
del c['b']
print(c)

# print(c[2])
print(c.get(2))
print(c.keys())
print(c.values())

for i in c.keys() :
    print(i, c.get(i))

# for i in c.valuse():
#     #print(i, c.get(i))

print('c' in c)  # print('c' in c.keys())
print(2 in c.values())

#딕셔너리 응용 실습1 
dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위", 
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간", 
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}

print("컴퓨터 사전")
word = input("검색할 단어:")
if word in dic:
    print(f'{word}: {dic[word]}')
else:
    print("정의된 단어가 없습니다.")

#실습1 get 활용
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
s={}
for _ in range(n):
    s[input()]=True
    
a=0
for _ in range(m):
    if s.get(input()) ==True:
        a+=1
print(a)

#실습1 set 이용
n,m=map(int,input().split())
s= set()
for i in range(n):
    s.add(input())
    
a=0
for i in range(m):
    str = input()
    if str in s:
        a += 1
print(a) 



 
#실습2 딕셔너리 사용    
students = {"Alice":85,"Bob":90,"Charlie":95}

print(students)

students["David"] = 80
students["Alice"] = 88
del(students["Bob"])
for student in students.keys():
    print(student,students[student])

#실습2-1 다른 방법
#학생 딕셔너리 작성
dict = {}
dict["Alice"] = 85
dict["Bob"] = 90
dict["Charlie"] = 95
print(dict)
#학생 추가 및 점수 수정
dict["David"] = 80
dict["Alice"] = 88
#학생 삭제
dict.pop("Bob")
print(dict)
#for문 이용하여 남은 학생 점수 나타내기
for student in dict:
    print(f"{student}의 점수는{dict.get(student)}")


#2차원 리스트
d = [
    [10,20],
    [30,40],
    [50,60]
]

print(d)
print(d[0][0])
print(d[1][1])
d.append([70,80])
print(d)
d[0][0] = 90
print(d)

# d[1].pop(1)
del(d[1][1])
print(d)
#print(d[1][1])
print(len(d))
print(len(d[0]))

for i in range(0,len(d)):
    for j in range(0,len(d[i])):
        print([i][j], end=" ")
    print()
    
for x, y in d:
    print(x,y)

