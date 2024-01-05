'''
为了学习可视化，首先我们学习了numpy和pandas两个基本库

numpy其实就是专门来处理另一种数据结构的，数组
1.创建：list,arange,zeros,ones,random
2.当然作为多维的，可以获取其size，shape
3.两数组结合np.concatenate(arr6,arr4)
4.相比于列表更加便捷的操作arr.T,arr.unique,reshape,sum,max,min,mean
5.数据流：
np.savetxt('array.csv',a,fmt='%d',delimiter=',')
b = np.loadtxt('array.csv',delimiter=',') # 这里的后缀可以改

pandas:其中有两个数据结构Series 和 DataFrame
Series:(序列)一般来说就是一维带有序号
# serise创建
s = ser([1,2,3,4],index=['one','two','there','four'])

DataFrame要复杂点，当然也是最牛逼的
1.创建有index,columns,dtype,并且也可以按照字典的形式创建
2.DataFrame 最nb的一点就是有df.describe()可以查询其count,mean,std,min,占比，max
3.print(data.iloc[0])通过行索引，[]列索引
4.既然是nb的数据结构当然有一些nb方法

# 去重
data.drop_duplicates('A')
# 去掉不必要的列
data.drop(colums=['A','B'])
# 去掉不必要的行
data.drop(index=[0,1])
# 巧用apply
data['A'] = data['A'].apply(lambda x:x+1)
# 数据分类cut
5.数据流
csv_content = pd.read_csv() # csv text
xl_content = pd.read_excel() # xlsx
json_content = pd.read_json() # json
df1.to_csv() # 一行代码存入文件，就很牛逼


当然学会了这两种数据结构，还要掌握一些数据处理的方法
比如null的检测 和异常值的处理

好的，在可视化上一般可采用，matplotpy,seabron,pyechart
一般绘制的图形有:
1.折线图
plt.plot()
2.饼图
plt.pie()
3.箱型图
plt.boxplot()
4.直方图
plt.hist()
5.柱形图
plt.bar()
6.散点图
plt.scatter(x,y)
常用辅助元素：
1.xlabel,ylabel
2.xlim,ylim 刻度范围
3.title
4.legend() 图例
5.grid网格
6.xticks刻度
7.annotate注释指向性文本
8.text 无指向性文本(x,y,s,bbox)
9.table
10.plt.figure(figsize=(10,8)) 设置画布大小

当我想在画布上绘制多个子图如何操作呢
① 普通的子图绘制
fig = plt.figure()
fig.suptitle('Figure') # 创建一张画布 子图标题为Figure
plt.subplot(341) # 将画布分为3-4 的第一个位置（区域意识！！）
plt.subplot(3,4,(2,4)) # 在3-4中 左上角是第2个区域，右下角是第四个区域
# 这样我们就可以完成 自己随意的定义区域而不受限制

②此外创建子图对象
fig2,axs = plt.subplots(2,2,figsize=(5,5)) # 绘制的2行2列
axs[0,0].hist() # 均等的第一个子图的绘制
# 自定义布局方式之add_gridspec()   GridSpec类
fig3 = plt.figure()  # 创建一个画布
gs = fig3.add_gridspec(3,3) # 利用GriSpec类创建对象，3行3列
f3_ax1 = fig3.add_subplot(gs[0,:]) # 第一个子图为第一行的全部
f3_ax2  = fig3.add_subplot(gs[1,:-1]) #  第二个为第二行的最后一列

这个时候很多图表基本上我们都能绘制了
为了更加个性化的定制可以进行以下：
1.坐标轴的定制
'''
import numpy as np
list1 = [1,2,3,4,5]
# 有关创建
arr1 = np.array(list1) # 列表转数组
arr2 = np.arange(1,10,2) # arange 创建
arr3 = np.zeros((2,3))
arr4 = np.ones((2,3))
arr5 = np.random.rand(2,3) # random 函数中rand 和 random差不多，只是random只能传一个参数，通常是元组
arr6 = np.random.randint(1,10,size=(2,3))

# print(arr6.describe())
# 获取属性
# arr6.shape
# arr5.size
# np.concatenate(arr6,arr4)
# 数据流
# a = np.arange(20)
# np.save('array_1',a) # 这个文件的后缀为 npy
# # csv文件
# # 这里面中的 fmt 参数主要是用来设置具体数值的类型，而 delimiter 值得是你要以 xx 进行分割。
# np.savetxt('array.csv',a,fmt='%d',delimiter=',')
# b = np.loadtxt('array.csv',delimiter=',') # 这里的后缀可以改

import pandas as pd
arr = np.random.randint(1,10,size=(2,3))
# 采用index colums自己设计的方式创建
df = pd.DataFrame(1,('2','2','2'),columns=('a','b','c'))
# 采用字典的形式创建
data = pd.DataFrame({'A':[38,48,29,40],'B':[23.5,63,58,77],'C':[40.2,44,2,31],'D':[23,44,25,56]})
print(data)
print(data.iloc[1]) # 按行进行访问（索引）
print(data['A'])


df1 = pd.DataFrame() # 先创建一个空的
# df1['product'] = [pd.util.testing.rands(6) for i in range(15)]
df1['price'] = [np.random.randint(1000) for i in range(15)] # 进行数据添加
print(df1)
bins = [0,200,400,600,800,1000] # bins
# cut 方法对df1 按照bins分组
res  = pd.cut(df1['price'],bins) # cut分组
print(res)
print(res.value_counts())
print(res.describe())
df1.to_csv()

# 缺失值的处理
# 缺失值检测
na_df = pd.DataFrame({'A':[1, 2, np.NaN, 4],
                          'B':[3, 4, 4, 5],
                          'C':[5, 6, 7, 8],
                          'D':[7, 5, np.NaN, np.NaN]})
print(na_df)
# 利用isnull，isna（notnull）可检测是否存在缺失值
print(na_df.isna().sum())# 统计
print(na_df.isnull().any())# 存在缺失值,返回true
# 当然箱型图也可以
from matplotlib import pyplot as plt

plt.boxplot(na_df)
plt.show()

# 处理缺失值
# 1.如果数据多，可以选择删除
new_df = na_df.dropna()
print(new_df)
# 2.计算A列,平均值填充
col_a = np.around(np.mean(na_df['A']),1)
col_b = np.around(np.mean(na_df['D']),1)
na_df = na_df.fillna({'A':col_a,'D':col_b})
print(na_df)
# na_df.fillna(method='obj.bfill()')# 用front前面的数字来填充
na_df.interpolate(method='linear')# 林耳朵是用前后平均值来填充
# 重复值的检测
# na_df.duplicated()