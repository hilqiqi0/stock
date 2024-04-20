from collections import Counter

stock_one = {
    '市值': 100000,
    '持仓': 100,
    '市价': 50,
    '成本价': 45,
    '盈亏': 500,
    '盈亏比例': 0.05
}

import random


def generate_random_number(frequency=0.5):
    probability = random.random()  # 生成一个0到1之间的随机概率值

    if probability < frequency:
        return 1
    else:
        return -1


random_list = []
for i in range(100000):
    random_list.append(generate_random_number(frequency=0.8))

# print(random_list)
# 使用Counter统计列表中元素的出现频率
frequency_counter = Counter(random_list)

# 获取元素的出现频率
for element, element_count in frequency_counter.items():
    frequency = element_count / len(random_list)
    print(f"元素 {element} 出现的次数为 {element_count}  出现的频率为 {frequency}")


def round_decimal(number, decimal_places):
    decimal_format = "{:." + str(decimal_places) + "f}"
    rounded_number = decimal_format.format(number)
    return float(rounded_number)


# 示例使用
result = round_decimal(3.1415926, 3)
print(result)  # 输出: 3.142




market_price = 10  # 市场价

stock_position = 100  # 仓位
stock_sum = market_price * stock_position  # 股票市值
stock_cost = 10  # 股票成本

stock_cost_price = stock_cost/stock_position  # 股票成本价格

total_money = 1000  # 可用金额

total_start = total_money + stock_sum  # 开始总额 = 可用金额 + 股票市值

profit = 0
print("开始市值：", total_start)
print("--------------")
up_count = 0
down_count = 0
for i in range(1000):
    op = generate_random_number(frequency=0.4)  # 买卖
# for i in [1,-1]:
#     op = i

    if op == 1:
        percent = op * 0.01  # 涨幅
        up_count += 1
    else:
        percent = op * 0.02  # 跌幅
        down_count += 1
    print("涨跌：", percent)

    market_price += round_decimal(market_price * percent, 2)  # 当前价格
    market_price = round_decimal(market_price, 2)
    print("当前价格：", market_price)

    # 操作
    total_money += market_price * op
    print("可用金额：", total_money)
    stock_cost -= market_price * op
    print("总成本：", stock_cost)
    stock_position = stock_position - op
    print("当前仓位：", stock_position)
    stock_cost_price = stock_cost / stock_position
    print("成本价格：", stock_cost_price)

    stock_sum = market_price * stock_position
    print("股票市值：", stock_sum)
    total = total_money + stock_sum
    print("总市值：", total)
    print("赚了：", total-total_start)
    print("上涨了：", up_count)
    print("下跌了：", down_count)
    print("--------------")
    # print("成本：", total_money / current_position)
    # cost_value -= market_price * op
    #
    # tmp_position = position - op
    # cost_price = (position * cost_price + op * market_price) / tmp_position  # 成本
    #
    # position = tmp_position  # 仓位

    # print(op, position, cost_value,market_price, cost_price,)
