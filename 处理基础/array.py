# 1.创建一个数组，该数组的形状为(5,1)，元素值均为0。
# 2.创建一个代表国际象棋棋盘的8*8数组，其中棋盘的白格用0填充，棋盘黑格用1填充。

import numpy as  np
import pandas as pd

# 1.
arr = np.zeros(shape=(5,1),dtype=int)
print(arr)
# 2.
ch_arr = np.array([0,1]*32).reshape(8,8)
print(ch_arr)