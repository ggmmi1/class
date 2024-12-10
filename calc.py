#datetime 모듈 시간
import datetime

now = datetime.datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)

print(f"{now.hour}시 {now.minute}분 {now.second}초")
  
#datetime 나이가 100세 되는 해의 연도 계산하기 프로그램  
import datetime
today  = datetime.datetime.today()
print(today.year)

age = int(input("나이 입력: "))

result = today.year + (100 -age)
print("100세 되는 해는 " + str(result)+ "년 입니다.")

#datetime 지난 날짜 
print("지금까지 몇 일?")
first_day = datetime.date.today(2024, 11, 25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)
print(f"개강 이후 {passed_time.days}일 지났습니다.")








    
