import os
import time

import tushare as ts

tushare_token = os.getenv("tushare_token")
ts.set_token(tushare_token)

# sina数据
# df = ts.realtime_quote(ts_code='000001.SH,600000.SH,000001.SZ')

while 1:
    print("##################################")
    df = ts.realtime_quote(ts_code='000001.SH,603896.SH')

    # print(df)

    for index, row in df.iterrows():

        # print(index, row["NAME"], row["TIME"], row["PRICE"])

        print("当前价格：{}  时间：{} ".format(row["PRICE"], row["TIME"]))

        if index != 0:
            print("竞价买：{}   竞价卖：{}".format(row["BID"], row["ASK"]))

            for i in range(5, 0, -1):
                print("卖{} {:<5}   {:>5}".format(i, row[f"A{i}_V"], row[f"A{i}_P"]))

            print("-------")
            for i in range(1, 6):
                print("买{} {:<5}   {:>5}".format(i, row[f"B{i}_V"], row[f"B{i}_P"]))

    time.sleep(3)

# num1 = 42
# num2 = 33
# message = f"{num1:<5}The number is {num2:>5}"
# print(message)

# 42   The number is    33
