'''
Author: spc
Email: hilqiqi0@foxmail.com
Date: 2024-04-11 17:46:25
LastEditors: spc
LastEditTime: 2024-04-11 17:50:16
FilePath: /stock/stock/feature_data.py
Description: 

Copyright (c) 2024 by spc, All Rights Reserved. 
'''
import pandas as pd

from util.tools import StockBase


class FeatureData(StockBase):
    
    def get_limit_list_d(self):
        """
        涨跌停列表（新）
        接口：limit_list_d
        描述：获取沪深A股每日涨跌停、炸板数据情况，数据从2020年开始（不提供ST股票的统计）
        限量：单次最大可以获取1000条数据，可通过日期或者股票循环提取
        积分：5000积分每分钟可以请求200次每天总量1万次，8000积分以上每分钟500次每天总量不限制，具体请参阅

        字段	            类型	说明
        trade_date	    str	交易日期
        ts_code	        str	股票代码
        industry	    str	所属行业
        name	        str	股票名称
        close	        float	收盘价
        pct_chg	        float	涨跌幅
        swing	        float	振幅
        amount	        float	成交额
        limit_amount	float	板上成交金额
        float_mv	    float	流通市值
        total_mv	    float	总市值
        turnover_ratio	float	换手率
        fd_amount	    float	封单金额
        first_time	    str	首次封板时间
        last_time	    str	最后封板时间
        open_times	    int	炸板次数
        up_stat	        str	涨停统计
        limit_times	    int	连板数
        limit	        str	D跌停U涨停Z炸板
        :return:
        """
        print("涨跌停列表（新）: limit_list_d")

        df = self.pro.stock_basic()
        ts_codes = df['ts_code'].values

        column_names = "trade_date,ts_code,industry,name,close,pct_chg,swing,amount,limit_amount,float_mv,total_mv,turnover_ratio,fd_amount,first_time,last_time,open_times,up_stat,limit_times,limit"
        all_df = pd.DataFrame()
        for index, ts_code in enumerate(ts_codes):
            print(index, ts_code, end=",")
            tmp_df = self.pro.limit_list_d(ts_code=ts_code, fields=column_names)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)
            print("tmp_df.shape", tmp_df.shape)
            # break

        table_name = "limit_list_d"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)


if __name__ == '__main__':
    print("feature data...")
    feature_data = FeatureData(db_name="tushare_feature")
    feature_data.get_limit_list_d()

    