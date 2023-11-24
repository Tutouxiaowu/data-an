# Numpy对数据的存取
import numpy as np
# 存入
a = np.arange(20)
np.save('array_1',a) # 这个文件的后缀为 npy
# 读取
b = np.load('array_1.npy')
# np.savez 压缩存储
np.savez('array_z',a,b)
# txt
np.savetxt('array.txt',a)
np.loadtxt('array.txt')
# csv文件
# 这里面中的 fmt 参数主要是用来设置具体数值的类型，而 delimiter 值得是你要以 xx 进行分割。
np.savetxt('array.csv',a,fmt='%d',delimiter=',')
b = np.loadtxt('array.csv',delimiter=',')
