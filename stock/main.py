'''
Author: spc
Email: hilqiqi0@foxmail.com
Date: 2024-02-24 11:24:06
LastEditors: spc
LastEditTime: 2024-02-24 13:49:52
FilePath: /stock/stock/main.py
Description: 

Copyright (c) 2024 by spc, All Rights Reserved. 
'''


import os, sys
sys.path.append(os.getcwd())

from util.tools import get_tushare_pro


if __name__ == '__main__':
    print("start stock...")
    
    pro = get_tushare_pro()

    df = pro.stock_basic()
    
    print(df)
    