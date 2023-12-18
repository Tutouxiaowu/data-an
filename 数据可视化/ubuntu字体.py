
import matplotlib.font_manager as fm

font_list = fm.findfont(fm.FontProperties(family='SimHei'))
print(font_list)
import matplotlib
print(matplotlib.matplotlib_fname())

import matplotlib.pyplot as plt

font_name = "simhei"
plt.rcParams['font.family']= font_name # 指定字体，实际上相当于修改 matplotlibrc 文件　只不过这样做是暂时的　下次失效
plt.rcParams['axes.unicode_minus']=False # 正确显示负号，防止变成方框


x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

plt.plot(x, y)
plt.title("示例图表")
plt.xlabel("X 轴")
plt.ylabel("Y 轴")

plt.show()
