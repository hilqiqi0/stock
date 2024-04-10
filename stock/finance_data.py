'''
Author: spc
Email: hilqiqi0@foxmail.com
Date: 2024-02-25 18:55:48
LastEditors: spc
LastEditTime: 2024-02-25 19:00:21
FilePath: /stock/stock/finance_data.py
Description: 

Copyright (c) 2024 by spc, All Rights Reserved. 
'''
import pandas as pd

from util.tools import StockBase


class FinanceData(StockBase):

    def get_income(self):
        """
        利润表
        接口：income，可以通过数据工具调试和查看数据。
        描述：获取上市公司财务利润表数据

        字段	                类型	说明
        ts_code	            str	TS代码
        ann_date	        str	公告日期
        f_ann_date	        str	实际公告日期
        end_date	        str	报告期
        report_type	        str	报告类型 1合并报表 2单季合并 3调整单季合并表 4调整合并报表 5调整前合并报表 6母公司报表 7母公司单季表 8 母公司调整单季表 9母公司调整表 10母公司调整前报表 11调整前合并报表 12母公司调整前报表
        comp_type	        str	公司类型(1一般工商业2银行3保险4证券)
        end_type	        str	报告期类型
        basic_eps	        float	基本每股收益
        diluted_eps	        float	稀释每股收益
        total_revenue	    float	营业总收入
        revenue	            float	营业收入
        int_income	        float	利息收入
        prem_earned	        float	已赚保费
        comm_income	        float	手续费及佣金收入
        n_commis_income	    float	手续费及佣金净收入
        n_oth_income	    float	其他经营净收益
        n_oth_b_income	    float	加:其他业务净收益
        prem_income	        float	保险业务收入
        out_prem	        float	减:分出保费
        une_prem_reser	    float	提取未到期责任准备金
        reins_income	    float	其中:分保费收入
        n_sec_tb_income	    float	代理买卖证券业务净收入
        n_sec_uw_income	    float	证券承销业务净收入
        n_asset_mg_income	float	受托客户资产管理业务净收入
        oth_b_income	    float	其他业务收入
        fv_value_chg_gain	float	加:公允价值变动净收益
        invest_income	    float	加:投资净收益
        ass_invest_income	float	其中:对联营企业和合营企业的投资收益
        forex_gain	        float	加:汇兑净收益
        total_cogs	        float	营业总成本
        oper_cost	        float	减:营业成本
        int_exp	            float	减:利息支出
        comm_exp	        float	减:手续费及佣金支出
        biz_tax_surchg	    float	减:营业税金及附加
        sell_exp	        float	减:销售费用
        admin_exp	        float	减:管理费用
        fin_exp	            float	减:财务费用
        assets_impair_loss	float	减:资产减值损失
        prem_refund	        float	退保金
        compens_payout	    float	赔付总支出
        reser_insur_liab	float	提取保险责任准备金
        div_payt	        float	保户红利支出
        reins_exp	        float	分保费用
        oper_exp	        float	营业支出
        compens_payout_refu	float	减:摊回赔付支出
        insur_reser_refu	float	减:摊回保险责任准备金
        reins_cost_refund	float	减:摊回分保费用
        other_bus_cost	    float	其他业务成本
        operate_profit	    float	营业利润
        non_oper_income 	float	加:营业外收入
        non_oper_exp	    float	减:营业外支出
        nca_disploss	    float	其中:减:非流动资产处置净损失
        total_profit	    float	利润总额
        income_tax      	float	所得税费用
        n_income	        float	净利润(含少数股东损益)
        n_income_attr_p	    float	净利润(不含少数股东损益)
        minority_gain	    float	少数股东损益
        oth_compr_income	float	其他综合收益
        t_compr_income	    float	综合收益总额
        compr_inc_attr_p	float	归属于母公司(或股东)的综合收益总额
        compr_inc_attr_m_s	float	归属于少数股东的综合收益总额
        ebit	            float	息税前利润
        ebitda	            float	息税折旧摊销前利润
        insurance_exp	    float	保险业务支出
        undist_profit   	float	年初未分配利润
        distable_profit	    float	可分配利润
        rd_exp	            float	研发费用
        fin_exp_int_exp	    float	财务费用:利息费用
        fin_exp_int_inc	    float	财务费用:利息收入
        transfer_surplus_rese	    float	盈余公积转入
        transfer_housing_imprest	float	住房周转金转入
        transfer_oth	            float	其他转入
        adj_lossgain	            float	调整以前年度损益
        withdra_legal_surplus	    float	提取法定盈余公积
        withdra_legal_pubfund	    float	提取法定公益金
        withdra_biz_devfund	        float	提取企业发展基金
        withdra_rese_fund	        float	提取储备基金
        withdra_oth_ersu	        float	提取任意盈余公积金
        workers_welfare	            float	职工奖金福利
        distr_profit_shrhder	    float	可供股东分配的利润
        prfshare_payable_dvd	    float	应付优先股股利
        comshare_payable_dvd	    float	应付普通股股利
        capit_comstock_div	        float	转作股本的普通股股利
        net_after_nr_lp_correct	    float	扣除非经常性损益后的净利润（更正前）
        oth_income	                float	其他收益
        asset_disp_income	        float	资产处置收益
        continued_net_profit	    float	持续经营净利润
        end_net_profit	            float	终止经营净利润
        credit_impa_loss	        float	信用减值损失
        net_expo_hedging_benefits	float	净敞口套期收益
        oth_impair_loss_assets	    float	其他资产减值损失
        total_opcost	            float	营业总成本2
        amodcost_fin_assets     	float	以摊余成本计量的金融资产终止确认收益
        update_flag	                str	更新标识
        :return:
        """

        print("利润表: income")

        # 使用示例
        start_date = pd.Timestamp(2000, 1, 1)
        end_date = pd.Timestamp(2024, 12, 31)
        last_days = self.get_last_day_of_quarters(start_date, end_date)

        column_names = 'ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,end_type,basic_eps,diluted_eps,total_revenue,revenue,int_income,prem_earned,comm_income,n_commis_income,n_oth_income,n_oth_b_income,prem_income,out_prem,une_prem_reser,reins_income,n_sec_tb_income,n_sec_uw_income,n_asset_mg_income,oth_b_income,fv_value_chg_gain,invest_income,ass_invest_income,forex_gain,total_cogs,oper_cost,int_exp,comm_exp,biz_tax_surchg,sell_exp,admin_exp,fin_exp,assets_impair_loss,prem_refund,compens_payout,reser_insur_liab,div_payt,reins_exp,oper_exp,compens_payout_refu,insur_reser_refu,reins_cost_refund,other_bus_cost,operate_profit,non_oper_income,non_oper_exp,nca_disploss,total_profit,income_tax,n_income,n_income_attr_p,minority_gain,oth_compr_income,t_compr_income,compr_inc_attr_p,compr_inc_attr_m_s,ebit,ebitda,insurance_exp,undist_profit,distable_profit,rd_exp,fin_exp_int_exp,fin_exp_int_inc,transfer_surplus_rese,transfer_housing_imprest,transfer_oth,adj_lossgain,withdra_legal_surplus,withdra_legal_pubfund,withdra_biz_devfund,withdra_rese_fund,withdra_oth_ersu,workers_welfare,distr_profit_shrhder,prfshare_payable_dvd,comshare_payable_dvd,capit_comstock_div,net_after_nr_lp_correct,oth_income,asset_disp_income,continued_net_profit,end_net_profit,credit_impa_loss,net_expo_hedging_benefits,oth_impair_loss_assets,total_opcost,amodcost_fin_assets,update_flag'
        all_df = pd.DataFrame()
        # 打印各个季度的最后一天
        for last_day in last_days:
            print(last_day, end=",")
            tmp_df = self.pro.income_vip(period=last_day, fields=column_names)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)
            print("tmp_df.shape", tmp_df.shape)
            # break

        table_name = "income"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_balancesheet(self):
        """
        资产负债表
        接口：balancesheet，可以通过数据工具调试和查看数据。
        描述：获取上市公司资产负债表

        字段	                类型	说明
        ts_code	            str	TS股票代码
        ann_date	        str	公告日期
        f_ann_date	        str	实际公告日期
        end_date	        str	报告期
        report_type	        str	报表类型
        comp_type	        str	公司类型(1一般工商业2银行3保险4证券)
        end_type	        str	报告期类型
        total_share	        float	期末总股本
        cap_rese	        float	资本公积金
        undistr_porfit	    float	未分配利润
        surplus_rese	    float	盈余公积金
        special_rese	    float	专项储备
        money_cap	        float	货币资金
        trad_asset	        float	交易性金融资产
        notes_receiv	    float	应收票据
        accounts_receiv	    float	应收账款
        oth_receiv	        float	其他应收款
        prepayment	        float	预付款项
        div_receiv	        float	应收股利
        int_receiv	        float	应收利息
        inventories	        float	存货
        amor_exp	        float	长期待摊费用
        nca_within_1y	    float	一年内到期的非流动资产
        sett_rsrv	        float	结算备付金
        loanto_oth_bank_fi	float	拆出资金
        premium_receiv	    float	应收保费
        reinsur_receiv	    float	应收分保账款
        reinsur_res_receiv	float	应收分保合同准备金
        pur_resale_fa	    float	买入返售金融资产
        oth_cur_assets	    float	其他流动资产
        total_cur_assets	float	流动资产合计
        fa_avail_for_sale	float	可供出售金融资产
        htm_invest	        float	持有至到期投资
        lt_eqt_invest   	float	长期股权投资
        invest_real_estate	float	投资性房地产
        time_deposits	    float	定期存款
        oth_assets	        float	其他资产
        lt_rec	            float	长期应收款
        fix_assets      	float	固定资产
        cip	                float	在建工程
        const_materials	    float	工程物资
        fixed_assets_disp	float	固定资产清理
        produc_bio_assets	float	生产性生物资产
        oil_and_gas_assets	float	油气资产
        intan_assets	    float	无形资产
        r_and_d	            float	研发支出
        goodwill	        float	商誉
        lt_amor_exp     	float	长期待摊费用
        defer_tax_assets	float	递延所得税资产
        decr_in_disbur	    float	发放贷款及垫款
        oth_nca	            float	其他非流动资产
        total_nca	        float	非流动资产合计
        cash_reser_cb	    float	现金及存放中央银行款项
        depos_in_oth_bfi	float	存放同业和其它金融机构款项
        prec_metals	        float	贵金属
        deriv_assets	    float	衍生金融资产
        rr_reins_une_prem	float	应收分保未到期责任准备金
        rr_reins_outstd_cla	float	应收分保未决赔款准备金
        rr_reins_lins_liab	float	应收分保寿险责任准备金
        rr_reins_lthins_liab	float	应收分保长期健康险责任准备金
        refund_depos	    float	存出保证金
        ph_pledge_loans	    float	保户质押贷款
        refund_cap_depos	float	存出资本保证金
        indep_acct_assets	float	独立账户资产
        client_depos	    float	其中：客户资金存款
        client_prov	        float	其中：客户备付金
        transac_seat_fee	float	其中:交易席位费
        invest_as_receiv	float	应收款项类投资
        total_assets	    float	资产总计
        lt_borr	            float	长期借款
        st_borr	            float	短期借款
        cb_borr	            float	向中央银行借款
        depos_ib_deposits	float	吸收存款及同业存放
        loan_oth_bank	    float	拆入资金
        trading_fl	        float	交易性金融负债
        notes_payable	    float	应付票据
        acct_payable	    float	应付账款
        adv_receipts	    float	预收款项
        sold_for_repur_fa	float	卖出回购金融资产款
        comm_payable	    float	应付手续费及佣金
        payroll_payable	    float	应付职工薪酬
        taxes_payable	    float	应交税费
        int_payable	        float	应付利息
        div_payable	        float	应付股利
        oth_payable	        float	其他应付款
        acc_exp	            float	预提费用
        deferred_inc	    float	递延收益
        st_bonds_payable	float	应付短期债券
        payable_to_reinsurer	float	应付分保账款
        rsrv_insur_cont	    float	保险合同准备金
        acting_trading_sec	float	代理买卖证券款
        acting_uw_sec	    float	代理承销证券款
        non_cur_liab_due_1y	float	一年内到期的非流动负债
        oth_cur_liab	    float	其他流动负债
        total_cur_liab	    float	流动负债合计
        bond_payable	    float	应付债券
        lt_payable	        float	长期应付款
        specific_payables	float	专项应付款
        estimated_liab	    float	预计负债
        defer_tax_liab	    float	递延所得税负债
        defer_inc_non_cur_liab	float	递延收益-非流动负债
        oth_ncl	            float	其他非流动负债
        total_ncl	        float	非流动负债合计
        depos_oth_bfi   	float	同业和其它金融机构存放款项
        deriv_liab	        float	衍生金融负债
        depos	            float	吸收存款
        agency_bus_liab	    float	代理业务负债
        oth_liab	        float	其他负债
        prem_receiv_adva	float	预收保费
        depos_received  	float	存入保证金
        ph_invest	        float	保户储金及投资款
        reser_une_prem	    float	未到期责任准备金
        reser_outstd_claims	float	未决赔款准备金
        reser_lins_liab	    float	寿险责任准备金
        reser_lthins_liab	float	长期健康险责任准备金
        indept_acc_liab	    float	独立账户负债
        pledge_borr	        float	其中:质押借款
        indem_payable	    float	应付赔付款
        policy_div_payable	float	应付保单红利
        total_liab	        float	负债合计
        treasury_share	    float	减:库存股
        ordin_risk_reser	float	一般风险准备
        forex_differ	    float	外币报表折算差额
        invest_loss_unconf	float	未确认的投资损失
        minority_int	    float	少数股东权益
        total_hldr_eqy_exc_min_int	float	股东权益合计(不含少数股东权益)
        total_hldr_eqy_inc_min_int	float	股东权益合计(含少数股东权益)
        total_liab_hldr_eqy	float	负债及股东权益总计
        lt_payroll_payable	float	长期应付职工薪酬
        oth_comp_income	    float	其他综合收益
        oth_eqt_tools	    float	其他权益工具
        oth_eqt_tools_p_shr	float	其他权益工具(优先股)
        lending_funds	    float	融出资金
        acc_receivable	    float	应收款项
        st_fin_payable	    float	应付短期融资款
        payables	        float	应付款项
        hfs_assets	        float	持有待售的资产
        hfs_sales	        float	持有待售的负债
        cost_fin_assets	    float	以摊余成本计量的金融资产
        fair_value_fin_assets	float	以公允价值计量且其变动计入其他综合收益的金融资产
        contract_assets	        float	合同资产
        contract_liab	        float	合同负债
        accounts_receiv_bill	float	应收票据及应收账款
        accounts_pay	        float	应付票据及应付账款
        oth_rcv_total	        float	其他应收款(合计)（元）
        fix_assets_total	    float	固定资产(合计)(元)
        cip_total	        float	在建工程(合计)(元)
        oth_pay_total	    float	其他应付款(合计)(元)
        long_pay_total	    float	长期应付款(合计)(元)
        debt_invest	        float	债权投资(元)
        oth_debt_invest 	float	其他债权投资(元)
        oth_eq_invest   	float	其他权益工具投资(元)
        oth_illiq_fin_assets	float	其他非流动金融资产(元)
        oth_eq_ppbond	    float	其他权益工具:永续债(元)
        receiv_financing	float	应收款项融资
        use_right_assets	float	使用权资产
        lease_liab	        float	租赁负债
        update_flag	        str	更新标识

        :return:
        """
        print("资产负债表: balancesheet")

        # 使用示例
        start_date = pd.Timestamp(2023, 1, 1)
        end_date = pd.Timestamp(2023, 12, 31)
        last_days = self.get_last_day_of_quarters(start_date, end_date)

        column_names = "ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,end_type,total_share,cap_rese,undistr_porfit,surplus_rese,special_rese,money_cap,trad_asset,notes_receiv,accounts_receiv,oth_receiv,prepayment,div_receiv,int_receiv,inventories,amor_exp,nca_within_1y,sett_rsrv,loanto_oth_bank_fi,premium_receiv,reinsur_receiv,reinsur_res_receiv,pur_resale_fa,oth_cur_assets,total_cur_assets,fa_avail_for_sale,htm_invest,lt_eqt_invest,invest_real_estate,time_deposits,oth_assets,lt_rec,fix_assets,cip,const_materials,fixed_assets_disp,produc_bio_assets,oil_and_gas_assets,intan_assets,r_and_d,goodwill,lt_amor_exp,defer_tax_assets,decr_in_disbur,oth_nca,total_nca,cash_reser_cb,depos_in_oth_bfi,prec_metals,deriv_assets,rr_reins_une_prem,rr_reins_outstd_cla,rr_reins_lins_liab,rr_reins_lthins_liab,refund_depos,ph_pledge_loans,refund_cap_depos,indep_acct_assets,client_depos,client_prov,transac_seat_fee,invest_as_receiv,total_assets,lt_borr,st_borr,cb_borr,depos_ib_deposits,loan_oth_bank,trading_fl,notes_payable,acct_payable,adv_receipts,sold_for_repur_fa,comm_payable,payroll_payable,taxes_payable,int_payable,div_payable,oth_payable,acc_exp,deferred_inc,st_bonds_payable,payable_to_reinsurer,rsrv_insur_cont,acting_trading_sec,acting_uw_sec,non_cur_liab_due_1y,oth_cur_liab,total_cur_liab,bond_payable,lt_payable,specific_payables,estimated_liab,defer_tax_liab,defer_inc_non_cur_liab,oth_ncl,total_ncl,depos_oth_bfi,deriv_liab,depos,agency_bus_liab,oth_liab,prem_receiv_adva,depos_received,ph_invest,reser_une_prem,reser_outstd_claims,reser_lins_liab,reser_lthins_liab,indept_acc_liab,pledge_borr,indem_payable,policy_div_payable,total_liab,treasury_share,ordin_risk_reser,forex_differ,invest_loss_unconf,minority_int,total_hldr_eqy_exc_min_int,total_hldr_eqy_inc_min_int,total_liab_hldr_eqy,lt_payroll_payable,oth_comp_income,oth_eqt_tools,oth_eqt_tools_p_shr,lending_funds,acc_receivable,st_fin_payable,payables,hfs_assets,hfs_sales,cost_fin_assets,fair_value_fin_assets,contract_assets,contract_liab,accounts_receiv_bill,accounts_pay,oth_rcv_total,fix_assets_total,cip_total,oth_pay_total,long_pay_total,debt_invest,oth_debt_invest,oth_eq_invest,oth_illiq_fin_assets,oth_eq_ppbond,receiv_financing,use_right_assets,lease_liab,update_flag"

        all_df = pd.DataFrame()
        # 打印各个季度的最后一天
        for last_day in last_days:
            print(last_day, end=",")
            tmp_df = self.pro.balancesheet_vip(period=last_day, fields=column_names)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)
            print("tmp_df.shape", tmp_df.shape)
            # break

        table_name = "balancesheet"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_cashflow(self):
        """
        现金流量表
        接口：cashflow，可以通过数据工具调试和查看数据。
        描述：获取上市公司现金流量表

        字段	                类型	说明
        ts_code	            str	TS股票代码
        ann_date	        str	公告日期
        f_ann_date	        str	实际公告日期
        end_date	        str	报告期
        comp_type	        str	公司类型(1一般工商业2银行3保险4证券)
        report_type	        str	报表类型
        end_type	        str	报告期类型
        net_profit	        float	净利润
        finan_exp	        float	财务费用
        c_fr_sale_sg	    float	销售商品、提供劳务收到的现金
        recp_tax_rends	    float	收到的税费返还
        n_depos_incr_fi	    float	客户存款和同业存放款项净增加额
        n_incr_loans_cb	    float	向中央银行借款净增加额
        n_inc_borr_oth_fi	float	向其他金融机构拆入资金净增加额
        prem_fr_orig_contr	float	收到原保险合同保费取得的现金
        n_incr_insured_dep	float	保户储金净增加额
        n_reinsur_prem	    float	收到再保业务现金净额
        n_incr_disp_tfa	    float	处置交易性金融资产净增加额
        ifc_cash_incr	    float	收取利息和手续费净增加额
        n_incr_disp_faas	float	处置可供出售金融资产净增加额
        n_incr_loans_oth_bank	float	拆入资金净增加额
        n_cap_incr_repur	float	回购业务资金净增加额
        c_fr_oth_operate_a	float	收到其他与经营活动有关的现金
        c_inf_fr_operate_a	float	经营活动现金流入小计
        c_paid_goods_s	    float	购买商品、接受劳务支付的现金
        c_paid_to_for_empl	float	支付给职工以及为职工支付的现金
        c_paid_for_taxes	float	支付的各项税费
        n_incr_clt_loan_adv	float	客户贷款及垫款净增加额
        n_incr_dep_cbob	    float	存放央行和同业款项净增加额
        c_pay_claims_orig_inco	float	支付原保险合同赔付款项的现金
        pay_handling_chrg	    float	支付手续费的现金
        pay_comm_insur_plcy	    float	支付保单红利的现金
        oth_cash_pay_oper_act	float	支付其他与经营活动有关的现金
        st_cash_out_act	        float	经营活动现金流出小计
        n_cashflow_act	        float	经营活动产生的现金流量净额
        oth_recp_ral_inv_act	float	收到其他与投资活动有关的现金
        c_disp_withdrwl_invest	float	收回投资收到的现金
        c_recp_return_invest	float	取得投资收益收到的现金
        n_recp_disp_fiolta	    float	处置固定资产、无形资产和其他长期资产收回的现金净额
        n_recp_disp_sobu	    float	处置子公司及其他营业单位收到的现金净额
        stot_inflows_inv_act	float	投资活动现金流入小计
        c_pay_acq_const_fiolta	float	购建固定资产、无形资产和其他长期资产支付的现金
        c_paid_invest	        float	投资支付的现金
        n_disp_subs_oth_biz	    float	取得子公司及其他营业单位支付的现金净额
        oth_pay_ral_inv_act	    float	支付其他与投资活动有关的现金
        n_incr_pledge_loan	    float	质押贷款净增加额
        stot_out_inv_act	    float	投资活动现金流出小计
        n_cashflow_inv_act	    float	投资活动产生的现金流量净额
        c_recp_borrow	        float	取得借款收到的现金
        proc_issue_bonds	    float	发行债券收到的现金
        oth_cash_recp_ral_fnc_act	float	收到其他与筹资活动有关的现金
        stot_cash_in_fnc_act	    float	筹资活动现金流入小计
        free_cashflow	            float	企业自由现金流量
        c_prepay_amt_borr	        float	偿还债务支付的现金
        c_pay_dist_dpcp_int_exp	    float	分配股利、利润或偿付利息支付的现金
        incl_dvd_profit_paid_sc_ms	float	其中:子公司支付给少数股东的股利、利润
        oth_cashpay_ral_fnc_act	float	支付其他与筹资活动有关的现金
        stot_cashout_fnc_act	float	筹资活动现金流出小计
        n_cash_flows_fnc_act	float	筹资活动产生的现金流量净额
        eff_fx_flu_cash	        float	汇率变动对现金的影响
        n_incr_cash_cash_equ	float	现金及现金等价物净增加额
        c_cash_equ_beg_period	float	期初现金及现金等价物余额
        c_cash_equ_end_period	float	期末现金及现金等价物余额
        c_recp_cap_contrib	    float	吸收投资收到的现金
        incl_cash_rec_saims	    float	其中:子公司吸收少数股东投资收到的现金
        uncon_invest_loss	    float	未确认投资损失
        prov_depr_assets	    float	加:资产减值准备
        depr_fa_coga_dpba	    float	固定资产折旧、油气资产折耗、生产性生物资产折旧
        amort_intang_assets	    float	无形资产摊销
        lt_amort_deferred_exp	float	长期待摊费用摊销
        decr_deferred_exp	    float	待摊费用减少
        incr_acc_exp	        float	预提费用增加
        loss_disp_fiolta	    float	处置固定、无形资产和其他长期资产的损失
        loss_scr_fa	            float	固定资产报废损失
        loss_fv_chg	            float	公允价值变动损失
        invest_loss	            float	投资损失
        decr_def_inc_tax_assets	float	递延所得税资产减少
        incr_def_inc_tax_liab	float	递延所得税负债增加
        decr_inventories	    float	存货的减少
        decr_oper_payable	    float	经营性应收项目的减少
        incr_oper_payable	    float	经营性应付项目的增加
        others	                float	其他
        im_net_cashflow_oper_act	float	经营活动产生的现金流量净额(间接法)
        conv_debt_into_cap	        float	债务转为资本
        conv_copbonds_due_within_1y	float	一年内到期的可转换公司债券
        fa_fnc_leases	            float	融资租入固定资产
        im_n_incr_cash_equ	        float	现金及现金等价物净增加额(间接法)
        net_dism_capital_add	float	拆出资金净增加额
        net_cash_rece_sec	    float	代理买卖证券收到的现金净额(元)
        credit_impa_loss	    float	信用减值损失
        use_right_asset_dep	    float	使用权资产折旧
        oth_loss_asset	        float	其他资产减值损失
        end_bal_cash	        float	现金的期末余额
        beg_bal_cash	        float	减:现金的期初余额
        end_bal_cash_equ	    float	加:现金等价物的期末余额
        beg_bal_cash_equ	    float	减:现金等价物的期初余额
        update_flag	            str	更新标志

        :return:
        """
        print("现金流量表: cashflow")

        # 使用示例
        start_date = pd.Timestamp(2023, 1, 1)
        end_date = pd.Timestamp(2023, 12, 31)
        last_days = self.get_last_day_of_quarters(start_date, end_date)

        all_df = pd.DataFrame()
        # 打印各个季度的最后一天
        for last_day in last_days:
            print(last_day, end=",")
            tmp_df = self.pro.cashflow_vip(period=last_day, fields="")
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)
            print("tmp_df.shape", tmp_df.shape)
            # break

        table_name = "cashflow"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_forecast(self):
        """
        业绩预告
        接口：forecast，可以通过数据工具调试和查看数据。
        描述：获取业绩预告数据

        字段	            类型	说明
        ts_code	        str	TS股票代码
        ann_date    	str	公告日期
        end_date    	str	报告期
        type	        str	业绩预告类型
        p_change_min	float	预告净利润变动幅度下限（%）
        p_change_max	float	预告净利润变动幅度上限（%）
        net_profit_min	float	预告净利润下限（万元）
        net_profit_max	float	预告净利润上限（万元）
        last_parent_net	float	上年同期归属母公司净利润
        notice_times	int	公布次数
        first_ann_date	str	首次公告日
        summary	        str	业绩预告摘要
        change_reason	str	业绩变动原因
        update_flag	    str	更新标志

        :return:
        """
        print("业绩预告: forecast")

        # 使用示例
        start_date = pd.Timestamp(2023, 1, 1)
        end_date = pd.Timestamp(2024, 12, 31)
        last_days = self.get_last_day_of_quarters(start_date, end_date)

        column_names = "ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min,net_profit_max,last_parent_net,notice_times,first_ann_date,summary,change_reason,update_flag"

        all_df = pd.DataFrame()
        # 打印各个季度的最后一天
        for last_day in last_days:
            print(last_day, end=",")
            tmp_df = self.pro.forecast_vip(period=last_day, fields=column_names)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)
            print("tmp_df.shape", tmp_df.shape)
            # break

        table_name = "forecast"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_express(self):
        """
        业绩快报
        接口：express
        描述：获取上市公司业绩快报

        字段	            类型	说明
        ts_code	        str	TS股票代码
        ann_date	    str	公告日期
        end_date	    str	报告期
        revenue	        float	营业收入(元)
        operate_profit	float	营业利润(元)
        total_profit	float	利润总额(元)
        n_income	    float	净利润(元)
        total_assets	float	总资产(元)
        total_hldr_eqy_exc_min_int	float	股东权益合计(不含少数股东权益)(元)
        diluted_eps	    float	每股收益(摊薄)(元)
        diluted_roe	    float	净资产收益率(摊薄)(%)
        yoy_net_profit	float	去年同期修正后净利润
        bps	            float	每股净资产
        yoy_sales	    float	同比增长率:营业收入
        yoy_op	        float	同比增长率:营业利润
        yoy_tp	        float	同比增长率:利润总额
        yoy_dedu_np	    float	同比增长率:归属母公司股东的净利润
        yoy_eps	        float	同比增长率:基本每股收益
        yoy_roe	        float	同比增减:加权平均净资产收益率
        growth_assets	float	比年初增长率:总资产
        yoy_equity	    float	比年初增长率:归属母公司的股东权益
        growth_bps	    float	比年初增长率:归属于母公司股东的每股净资产
        or_last_year	float	去年同期营业收入
        op_last_year	float	去年同期营业利润
        tp_last_year	float	去年同期利润总额
        np_last_year	float	去年同期净利润
        eps_last_year	float	去年同期每股收益
        open_net_assets	float	期初净资产
        open_bps	    float	期初每股净资产
        perf_summary	str	业绩简要说明
        is_audit	    int	是否审计： 1是 0否
        remark	        str	备注
        update_flag	    str	更新标志

        :return:
        """
        print("业绩快报: express")

        # 使用示例
        start_date = pd.Timestamp(2023, 1, 1)
        end_date = pd.Timestamp(2024, 12, 31)
        last_days = self.get_last_day_of_quarters(start_date, end_date)

        column_names = "ts_code,ann_date,end_date,revenue,operate_profit,total_profit,n_income,total_assets,total_hldr_eqy_exc_min_int,diluted_eps,diluted_roe,yoy_net_profit,bps,yoy_sales,yoy_op,yoy_tp,yoy_dedu_np,yoy_eps,yoy_roe,growth_assets,yoy_equity,growth_bps,or_last_year,op_last_year,tp_last_year,np_last_year,eps_last_year,open_net_assets,open_bps,perf_summary,is_audit,remark,update_flag"

        all_df = pd.DataFrame()
        # 打印各个季度的最后一天
        for last_day in last_days:
            print(last_day, end=",")
            tmp_df = self.pro.express_vip(period=last_day, fields=column_names)
            all_df = pd.concat([all_df, tmp_df], ignore_index=True)
            print("tmp_df.shape", tmp_df.shape)
            # break

        table_name = "express"
        res = self.mysql_write_data(all_df,
                                    name=table_name, if_exists="replace",
                                    index=True, index_label="id", chunksize=5000)
        print("res: ", res)

    def get_dividend(self):
        """
        接口：dividend
        描述：分红送股数据

        字段	            类型	说明
        ts_code	        str	TS代码
        end_date	    str	分送年度
        ann_date	    str	预案公告日（董事会）
        div_proc	    str	实施进度
        stk_div     	float	每股送转
        stk_bo_rate	    float	每股送股比例
        stk_co_rate	    float	每股转增比例
        cash_div	    float	每股分红（税后）
        cash_div_tax	float	每股分红（税前）
        record_date	    str	股权登记日
        ex_date	        str	除权除息日
        pay_date	    str	派息日
        div_listdate	str	红股上市日
        imp_ann_date	str	实施公告日
        base_date	    str	基准日
        base_share	    float	实施基准股本（万）
        update_flag	    str	是否变更过（1表示变更）

        :return:
        """
        print("分红送股数据: dividend")

        df = self.pro.stock_basic()
        ts_codes = df['ts_code'].values

        column_names = "ts_code,end_date,ann_date,div_proc,stk_div,stk_bo_rate,stk_co_rate,cash_div,cash_div_tax,record_date,ex_date,pay_date,div_listdate,imp_ann_date,base_date,base_share,update_flag"

        all_df = pd.DataFrame()
        try:
            for index, ts_code in enumerate(ts_codes):
                print(index, ts_code, end=",")
                tmp_df = self.pro.dividend(ts_code=ts_code, fields=column_names)
                all_df = pd.concat([all_df, tmp_df], ignore_index=True)
                print("tmp_df.shape", tmp_df.shape)
                # break
        except Exception as e:
            print(e)
        finally:
            table_name = "dividend"
            res = self.mysql_write_data(all_df,
                                        name=table_name, if_exists="replace",
                                        index=True, index_label="id", chunksize=5000)
            print("res: ", res)

    def get_dividend_append(self):
        print("分红送股数据: dividend")

        df = self.pro.stock_basic()
        ts_codes = df['ts_code'].values

        column_names = "ts_code,end_date,ann_date,div_proc,stk_div,stk_bo_rate,stk_co_rate,cash_div,cash_div_tax,record_date,ex_date,pay_date,div_listdate,imp_ann_date,base_date,base_share,update_flag"

        all_df = pd.DataFrame()
        try:
            for index, ts_code in enumerate(ts_codes):
                if index < 269:
                    continue
                print(index, ts_code, end=",")
                tmp_df = self.pro.dividend(ts_code=ts_code, fields=column_names)
                all_df = pd.concat([all_df, tmp_df], ignore_index=True)
                print("tmp_df.shape", tmp_df.shape)
                # break
        except Exception as e:
            print(e)
        finally:
            table_name = "dividend"
            res = self.mysql_write_data(all_df,
                                        name=table_name, if_exists="replace",
                                        index=True, index_label="id", chunksize=5000)
            print("res: ", res)

if __name__ == '__main__':
    print("finance data...")
    finance_data = FinanceData(db_name="tushare_finance")
    finance_data.get_income()
    # finance_data.get_balancesheet()
    # finance_data.get_cashflow()
    # finance_data.get_forecast()
    # finance_data.get_express()
    # finance_data.get_dividend()
    # finance_data.get_dividend_append()





