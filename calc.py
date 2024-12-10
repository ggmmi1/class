import calc_module

print(calc_module.add(1,2))
print(calc_module.sub(1,2))
print(calc_module.mul(1,2))
print(calc_module.div(1,2))

#add만 가져오기
from calc_module import add
print(add(1,2))
#calc_module.add() #안 됨

import calc_module as cm
print(cm.add(1,2))

import math
print(math.floor(3.141592)) #내림 3
print(math.ceil(3.141592)) #올림 4
print(math.sqrt(9))

from math import floor, ceil
print(floor(3.141592))
print(ceil(3.141592))
#math. 사용 가능한 함수들 촤라락 나옴

#표준 모듈 = random 모듈
import random 
print(random.randint(1,5))
print(random.uniform(1,5))
print(random.random())
print(random.randrange(1,5))
print(random.randrange(1,5,2))