import pandas as pd
import numpy as np

pt = {6: 0, 7: 1, 8: 2, 9: 3, 10: 4, 25: 5, 41: 6, 105: 7, 110: 8, 115: 9,
      148: 10, 156: 11, 222: 12, 228: 13, 235: 14, 256: 15, 280: 16, 310: 17,
      387: 18, 392: 19, 394: 20, 398: 21, 401: 22, 402: 23, 430: 24, 480: 25, 485: 26, 673: 27}

file_name = '图片虫子位置详情表.csv'
df = pd.read_csv(file_name, names=range(9), header=None, encoding='ANSI')
df = df.loc[1:, 1:]
df.columns = ['序号', '文件名', '虫子编号', '虫子名', 'x', 'y', '左上', '右下']  # 添加列名
pd.set_option('display.max_rows', 10)  # 打印行数
np.set_printoptions(threshold=1e6)  # 设置输出
# print(df.dtypes)#查看数据类型
querySer = df.loc[:, '虫子编号'] != '0'
# 应用查询条件
print('处理前：', df.shape)
df = df.loc[querySer, :]
print('处理后：', df.shape)
print(df)
# 筛掉无虫数据结果临时文件
# df.to_csv('ans.csv')
for index, row in df.iterrows():
    print(row["文件名"], row["虫子名"])
    name = row["文件名"][0:-4] + ".txt"
    # 根据左上右下坐标计算宽和高

    x1, y1 = str(row['左上']).split(',')
    x2, y2 = str(row['右下']).split(',')
    # 创建追加txt文件
    with open('./data_pest/labels/' + name, 'a') as fp:
        a = float(row['x']) / 5472
        b = float(row['y']) / 3648
        c = (float(x2) - float(x1)) / 5472
        d = (float(y2) - float(y1)) / 3648
        fp.write(str(pt[int(row['虫子编号'])]))
        fp.write(" ")
        fp.write(str(a))
        fp.write(" ")
        fp.write(str(b))
        fp.write(" ")
        fp.write(str(c))  # 宽
        fp.write(" ")
        fp.write(str(d))  # 高
        fp.write("\n")