import numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
import matplotlib.pyplot as plt
'''
我们绘画的时候 需要有区域意识，首先是figure 画布的区域 我们可以创建多个画布 plt.figure(1) plt.figure(2)
'''

# 普通的子图绘制
fig = plt.figure()
fig.suptitle('Figure') # 创建一张画布 子图标题为Figure
plt.subplot(341) # 将画布分为3-4 的第一个位置（区域意识！！）
plt.subplot(3,4,(2,4)) # 在3-4中 左上角是第2个区域，右下角是第四个区域
# 这样我们就可以完成 自己随意的定义区域而不受限制

# 还有就是面对对象axes子类的绘制
fig2,axs = plt.subplots(2,2,figsize=(5,5)) # 绘制的2行2列
axs[0,0].hist() # 均等的第一个子图的绘制



# 自定义布局方式之add_gridspec()   GridSpec类
fig3 = plt.figure()  # 创建一个画布
gs = fig3.add_gridspec(3,3) # 利用GriSpec类创建对象，3行3列
f3_ax1 = fig3.add_subplot(gs[0,:]) # 第一个子图为第一行的全部
f3_ax2  = fig3.add_subplot(gs[1,:-1]) #  第二个为第二行的最后一列

'''
当然刻度线也可以修改

'''















''''
1.固定区域等分：
①.
fig,axs=plt.subplots(2,2)#创建2，2的子图
axs[0,0].plot(s) # 选定子图绘制
②.
axe1=plt.subplot(221) # 它的意思是2*2的子图中的第一个
axe4=plt.subplot(224)
axe1.set_title()
'''


# 修改Matplotlib配置文件
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

y = np.arange(12)
x1 = np.array([19, 33, 28, 29, 14, 24, 57, 6, 26, 15, 27, 39])
x2 = np.array([25, 33, 58, 39, 15, 64, 29, 23, 22, 11, 27, 50])
labels = np.array(['中国', '加拿大', '巴西', '澳大利亚', '日本', '墨西哥',
                       '俄罗斯', '韩国', '瑞士', '土耳其', '英国', '美国'])

fig,(axe1,axe2)=plt.subplots(1,2) #绘制两个子图
barh1_rects = axe1.barh(y,x1,height=0.5, tick_label=labels, color='#FFA500')
axe1.set_xlabel("人口比例%")
axe1.set_title("部分国家养猫人群的比例")
axe1.set_xlim(0,x1.max()+10)

for rect in barh1_rects:
        width = rect.get_width()
        axe1.text(width + 3, rect.get_y() , s='{}'.format(width),
                   ha='center', va='bottom')


barh2_rects = axe2.barh(y, x2, height=0.5, tick_label=labels, color='#20B2AA')
axe2.set_xlabel('人群比例（％）')  # axe子图方式设置标签set_
axe2.set_title('部分国家养狗人群的比例')
axe2.set_xlim(0, x2.max()+10)

for rect in barh1_rects:
        width = rect.get_width()
        axe2.text(width + 3, rect.get_y() , s='{}'.format(width),
                   ha='center', va='bottom')

plt.tight_layout()
plt.show()