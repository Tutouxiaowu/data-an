
# seaborn 库是在 matplotlib 的基础上建立的 Python 数据可视化库，用法差不多，不过它提供了一些更高级一些的界面

import seaborn as sns
import numpy as np
import pandas as pd
x = np.random.rand(100)
y = np.random.rand(100)
df = pd.DataFrame({'x':x,'y':y})
# 散点图
sns.relplot(data=df,kind='scatter')
# 折线图
sns.relplot(x=x,data=df,kind='line')
# 箱型图
sns.catplot(data=df,kind='box')
# 条形图
sns.catplot(data=df,kind='bar')
# 点线图
sns.catplot(data=df,kind="point")
# 直方图
a = np.random.rand(666)
s = pd.Series(a)
sns.displot(s,kde = False)# 是否显示线条

