#calendar 모듈
import calendar

calendar.prcal(2025) #년도 달력 표기
calendar.prmonth(2024, 12) #해당 월 표기
calendar.weekday(2024,12,11) #해당 요일 표기 



#날짜로 요일 알아내기
import datetime
import calendar

days = ["월", "화", "수", "목", "금", "토", "일"]

weekday = datetime.date.today().weekday()
print(weekday)
print("오늘은" + days[weekday]+ "요일")

the_day = datetime.date(2024, 12, 25).weekday()
print(the_day)
print("크리스마스는" + days[the_day]+"요일")

#날짜로 요일 알아내기 함수로 정의 
def get_weekday(yyyy, m, dd):
    days = ["월", "화", "수", "목", "금", "토", "일"]
    idx = datetime.date(yyyy, m, dd).weekday()
    print("{}년, {}월, {}일, {}요일".format(yyyy, m, dd, days[idx]))
get_weekday(2024,12,24)

#타임 모듈 
import time

a= time.time()
time.sleep(2)
b = time.time()
print(b-a)

print(time.localtime())
time_str = time.localtime()
print(time_str.tm_year)

print(time.ctime()) #ctime 시간을 바꿔주는 것 
print(time.ctime(a))
print(time.ctime(b))

#1970년 1월 1일 기준 
year = round(time.time()/(365*24*60*60)) #년을 초로 만들어 주는 것 
print(year)
day = time.time()/(24*60*60)
print(day)

#수행시간 측정하기
import time
start = time.time()

for i in range(10):
    print(i)
    time.sleep(1)
    
end = time.time()
print(f"수행시간: {end-start}초")


#수행시간 측정하기
import time
start = time.time()

for i in range(10):
    print(i)
    time.sleep(1)
    
end = time.time()
print(f"수행시간: {end-start}초") 

#수행시간 측정하기 함수 변경
def check_time(func):
    start = time.time()
    func()
    end = time.time()
    print(f"수행시간: {end-start}초") 
    
def a():
    for i in range(10):
        print(i)
        time.sleep(1)
        
def b():
    for i in range(100):
        print(i)
        time.sleep(0.5)

check_time(a)


# 파일 쓰기 w
f = open("test.txt", "w") #test.txt 경로, "w" 모드 
f.write("Hello world\n") #여기서 ! 추가하면 기존 것ㅇ디 사라지고 수정된 것민 남아있음 한마디로 처음부터 다시 
f.close()

#파일 입출력 r
f2 = open("test.txt") #어디서 실행하는지 중요함 위치가 어딘지는 중요하지 않음
print(f2.read())
f2.close()

#파일 입출력 a #데이터 추가 

f3 = open("test.txt", "a")
f3.write("hello World22\n")
f3.close() #닫아주기 필수 같은 파일일 경우 

#readline 한 줄 읽기
f2 = open("test.txt") 
print(f2.readline(), end="") 
f2.close()