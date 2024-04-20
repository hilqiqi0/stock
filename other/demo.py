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
for i in range(10):
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
    sum += value * count_op * -1

    print("本次操作: ", value_op, ";当前价格：", value, ";计数：", count, ";剩余：", sum, ";总价值：", sum + value * count, "赚了：", 2828*2 - (sum + value * count))



stock_list = [
    {"stock_count": 100,      # 股票数量
     "stock_value": 28.28,      # 当前价格
     "stock_old": 28.28,        # 成本价
     "stock_sum": 2828,
     "stock_profit": 0,
     }
]

money_values = 1000   # 现金
stock_values = 0      # 股票市值
total = stock_values + money_values   # 账户总额



def get_value(stock_list):
    stock_values = 0
    for stock in stock_list:
        stock_sum = stock["stock_sum"]


stocks = [
    {
        'Market Value': 100000,
        'Position': 100,
        'Market Price': 50,
        'Cost Price': 45,
        'Profit/Loss': 500,
        'Profit/Loss Ratio': 0.05
    },
    {
        '市值': 100000,
        '持仓': 100,
        '市价': 50,
        '成本价': 45,
        '盈亏': 500,
        '盈亏比例': 0.05
    }
]





