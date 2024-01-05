import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
font_name = "simhei"
plt.rcParams['font.family']= font_name # 指定字体，实际上相当于修改 matplotlibrc 文件　只不过这样做是暂时的　下次失效
plt.rcParams['axes.unicode_minus']=False # 正确显示负号，防止变成方框
# x_moon = ['January','February','March','April','May','June','July','August','September','October','November','December']
# y_2018 = [39,20,40,38,42,43,41,41,45,48,52,50]
# y_2019 = [45,28,48,49,50,51,50,50,51,52,70,65]
# plt.figure(figsize=(16,8))
# plt.plot(x_moon,y_2018,color='#8B0000',linestyle = '--',marker='^',linewidth=1.5)
#
# plt.plot(x_moon,y_2019,color='#006374',linestyle = '-',marker='D',linewidth=1.5)
# plt.style.use('fivethirtyeight')
# plt.xlabel("月份")
# plt.ylabel("业务量(亿件)")
# plt.show()
# x = np.linspace(-1*np.pi,1*np.pi,100) # 临空间
# y1 = np.cos(x)
# y2 = np.sin(x)
# plt.plot(x,y2,color='r',linewidth=1.0,label = "sin")
# plt.plot(x,y1,color='b',linewidth=1.0,alpha = 0.5,label ="cos")
# # 注释文本
# plt.annotate("the_point",(1,np.cos(1)),xytext=(-2,1),arrowprops=dict(arrowstyle='->'))
# # 填充颜色
# plt.fill_between(x,y1, where=(np.abs(x) < 0.5) | (y1 > 0.5), color='green', alpha=0.25)
#
# # 刻度线
# x_ticks=['-pi','-pi/2','0','pi/2','pi']
# plt.xticks([-1*np.pi, -1/2*np.pi, 0, 1/2*np.pi, 1*np.pi],x_ticks)
# plt.yticks([-1, 0, 1], ['-1', '0', '1'])
#
# plt.title("cos&sin")
# plt.grid()
# plt.legend()
# plt.show()


#
# x = np.linspace(-2*np.pi, 2*np.pi, 100)
#
# # 计算正弦函数和余弦函数的值
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# # 设置sharex 共享x轴 同样的sharey 共享y轴
# fig,axs= plt.subplots(2,3,figsize=(12,8),sharex=True)
# axs[1,0].plot(x,y_sin)
# axs[0, 2].plot(x, y_cos)
# # 整体设置
# fig.suptitle("Trigonometric Functions")
# fig.text(0.5, 0.04, "x", ha="center")
# fig.text(0.04, 0.5, "y", va="center", rotation="vertical")
# # 调整子图之间的间距
# plt.subplots_adjust(hspace=0.3)
# plt.show()

# fig3 = plt.figure()  # 创建一个画布
# gs = fig3.add_gridspec(3,4) # 利用GriSpec类创建对象，3行3列
# f3_ax1 = fig3.add_subplot(gs[0,:]) # 第一个子图为第一行的全部
# f3_ax2  = fig3.add_subplot(gs[1,0:1])
# f3_ax3  = fig3.add_subplot(gs[1,2:3])
# f3_ax4  = fig3.add_subplot(gs[2,0:0])
# f3_ax5  = fig3.add_subplot(gs[2,1:3])
# plt.show()
# fig3 = plt.figure(figsize=(12,8))  # 创建一个画布
# gs = fig3.add_gridspec(3, 4)  # 利用GridSpec类创建对象，3行4列
# f3_ax1 = fig3.add_subplot(gs[0, :])  # 第一个子图为第一行的全部
# f3_ax2 = fig3.add_subplot(gs[1, 0:2])  # 修改索引范围
# f3_ax3 = fig3.add_subplot(gs[1, 2:4])  # 修改索引范围
# f3_ax4 = fig3.add_subplot(gs[2, 0:1])  # 修改索引范围
# f3_ax5 = fig3.add_subplot(gs[2, 1:4])  # 修改索引范围
# plt.show()
# 以原坐标轴为例 0.2，0.2 位置绘制一个0.7，0.7大小的坐标轴
