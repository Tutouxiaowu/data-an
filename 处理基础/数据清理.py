import pandas as pd
import numpy as np
# 缺失值检测
na_df = pd.DataFrame({'A':[1, 2, np.NaN, 4],
                          'B':[3, 4, 4, 5],
                          'C':[5, 6, 7, 8],
                          'D':[7, 5, np.NaN, np.NaN]})
print(na_df)
# 利用isnull，isna（notnull）可检测是否存在缺失值
print(na_df.isna().sum())# 统计
print(na_df.isnull().any())# 存在确实值,返回true
# 缺失值处理
# 删除缺失行
new_df = na_df.dropna()# thresh=3 存在3非NaN值
print(new_df)
# 计算A列平均值
col_a = np.around(np.mean(na_df['A']),1)# around(float,1) 保留1位小数字
col_d = np.around(np.mean(na_df['D']),1)
na_df = na_df.fillna({'A':col_a,'D':col_d})
print(na_df)
na_df.fillna(method='ffill')# 用front前面的数字来填充
na_df.interpolate(method='linear')# 林耳朵是用前后平均值来填充
# 重复值的检测
person_info = pd.DataFrame({'name': ['刘婷婷', '王淼', '彭岩', '刘华', '刘华', '周华'],
                'age': [24, 23, 29, 22, 22, 27],
                'height': [162, 165, 175, 175, 175, 178],
                'gender': ['女', '女', '男', '男', '男', '男']})
print(person_info.duplicated())
print(person_info.drop_duplicates()) # 删除重复值并对其索引重新排序
# 异常值检测
def three_sigma(ser):
    # 计算平均值
    mean_data = ser.mean()
    # 计算标准差
    std_data = ser.std()
    # 小于μ-3σ或大于μ+3σ的数值均为异常值 #生成一个布尔索引rule
    rule = (mean_data - 3 * std_data > ser) | (mean_data + 3 * std_data < ser)
    # 返回异常值的行索引
    index = np.arange(ser.shape[0])[rule]# 获取满足rule得下标
    # 获取异常值
    outliers = ser.iloc[index]
    return outliers
excel_data = pd.read_excel('data.xlsx')
result = three_sigma(excel_data['value'])
print(result)
from matplotlib import pyplot as plt
###### 绘制箱型图
plt.rcParams['font.sans-serif'] = ['SimHei']
excel_data.boxplot(column='value')
plt.show()
#### 正态分布检测
import scipy.stats as stats
data = pd.read_excel('data.xlsx')
u = data['value'].mean() # 均值
std = data['value'].std() # 标准差
print(stats.kstest(data['value'],'norm',(u,std)))# 检测是否符合正太分布
excel_data.drop([121,710]) # 删除异常项目 121 710
clean_data = excel_data.drop([121,710])
print(three_sigma(clean_data['value']))
replace_data = excel_data.replace({13.2:10.2,13.1:10.5})
print(excel_data.info()) # 可查看信息info
