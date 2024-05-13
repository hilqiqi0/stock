import pandas as pd
from sqlalchemy import create_engine

engine_ts = create_engine('mysql://root@127.0.0.1:3306/tushare_stock?charset=utf8&use_unicode=1')

sql = """SELECT ts_code, name
          FROM tushare_stock.stock_basic 
          where name not like '%%ST%%'
          # limit 10
          """
df_stock = pd.read_sql_query(sql, engine_ts)
# print(df_stock)

for index, row in df_stock.iterrows():
    ts_code = row["ts_code"]
    # ts_code = '000888.SZ'
    # ts_code = '000005.SZ'

    # print(ts_code)

    sql = f"""SELECT ts_code, name, turn_over, trade_date, vol
              FROM tushare_market.bak_daily 
              where ts_code = '{ts_code}' 
              order by trade_date
--               limit 10
              """
    df_stock_one = pd.read_sql_query(sql, engine_ts)

    turn_over = 100
    turn_over_list = []
    start_date = ""
    for _, row_one in df_stock_one.iterrows():
        current_turn_over = row_one["turn_over"]
        if current_turn_over == 0.0:
            break
        if len(turn_over_list) == 0:
            if current_turn_over/turn_over > 2:
                turn_over_list.append(turn_over)
                turn_over_list.append(current_turn_over)
                start_date = row_one["trade_date"]
        elif len(turn_over_list) == 2:
            if current_turn_over/turn_over_list[0] > 4:
                turn_over_list.append(current_turn_over)
                # print(ts_code, "----------------------")
                # break
            else:
                turn_over_list = []
                start_date = ""

        else:
            if current_turn_over/turn_over_list[0] > 5:
                turn_over_list.append(current_turn_over)
                # print(ts_code, "^^^^^^^^^^^^^^")
                # break
            else:
                if len(turn_over_list) > 5:
                    print(row_one["name"], ts_code, start_date, turn_over_list)
                turn_over_list = []
                start_date = ""
                # break
        turn_over = current_turn_over
        # print(turn_over)
        # break


    # break
