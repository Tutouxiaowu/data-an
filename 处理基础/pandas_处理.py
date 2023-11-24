#   1. 使用DataFrame创建如上图所示的数据。
#   2. 对创建的数据以列索引D为准进行按值排序。
# 计算排序后行号索引为1数据的平均值。

import pandas as pd
data = pd.DataFrame({'A':[38,48,29,40],'B':[23.5,63,58,77],'C':[40.2,44,2,31],'D':[23,44,25,56]})
print(data)
# 通过复制的内容创建
df = pd.read_clipboard()

# 获取数值
# 通过iloc 对索引进行取值
print(data.iloc[0])
print(data.values)
print(data.columns)
print(data.index)
print(data.columns.str.upper()) # 大小写
print(data.columns.str.lower())
# 获取一次性数据
data.describe()

# 保存到csv
# data.to_csv('')

# 去重
data.drop_duplicates('A')
# 去掉不必要的列
data.drop(colums=['A','B'])
# 去掉不必要的行
data.drop(index=[0,1])
# 巧用apply
data['A'] = data['A'].apply(lambda x:x+1)
import numpy as np
import pandas as pd
# 数据分类
df1 = pd.DataFrame()
# df1['product'] = [pd.util.testing.rands(6) for i in range(15)]
df1['price'] = [np.random.randint(1000) for i in range(15)]
print(df1)
bins = [0,200,400,600,800,1000]
# cut 方法对df1 按照bins分组
res  = pd.cut(df1['price'],bins)
print(res)
print(res.value_counts())
print(res.describe())