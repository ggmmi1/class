        
#실습. 로또 번호 뽑기
#조건1 1~45까지의 수 중에서 랜덤으로 6개의 숫자를 뽑는다.
#조건2 6개의 숫자 중 중복되는 숫자가 없도록 한다.
#조건3 오름차순 정렬

import random

num = random.randint(1,45)
lotto = []

for i in range(6):
    while num in lotto:
        num = random.randint(1,45)
    lotto.append(num)
lotto.sort()
print(f"로또 {lotto}")
    


        









    
