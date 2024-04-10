import math
import random

# for i in range(10):
#     r = random.randint(0,1)
#     print(r)


count = 100
value = 28.28
sum = 2828

# for r in [0,1]:
# for r in [1,0]:
for i in range(1000):
    r = random.randint(0, 1)
    if r:
        value_op = round(value * 0.01, 2)
        count_op = -1
    else:
        value_op = - round(value * 0.01, 2)
        count_op = +1

    value += value_op
    count += count_op
    value = round(value, 2)
    sum += value*count_op * -1

    print("本次操作: ", value_op, ";当前价格：", value, ";计数：", count, ";剩余：", sum , ";总价值：",sum+value*count)
