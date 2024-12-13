#바이러니 파일 
with open ("./output/input.txt", "wb") as f:
    txt = "드론이 비행한다."
    f.write(txt.encode()) #encode 암호화
    
with open ("./output/input.txt", "rb") as f2:
    data = f2.read()
    print(data)
    print(data.decode()) #decode 복구화
    
with open ("./output/idea.png", "rb") as f1:
    img = f1.read()
    
with open ("./output/idea1.png", "wb") as f2:
    f2.write(img)



#예외처리 예시
try:
    num = int(input("정수 입력"))
except ValueError:
    print("정수가 아님! 정수를 입력해줏세요")
     
#예외처리 예시 2
try:
    num = int(input("정수 입력"))
except ValueError as msg:
    print(msg)
    
#예외처리 예시 3
try:
    num = int(input("정수 입력"))
except:
    print("정수가 아님!")
     
#예외처리 예시 4
try:
    num = int(input("정수 입력"))
except Exception as msg:
    print(msg)
    
#다중예외처리 예시 1
try:
    num = int(input("정수 입력"))
except Exception as msg:
    print(msg)
else:
    print("예외 없음")

#다중예외처리 예시 2
try:
    num = int(input("정수 입력"))
except IndexError as msg:
    print("IndexError", msg)
except ValueError as msg:
    print("ValueError", msg)
except Exception as msg:  #부모자식같은 에러인 경우 순서가 중요하다. 
    print("Exception", msg) #보통 Exception 아래 있는게 좋음 
else:
    print("예외 없음")  

#실습 정수 입력 받기, 사용자가 제대로된 정수 입력할 때까지 반복하여 입력 받기
while True:
    try:
        num = int(input("숫자 입력"))
        print(f"정수 입력 성공!")
        break
    except ValueError:
        print("정수가 아님! 정수를 입력해주세요!")

#예외처리 finally 구문 
while True:
    try:
        num = int(input("숫자 입력"))
        print(f"정수 입력 성공!")
        break
    except ValueError:
        print("정수가 아님! 정수를 입력해주세요!")
    finally:
        print("귤의 붙어있는 이름은 귤락")  #break, continue 상관없이 구문을 벗어날때 무조건 실행

#강제 예외 발생 raise 사용 1
a = 1
try:
    a+=1
    raise Exception #강제로 에러 발생 시키는 방법 특정위치에서 raise걸면 어디서 에러가 났는지 확인 가능 
    a+=2
    print("a",a)
except:
    print("error",a)


 #강제 예외 발생 raise 사용 2
class Animal:
    def breathe(self):
        print("숨을 쉰다.")
        
    def cry(self):
        raise NotImplementedError
class Dog(Animal):
    def sleep(self):
        print("행니미가 잠을 잔다.")
    def cry(self):
        print("으르릉 왈")
        
d = Dog()
d.breathe()
d.cry() 