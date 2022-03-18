# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 22:34:13 2022

@author: 最后一盏
"""
import pandas as pd
import numpy as np
from shutil import copyfile
import os,sys
file_name = '../附件2/图片虫子位置详情表.csv'
df = pd.read_csv(file_name, names=range(9), header=None, encoding='ANSI')
df = df.loc[1:, 1:]
df.columns = ['序号', '文件名', '虫子编号', '虫子名', 'x', 'y', '左上', '右下']  # 添加列名
pd.set_option('display.max_rows', 10)  # 打印行数
np.set_printoptions(threshold=1e6)  # 设置输出
querySer = df.loc[:, '虫子编号'] != '0'
df = df.loc[querySer, :]
ls = []
for index, row in df.iterrows():
    str = row["文件名"]
    if str not in ls:
        ls.append(str)
for i in ls:
    path1 = "./"+i #需要复制的文件所在地址
    path2 = "../有标记的图片/"+i #目标地址
    copyfile(path1, path2)
    os.remove(path1)
