#range 範圍
#清單產生器
import random

#range(5) #[0, 1, 2, 3, 4]
range(2 , 10, 3) # [2, 5, 8]
range(10, 3, -2) #[10, 8, 6, 4]

for i in range(2, 5):
    r = random.randint(1, 100)
    print('這是第', i+1, '次產生隨機數', r)

for i in range(100):
    print('hi')

