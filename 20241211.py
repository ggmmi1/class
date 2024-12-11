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