#   1. 使用DataFrame创建如上图所示的数据。
#   2. 对创建的数据以列索引D为准进行按值排序。
# 计算排序后行号索引为1数据的平均值。
import pandas as pd
data = pd.DataFrame({'A':[38,48,29,40],'B':[23.5,63,58,77],'C':[40.2,44,2,31],'D':[23,44,25,56]})
print(data)
data = data.sort_values(by='B') # sort_index 为按照索引排列
print(data)
mean1 = data.iloc[1].mean() # 访问列索引 data['A'] 访问索引(行)iloc
print(mean1)