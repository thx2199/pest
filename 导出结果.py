# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:04:15 2022

@author: 最后一盏
"""
#%% 导出结果——问题二三的结果样例
import pandas as pd
import numpy as np
import os,codecs
from csv import reader,writer

pt = {0: 6, 1: 7, 2: 8, 3: 9, 4: 10, 5: 25, 6: 41, 7: 105, 8: 110, 9: 115, 10: 148,
      11: 156, 12: 222, 13: 228, 14: 235, 15: 256, 16: 280, 17: 310, 18: 387, 19: 392,
      20: 394, 21: 398, 22: 401, 23: 402, 24: 430, 25: 480, 26: 485, 27: 673}

path = "./labels" #文件所在地址
file_list = os.listdir(path)
f1 = codecs.open('./problem_2.csv','w','gbk')
w1 = writer(f1)
w1.writerow(['序号','文件名','虫子编号','中心点x坐标','中心点y坐标','左上角x坐标','左上角y坐标','右下角x坐标','右下角y坐标'])
f2 = codecs.open('./problem_3.csv','w','gbk')
w2 = writer(f2)
w2.writerow(['序号','文件名','虫子编号','数量'])
num = {}
for fn in file_list:
        name=fn[0:-4]+'.jpg'
        f = open('./labels/'+fn,encoding='UTF-8')
        while True:
            line = f.readline()
            if line:
                ID,x,y,w,h = line.split()
                x,y,w,h = round(float(x)*5472),round(float(y)*3648),round((float(w)/2)*5472),round((float(h)/2)*3648)
                zs_x,zs_y = x-w,y-h
                yx_x,yx_y = x+w,y+h
                bh = pt[int(ID)]
                w1 = writer(f1)
                w1.writerow(['',name,bh,x,y,zs_x,zs_y,yx_x,yx_y])
                if bh in num:
                    num[bh] = num[bh] + 1
                else:
                    num[bh] = 1
                
            else:
                for k in num:
                    w2 = writer(f2)
                    w2.writerow(['',name,k,num[k]])
                break
        f.close()
f1.close()        
f2.close()




#%% 导出结果——问题三的结果样例










