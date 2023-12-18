import  numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
a = np.random.rand(100)
s = pd.DataFrame(a)
# # print(s)
# # 折线图
# plt.plot(a)
# plt.xlabel('lol')
# plt.ylabel('fxxkpython')
# plt.title('折线图')

# 直方图
# bin,range()限定范围
# plt.hist(s,20)
# plt.show()

# 柱形图
l1 = ['python','java','c']
l2 = [60,30,10]
plt.bar(x=l1,height=l2,color='yellow')
'''
    x：用于指定柱状图的x轴坐标，通常是一个数组或序列。
    height：用于指定柱状图的高度，通常是一个数组或序列。
    width：用于指定柱状图的宽度，默认值为0.8。
    color：用于指定柱状图的颜色，可以是一个字符串（表示颜色名称）或一个RGB元组。
    align：用于指定柱状图的对齐方式，可以是’center’（默认值）、‘edge’或’align’。
    edgecolor：用于指定柱状图的边框颜色，默认值为None。
    linewidth：用于指定柱状图的边框宽度，默认值为None。
    tick_label：用于指定柱状图的刻度标签，通常是一个字符串数组或序列。
'''
plt.show()

# 饼图
plt.pie(labels=l1,x=l2)

# 散点图
# 属性——x,y,s(数据点的大小),c(散点的颜色),marker='o'(散点样式), alpha=0.5（透明度）
x = np.random.rand(300)
y = np.random.rand(300)
plt.scatter(x,y)

# 箱形图
a2 = np.random.randint(20,size=(10,4))
plt.boxplot(a2)

# 有关子图
fig,axs=plt.subplots(2,2)#创建2，2的子图
axs[0,0].plot(s) # 选定子图绘制

# 要在所有子图中绘制相同的图形，请使用循环。以下代码将在所有子图中绘制一条线：
for ax in axs.flat:
    ax.plot(a)
# 有关图的辅助元素请看另一个 matplotlib辅助元素