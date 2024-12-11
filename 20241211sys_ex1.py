#import sys

print(sys.argv)

args = sys.argv[1:]
print(args)

#사용자가 입력한 모든 숫자를 더하는 프로그램을 만들어라 (argv 이용)
import sys

args = sys.argv[1:]
sum = 0

for i in args:
    sum += int(i)

print(sum)   

#실습 3개를 입력 받는데 mul이면 두 수를 곱하고 add면 두 수를 더해라
# ex) a.py mul 2 3 
# 6
#a. py add 4 5
# 9
#입력이 2개 이하거나 4개 이상이면 오류 처리

import sys

args = sys.argv

if (len(args)!=4):
   print("Error")


else:
    cmd = args[1]
    num1 = int(args[2])
    num2 = int(args[3])
    if cmd == "mul":
        print(num1+num2)
    elif cmd == "add":
        print(num1+num2)

        
#sys.exit(0) 고쳐보기
import sys

args = sys.argv

if (len(args)!=4):
   print("Error")
   sys.exit(0)
        

cmd = args[1]
num1 = int(args[2])
num2 = int(args[3])
if cmd == "mul":
    print(num1*num2)
elif cmd == "add":
    print(num1+num2)

#모듈 
import os

os.chdir("//Users//gyeongmi//Desktop//codingg//python")
dir = os.popen ("git status")
print(dir.read())
print(os.listdir)

#실습 타자연습 게임
import random
import time

word = ["sky", "earth", "moon", "flower", "tree", "apple", "grape", "garlic", "onion", "potato"]

n = 1

input("[타자 게임] 준비되면 엔터하슈~")
start = time.time() 

while n < 11:
    print("문제", n)
    question = random.choice(word)
    print(question)
    user = input()
    if question == user:
        print("통과!")
        n += 1
    else:
        print("오타~,~ 다시 도전하세용!!")
        
end = time.time()
et = end - start
print(f"타자 시간: {et: .2f}초")


    





