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
    
