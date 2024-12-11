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
    
    




