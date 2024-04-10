'''
Author: spc
Email: hilqiqi0@foxmail.com
Date: 2024-02-24 11:45:49
LastEditors: spc
LastEditTime: 2024-02-24 16:00:18
FilePath: /stock/util/tools.py
Description: 

Copyright (c) 2024 by spc, All Rights Reserved. 
'''
from typing import Literal

import pandas as pd
import tushare as ts

import os

from sqlalchemy import create_engine, inspect, DDL, MetaData, Table, PrimaryKeyConstraint, text


def get_tushare_pro():
    tushare_token = os.getenv("tushare_token")
    ts.set_token(tushare_token)
    pro = ts.pro_api()
    return pro


def get_tushare_mysql_engine(db_name):
    tushare_mysql_engine = create_engine('mysql://root@127.0.0.1:3306/{}?charset=utf8&use_unicode=1'.format(db_name))
    return tushare_mysql_engine


class StockBase(object):
    def __init__(self, db_name):
        self.db_name = db_name

        self.pro = get_tushare_pro()
        self.engine = get_tushare_mysql_engine(db_name)

    def init_date(self):
        start_date = '20240101'
        end_date = '20240410'

        return start_date, end_date

    def print_test(self):
        print(self.db_name)

    def mysql_table_check_primary_key(self, table_name):

        with self.engine.connect() as con:
            check_sql_statement = text('SHOW CREATE TABLE {}'.format(table_name))
            check_result = con.execute(check_sql_statement)

            for check_row in check_result:
                # print(check_row)

                if "PRIMARY KEY" not in check_row[1]:
                    alter_sql_statement = text('ALTER TABLE {} ADD PRIMARY KEY (id)'.format(table_name))
                    alter_result = con.execute(alter_sql_statement)
                    # print(alter_result)
                    if alter_result.rowcount == 0:
                        # print("The result set is empty.")
                        pass
                    else:
                        for row in alter_result:
                            print(row)

                    alter_result.close()

            # Close the result set
            check_result.close()

    def mysql_write_data(self, frame,
                         name: str,
                         if_exists: Literal["fail", "replace", "append"] = "fail",
                         index: bool = True,
                         index_label=None,
                         schema: str | None = None,
                         chunksize: int | None = None,
                         **engine_kwargs):
        # frame.to_sql('stock_basic', self.engine, index=False, if_exists='append', chunksize=5000)
        # return
        result = frame.to_sql(name, self.engine,
                              index=index, index_label=index_label,
                              if_exists=if_exists, chunksize=chunksize)

        if index and index_label == "id":
            self.mysql_table_check_primary_key(table_name=name)

        return result

    def get_last_day_of_quarters(self, start_date, end_date):
        """
        获取指定时间范围的季度，最后一天

        # 使用示例
        start_date = pd.Timestamp(2023, 1, 1)
        end_date = pd.Timestamp(2023, 12, 31)
        last_days = self.get_last_day_of_quarters(start_date, end_date)

        # 打印各个季度的最后一天
        for last_day in last_days:
            print(last_day)

        :param start_date:
        :param end_date:
        :return:
        """
        # 创建一个包含起始日期和结束日期的日期范围
        date_range = pd.date_range(start=start_date, end=end_date, freq='QE')

        # 获取各个季度的最后一天
        last_days = [pd.Timestamp(date.year, date.month, 1) + pd.offsets.QuarterEnd() for date in date_range]

        return [last_day.strftime("%Y%m%d") for last_day in last_days]


class DemoStock(StockBase):
    def get_info(self):
        print(self.db_name)


if __name__ == '__main__':
    demo = DemoStock("db_demo")
    demo.print_test()
