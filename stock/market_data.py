'''
Author: spc
Email: hilqiqi0@foxmail.com
Date: 2024-02-25 14:31:39
LastEditors: spc
LastEditTime: 2024-02-25 14:35:04
FilePath: /stock/stock/market_data.py
Description: 

Copyright (c) 2024 by spc, All Rights Reserved. 
'''
from time import sleep

import pandas as pd

from util.tools import StockBase


class MarketData(StockBase):

    def get_daily(self):
        """
        A股日线行情
        接口：daily，可以通过数据工具调试和查看数据
        数据说明：交易日每天15点～16点之间入库。本接口是未复权行情，停牌期间不提供数据
        调取说明：120积分每分钟内最多调取500次，每次6000条数据，相当于单次提取23年历史
        描述：获取股票行情数据，或通过通用行情接口获取数据，包含了前后复权数据

        字段	        类型	说明
        ts_code 	str	股票代码
        trade_date	str	交易日期
        open	    float	开盘价
        high	    float	最高价
        low	        float	最低价
        close	    float	收盘价
        pre_close	float	昨收价
        change	    float	涨跌额
        pct_chg	    float	涨跌幅
        vol	        float	成交量
        amount	    float	成交额
        :return:
        """
        print("A股日线行情: daily")

        df = self.pro.trade_cal(exchange='', start_date='20240305', end_date='20240305')
        cal_date_list = df[df["is_open"] == 1]["cal_date"].values

        all_df = self.pro.daily(trade_date=cal_date_list[0])
        # print(all_df)
        for trade_date in cal_date_list[1:]:
            print("trade_date: ", trade_date)
            tmp_df = self.pro.daily(trade_date=trade_date)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)

        table_name = "daily"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_daily_basic(self):
        """
        每日指标
        接口：daily_basic，可以通过数据工具调试和查看数据。
        更新时间：交易日每日15点～17点之间
        描述：获取全部股票每日重要的基本面指标，可用于选股分析、报表展示等。

        字段          	类型	说明
        ts_code 	    str	TS股票代码
        trade_date  	str	交易日期
        close	        number	当日收盘价
        turnover_rate	number	换手率
        turnover_rate_f	number	换手率(自由流通股)
        volume_ratio	number	量比
        pe	            number	市盈率（总市值/净利润）
        pe_ttm	        number	市盈率（TTM）
        pb	            number	市净率（总市值/净资产）
        ps	            number	市销率
        ps_ttm	        number	市销率（TTM）
        dv_ratio	    number	股息率（%）
        dv_ttm	        number	股息率（TTM） （%）
        total_share     number	总股本
        float_share	    number	流通股本
        free_share	    number	自由流通股本
        total_mv	    number	总市值
        circ_mv	        number	流通市值
        limit_status	int	涨跌停状态
        :return:
        """
        print("每日指标: daily_basic")

        df = self.pro.trade_cal(exchange='', start_date='20240305', end_date='20240305')
        cal_date_list = df[df["is_open"] == 1]["cal_date"].values

        column_names ="ts_code,trade_date,close,turnover_rate,turnover_rate_f,volume_ratio,pe,pe_ttm,pb,ps,ps_ttm,dv_ratio,dv_ttm,total_share,float_share,free_share,total_mv,circ_mv,limit_status"
        all_df = self.pro.daily_basic(ts_code='', trade_date=cal_date_list[0], fields=column_names)
        # print(all_df)
        # column_names_list = all_df.columns.tolist()
        # print(",".join(column_names_list))
        # return
        for trade_date in cal_date_list[1:]:
            print("trade_date: ", trade_date)
            tmp_df = self.pro.daily_basic(ts_code='', trade_date=trade_date, fields=column_names)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)

        table_name = "daily_basic"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_moneyflow(self):
        """
        个股资金流向
        接口：moneyflow，可以通过数据工具调试和查看数据。
        描述：获取沪深A股票资金流向数据，分析大单小单成交情况，用于判别资金动向，数据开始于2010年。
        限量：单次最大提取6000行记录，总量不限制

        字段	           类型	说明
        ts_code	        str	TS代码
        trade_date	    str	交易日期
        buy_sm_vol	    int	小单买入量（手）
        buy_sm_amount	float	小单买入金额（万元）
        sell_sm_vol	    int	小单卖出量（手）
        sell_sm_amount	float	小单卖出金额（万元）
        buy_md_vol	    int	中单买入量（手）
        buy_md_amount	float	中单买入金额（万元）
        sell_md_vol	    int	中单卖出量（手）
        sell_md_amount	float	中单卖出金额（万元）
        buy_lg_vol	    int	大单买入量（手）
        buy_lg_amount	float	大单买入金额（万元）
        sell_lg_vol	    int	大单卖出量（手）
        sell_lg_amount	float	大单卖出金额（万元）
        buy_elg_vol	    int	特大单买入量（手）
        buy_elg_amount	float	特大单买入金额（万元）
        sell_elg_vol	int	特大单卖出量（手）
        sell_elg_amount	float	特大单卖出金额（万元）
        net_mf_vol	    int	净流入量（手）
        net_mf_amount	float	净流入额（万元）
        trade_count	    int	交易笔数
        :return:
        """
        print("个股资金流向: moneyflow")

        df = self.pro.trade_cal(exchange='', start_date='20240101', end_date='20240226')
        cal_date_list = df[df["is_open"] == 1]["cal_date"].values

        column_names = 'ts_code,trade_date,buy_sm_vol,buy_sm_amount,sell_sm_vol,sell_sm_amount,buy_md_vol,buy_md_amount,sell_md_vol,sell_md_amount,buy_lg_vol,buy_lg_amount,sell_lg_vol,sell_lg_amount,buy_elg_vol,buy_elg_amount,sell_elg_vol,sell_elg_amount,net_mf_vol,net_mf_amount,trade_count'
        all_df = self.pro.moneyflow(trade_date=cal_date_list[0], fields=column_names)
        # column_names_list = all_df.columns.tolist()
        # print(",".join(column_names_list))
        # return
        for trade_date in cal_date_list[1:]:
            print("trade_date: ", trade_date)
            tmp_df = self.pro.moneyflow(trade_date=trade_date, fields=column_names)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)

        table_name = "moneyflow"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_moneyflow_hsgt(self):
        """
        沪深港通资金流向
        接口：moneyflow_hsgt，可以通过数据工具调试和查看数据。
        描述：获取沪股通、深股通、港股通每日资金流向数据，每次最多返回300条记录，总量不限制。每天18~20点之间完成当日更新

        字段	        类型	说明
        trade_date	str	交易日期
        ggt_ss	    str	港股通（上海）
        ggt_sz	    str	港股通（深圳）
        hgt	        str	沪股通
        sgt	        str	深股通
        north_money	str	北向资金
        south_money	str	南向资金
        :return:
        """
        print("沪深港通资金流向: moneyflow_hsgt")

        df = self.pro.moneyflow_hsgt(start_date='20240101', end_date='20240226')

        table_name = "moneyflow_hsgt"
        res = self.mysql_write_data(df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_hsgt_top10(self):
        """
        沪深股通十大成交股
        接口：hsgt_top10
        描述：获取沪股通、深股通每日前十大成交详细数据，每天18~20点之间完成当日更新

        字段	        类型	说明
        trade_date	str	交易日期
        ts_code	    str	股票代码
        name	    str	股票名称
        close	    float	收盘价
        change	    float	涨跌幅
        rank	    str	资金排名
        market_type	str	市场类型（1：沪市 3：深市）
        amount	    float	成交金额
        net_amount	float	净成交金额
        buy	        float	买入金额
        sell	    float	卖出金额
        :return:
        """
        print("沪深股通十大成交股: hsgt_top10")

        df = self.pro.trade_cal(exchange='', start_date='20240101', end_date='20240226')
        cal_date_list = df[df["is_open"] == 1]["cal_date"].values

        all_df = self.pro.hsgt_top10(trade_date=cal_date_list[0])
        # print(all_df)
        # return
        for trade_date in cal_date_list[1:]:
            print("trade_date: ", trade_date)
            tmp_df = self.pro.hsgt_top10(trade_date=trade_date)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)

        table_name = "hsgt_top10"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_bak_daily(self):
        """
        备用行情
        接口：bak_daily
        描述：获取备用行情，包括特定的行情指标(数据从2017年中左右开始，早期有几天数据缺失，近期正常)
        限量：单次最大7000行数据，可以根据日期参数循环获取，正式权限需要5000积分。

        字段	            类型	说明
        ts_code	        str	股票代码
        trade_date	    str	交易日期
        name	        str	股票名称
        pct_change	    float	涨跌幅
        close	        float	收盘价
        change	        float	涨跌额
        open	        float	开盘价
        high	        float	最高价
        low	            float	最低价
        pre_close	    float	昨收价
        vol_ratio	    float	量比
        turn_over	    float	换手率
        swing	        float	振幅
        vol         	float	成交量
        amount      	float	成交额
        selling	        float	外盘
        buying	        float	内盘
        total_share	    float	总股本(万)
        float_share	    float	流通股本(万)
        pe	            float	市盈(动)
        industry	    str	所属行业
        area	        str	所属地域
        float_mv	    float	流通市值
        total_mv	    float	总市值
        avg_price	    float	平均价
        strength	    float	强弱度(%)
        activity	    float	活跃度(%)
        avg_turnover	float	笔换手
        attack	        float	攻击波(%)
        interval_3	    float	近3月涨幅
        interval_6	    float	近6月涨幅
        :return:
        """
        print("备用行情: bak_daily")

        df = self.pro.trade_cal(exchange='', start_date='20240101', end_date='20240226')
        cal_date_list = df[df["is_open"] == 1]["cal_date"].values

        all_df = self.pro.bak_daily(trade_date=cal_date_list[0])
        # print(all_df)
        # print(all_df.shape)
        # return
        for trade_date in cal_date_list[1:]:
            print("trade_date: ", trade_date, end="; ")
            tmp_df = self.pro.bak_daily(trade_date=trade_date)
            print("tmp_df.shape: ", tmp_df.shape)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)

        table_name = "bak_daily"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)


if __name__ == '__main__':
    print("market data...")

    market_data = MarketData(db_name="tushare_market")
    # market_data.get_daily()
    market_data.get_daily_basic()
    # market_data.get_moneyflow()
    # market_data.get_moneyflow_hsgt()
    # market_data.get_hsgt_top10()
    # market_data.get_bak_daily()