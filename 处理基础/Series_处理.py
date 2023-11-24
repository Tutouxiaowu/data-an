from pandas import Series as ser
# serise创建
s = ser([1,2,3,4],index=['one','two','there','four'])
print(s.index)
print(s.values)
# 转换数字类型
print(s.to_json)
# 获取数值
s.mean()
s.min()
s.max()
s.sum()
s.sort_values()
s.sort_index()
