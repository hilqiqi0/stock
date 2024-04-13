'''
Author: spc
Email: hilqiqi0@foxmail.com
Date: 2024-02-24 11:26:52
LastEditors: spc
LastEditTime: 2024-04-13 14:56:24
FilePath: /stock/stock/basic_data.py
Description: 

Copyright (c) 2024 by spc, All Rights Reserved. 
'''
from time import sleep

import pandas as pd

from util.tools import StockBase


class StockData(StockBase):

    # def read_data():
    #     sql = """SELECT * FROM stock_basic LIMIT 20"""
    #     df = pd.read_sql_query(sql, engine_ts)
    #     return df

    def get_stock_basic(self):
        """
        基础信息
        接口：stock_basic，可以通过数据工具调试和查看数据
        描述：获取基础信息数据，包括股票代码、名称、上市日期、退市日期等

        字段	类型	说明
        ts_code 	str	TS代码
        symbol  	str	股票代码
        name	    str	股票名称
        area	    str	地域
        industry	str	所属行业
        fullname	str	股票全称
        enname	    str	英文全称
        cnspell	    str	拼音缩写
        market	    str	市场类型
        exchange	str	交易所代码
        curr_type	str	交易货币
        list_status	str	上市状态 L上市 D退市 P暂停上市
        list_date	str	上市日期
        delist_date	str	退市日期
        is_hs	    str	是否沪深港通标的，N否 H沪股通 S深股通
        act_name	str	实控人名称
        act_ent_type	str	实控人企业性质
        :return:
        """
        print("基础信息：stock_basic")

        column_names = "ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,curr_type,list_status,list_date,delist_date,is_hs,act_name,act_ent_type"
        df = self.pro.stock_basic(exchange='', list_status='L', fields=column_names)

        table_name = "stock_basic"
        res = self.mysql_write_data(df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_trade_cal(self):
        """
        交易日历
        接口：trade_cal，可以通过数据工具调试和查看数据。
        描述：获取各大交易所交易日历数据,默认提取的是上交所
        :return:
        """

        print("交易日历：trade_cal")

        start_date, end_date = self.init_date()
        # df = self.pro.trade_cal(exchange='', start_date='20180101', end_date='20250101')
        df = self.pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)

        table_name = "trade_cal"
        res = self.mysql_write_data(df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_name_change(self):
        """
        股票曾用名
        接口：namechange
        描述：历史名称变更记录
        :return:
        """

    def get_hs_const(self):
        """
        沪深股通成份股
        接口：hs_const
        描述：获取沪股通、深股通成分数据
        :return:
        """

    def get_stock_company(self):
        """
        上市公司基本信息
        接口：stock_company，可以通过数据工具调试和查看数据。
        描述：获取上市公司基础信息，单次提取4500条，可以根据交易所分批提取\

        字段	        类型	说明
        ts_code	    str	股票代码
        exchange	str	交易所代码SSE上交所 SZSE深交所
        chairman	str	法人代表
        manager	    str	总经理
        secretary	str	董秘
        reg_capital	float	注册资本
        setup_date	str	注册日期
        province	str	所在省份
        city	    str	所在城市
        introduction	str	公司介绍
        website	    str	公司主页
        email	    str	电子邮件
        office	    str	办公室
        ann_date	str	公告日期
        business_scope	str	经营范围
        employees	int	员工人数
        main_business	str	主要业务及产品

        :return:
        """
        print("上市公司基本信息：stock_company")

        column_names = 'ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,ann_date,business_scope,employees,main_business'
        # 交易所代码 ，SSE上交所 SZSE深交所 BSE北交所
        df_sse = self.pro.stock_company(exchange='SSE', fields=column_names)
        df_szse = self.pro.stock_company(exchange='SZSE', fields=column_names)
        df_bse = self.pro.stock_company(exchange='BSE', fields=column_names)

        df = pd.concat([df_sse, df_szse], ignore_index=True)
        df = pd.concat([df, df_bse], ignore_index=True)

        table_name = "stock_company"
        res = self.mysql_write_data(df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_stk_managers(self):
        """
        上市公司管理层
        接口：stk_managers, 单次最大返回4000
        描述：获取上市公司管理层

        字段	类型	说明
        ts_code	    str	TS股票代码
        ann_date	str	公告日期
        name	    str	姓名
        gender	    str	性别
        lev	        str	岗位类别
        title	    str	岗位
        edu	        str	学历
        national	str	国籍
        birthday	str	出生年份
        begin_date	str	上任日期
        end_date	str	离任日期
        resume	    str	个人简历
        :return:
        """
        print("上市公司管理层: stk_managers")

        df = self.pro.stock_basic()
        ts_codes = df['ts_code'].values

        column_names = 'ts_code,ann_date,name,gender,lev,title,edu,national,birthday,begin_date,end_date,resume'

        # 获取单个公司高管全部数据
        # all_df = self.pro.stk_managers(ts_code=ts_codes[0], fields=column_names)
        # column_names_list = all_df.columns.tolist()
        # print(",".join(column_names_list))
        # print("tmp_df.shape: ", all_df.shape[0])

        ts_code_list = []
        data_size_max = 0
        all_df = pd.DataFrame()
        for index, ts_code in enumerate(ts_codes):
            ts_code_list.append(ts_code)

            if len(ts_code_list) == 50:  # 单次最大返回4000行，所有需要控制单次请求数量；当前记录max为2976个
                # 获取多个公司高管全部数据
                tmp_df = self.pro.stk_managers(ts_code=",".join(ts_code_list), fields=column_names)

                data_size_max = max(tmp_df.shape[0], data_size_max)
                print("tmp_df.shape: ", tmp_df.shape, ", data_size_max: ", data_size_max)
                all_df = pd.concat([all_df, tmp_df], ignore_index=True)
                ts_code_list = []
                print("index ts_code: ", index)
                # break

        if len(ts_code_list) > 0:
            # 获取多个公司高管全部数据
            tmp_df = self.pro.stk_managers(ts_code=",".join(ts_code_list))
            data_size_max = max(tmp_df.size, data_size_max)
            print("tmp_df.size: ", tmp_df.size, ", data_size_max: ", data_size_max)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)

        table_name = "stk_managers"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_stk_rewards(self):
        """
        管理层薪酬和持股
        接口：stk_rewards
        描述：获取上市公司管理层薪酬和持股
        :return:
        """

    def get_new_share(self):
        """
        IPO新股列表
        接口：new_share
        描述：获取新股上市列表数据
        限量：单次最大2000条，总量不限制
        :return:
        """

    def get_bak_basic(self):
        """
        备用列表
        接口：bak_basic
        描述：获取备用基础列表，数据从2016年开始
        限量：单次最大7000条，可以根据日期参数循环获取历史，

        字段	            类型	说明
        trade_date	    str	交易日期
        ts_code	        str	TS股票代码
        name	        str	股票名称
        industry	    str	行业
        area	        str	地域
        pe	            float	市盈率（动）
        float_share	    float	流通股本（万）
        total_share	    float	总股本（万）
        total_assets	float	总资产（万）
        liquid_assets	float	流动资产（万）
        fixed_assets	float	固定资产（万）
        reserved	    float	公积金
        reserved_pershare	float	每股公积金
        eps	            float	每股收益
        bvps	        float	每股净资产
        pb	            float	市净率
        list_date	    str	上市日期
        undp	        float	未分配利润
        per_undp	    float	每股未分配利润
        rev_yoy	        float	收入同比（%）
        profit_yoy	    float	利润同比（%）
        gpr	            float	毛利率（%）
        npr	            float	净利润率（%）
        holder_num	    int	股东人数
        :return:
        """
        print("备用列表: bak_basic")

        # df = self.pro.trade_cal(exchange='', start_date='20240101', end_date='20240228')
        start_date, end_date = self.init_date()
        df = self.pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)
        cal_date_list = df[df["is_open"] == 1]["cal_date"].values

        all_df = pd.DataFrame()
        for index, trade_date in enumerate(cal_date_list):
            print("trade_date: ", trade_date)
            tmp_df = self.pro.bak_basic(trade_date=trade_date)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)

        table_name = "bak_basic"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)


if __name__ == '__main__':
    print("stock data...")

    stock_data = StockData(db_name="tushare_stock")

    stock_data.get_stock_basic()
    # stock_data.get_trade_cal()
    stock_data.get_stock_company()
    stock_data.get_stk_managers()
    stock_data.get_bak_basic()
