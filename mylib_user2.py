
#모듈 가져오기
from modules.mylib import food

print(food.name)
food.cook()
food.eat()

from modules.mylib.food import name, cook, eat

print(name)
cook()
eat()

import bbb
bbb.add(1, 3)
print(bbb.add(1, 3)) 