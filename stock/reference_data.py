'''
Author: spc
Email: hilqiqi0@foxmail.com
Date: 2024-03-04 22:43:53
LastEditors: spc
LastEditTime: 2024-03-04 22:44:24
FilePath: /stock/stock/reference_data.py
Description: 

Copyright (c) 2024 by spc, All Rights Reserved. 
'''
import pandas as pd

from util.tools import StockBase


class ReferenceData(StockBase):

    def get_top10_holders(self):
        """
        前十大股东
        接口：top10_holders
        描述：获取上市公司前十大股东数据，包括持有数量和比例等信息
        积分：需2000积分以上才可以调取本接口，5000积分以上频次会更高

        字段	            类型	描述
        ts_code	        str	TS股票代码
        ann_date	    str	公告日期
        end_date	    str	报告期
        holder_name	    str	股东名称
        hold_amount	    float	持有数量（股）
        hold_ratio	    float	占总股本比例(%)
        hold_float_ratio	float	占流通股本比例(%)
        hold_change	    float	持股变动
        holder_type	    str	股东类型
        :return:
        """
        print("前十大股东: top10_holders")

        df = self.pro.stock_basic()
        ts_codes = df['ts_code'].values

        all_df = pd.DataFrame()
        for index, ts_code in enumerate(ts_codes):
            print(index, ts_code, end=",")
            tmp_df = self.pro.top10_holders(ts_code=ts_code, start_date='20170101', end_date='20241231')
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)
            print("tmp_df.shape", tmp_df.shape)
            # break

        table_name = "top10_holders"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)


if __name__ == '__main__':
    print("stock data...")

    stock_data = ReferenceData(db_name="tushare_reference")
    stock_data.get_top10_holders()