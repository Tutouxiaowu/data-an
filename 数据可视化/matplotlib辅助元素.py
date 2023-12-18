# Axes对象使用set_xlabel()方法可以设置x轴的标签，使用set_ylabel()方法可以设置y轴的标签。set_xlabel()、set_ylabel()方法与xlabel()、ylabel()函数的参数用法相同。

'''
1.xlabel
2.xlim
3.title
4.legend (图例)
5.grid网格
6.xticks刻度
7.annotate注释指向性文本
8.text 无指向性文本(x,y,s,bbox)
9.table
10.plt.figure(figsize=(10,8)) 设置画布大小
'''


import math
import numpy as np
import matplotlib.pyplot as plt
# 首先最简单的 xlabel ylabel
import matplotlib as mpl

# mpl.rcParams["font.family"] = "FangSong"  # 设置字体
#
# mpl.rcParams["axes.unicode_minus"] = False  # 正常显示负号

x = np.linspace(0, 10, 100)# 这里的linspace与arange十分相像，而且它可以指定leixdtype
y1 =  3*np.sin(x)+2
y2 =  3*np.cos(x)+2
plt.plot(x,y1,c='r')
plt.plot(x,y2,c='r')

#1.
# plt.xlabel('xzhou')
# plt.ylabel('yzhou')
# xlim 轴的范围
# plt.ylim(-2,5)
# plt.xlim(1,2)
# plt.title('cos and sin')
# plt.show()


# 2.legend添加图例
# plt.legend(loc=1)
# plt.legend(loc='upper right')
# 两种用法
# axes 一般我不用，因为没有提示，其次，plot都可以完成

# fig,axes = plt.subplots()
# axes.plot(x,y1,label = 'sinx')
# axes.plot(x,y2,label = 'cosx')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# 在label设置后，开启图例
# axes.legend()
# plt.show()

#  3.plot
line = plt.plot(x,y1,x,y2)
plt.legend(line,['sin','cos'])

# 4.设置网格线
plt.grid(axis='y',linewidth=0.3) #axis 只显示y轴的
# 5.设置参考线
plt.axhline(y=0,xmin=0,xmax=1, linestyle='-') #水平
plt.axvline(x=0,ymin=0,ymax=1, linestyle='-') #垂直 另外参考区域，axvspan与axhspan

# 设置指向性注释文本
plt.annotate("the_min",(3,-1),xytext=(3,-0.5),arrowprops=dict(arrowstyle='->'))
# 设置无指向性注释文本
plt.text(4,4,"cos_sin",bbox=dict(alpha=0.2))
plt.show()
plt.close()



# ①再举个例子
zd = ['play','shop','sport','daily','love','eat']
money = [10,20,30,40,50,60]
# 设置颜色
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
# 突出显示某一部分，值越大，偏离中心的距离越大
explode = (0, 0, 0.1, 0, 0, 0)
# 创建饼状图
# explode参数被用来突出显示’sport’部分，colors参数用来设置每个部分的颜色，shadow=True添加了阴影，startangle=150参数设置了饼图开始的角度
plt.pie(money, explode=explode, labels=zd, colors=colors, autopct='%1.1f%%', shadow=True, startangle=150)
plt.title("Spending Categories")  # 添加标题
plt.axis('equal')  # 确保是一个完整的圆形
plt.legend()
plt.show()
plt.close()


# ②例子
# 设置参考线
class_name = ['g1','g2','g3','g4','g5','g6']
theboy_grade = [90.5,89.5,88.7,88.5,88.2,88.6]
thegirl_grade = [92.7,86.0,90.5,85.0,89.9,89.5]
the_avg = (sum(thegirl_grade)+sum(theboy_grade))/(len(thegirl_grade)+len(theboy_grade))
print(the_avg)
bar_width=0.4
index=  np.arange(len(class_name))
plt.bar(index,theboy_grade,bar_width,label = 'boy',)
plt.bar(index+bar_width,thegirl_grade,bar_width,label = 'girl')
plt.axhline(y=the_avg,linestyle= '-',label = 'the_cankao')
# loc设置位置
plt.legend(loc='upper right')
plt.ylabel("grade")
plt.xlabel('class')
# 设置刻度
plt.xticks(index+bar_width/2,class_name)
plt.show()
plt.close()

# ③例子
fy = ['fy2013','fy2014','fy2015','fy2016','fy2017','fy2018','fy2019',]
gmv = [10000,16000,21000,30000,36000,44000,53000]
plt.bar(fy,gmv,label = gmv)
plt.ylabel("gmv/")
start = 0
for g in gmv:
    plt.text(start-0.3,g,g)
    start+=1
plt.show()

# ④例子
pei_name = ['mfen','qmai','jmu','applej','egg','yiol','yan','suger']
weight = [250,150,4,250,50,30,4,20]
explode1 = [0,0,0,0.1,0,0,0,0]
plt.figure(figsize=(10,8))
plt.pie(weight,labels=pei_name,explode=explode1,shadow=True,startangle=150,autopct='%1.1f%%',pctdistance=0.85)
# 希望它在图的外面 bbox_to_anchor
plt.legend(loc='upper left',bbox_to_anchor=(1.05, 1))
# plt.axis('equal')
plt.title('Pie Chart', fontsize=20)
# 调整图的大小
plt.show()


# ⑤美化的甜甜圈
import matplotlib.pyplot as plt
pei_name = ['mfen','qmai','jmu','applejuice','egg','yiol','yan','suger']
weight = [250,150,4,250,50,30,4,20]
explode1 = [0,0,0,0.1,0,0,0,0]
colors = ['lightsteelblue', 'rosybrown', 'peru', 'gold', 'darkkhaki', 'lightgreen', 'turquoise', 'purple']  # 添加颜色
plt.figure(figsize=(10,8))  # 调整图的大小
plt.title('Pie Chart', fontsize=20)  # 添加标题和调整字体大小
plt.pie(weight, explode=explode1, labels=pei_name, colors=colors, autopct='%1.1f%%', shadow=True, startangle=150, pctdistance=0.85)

centre_circle = plt.Circle((0,0),0.70,fc='white')  # 创建一个白色的圆，目的：覆盖原图，将饼图变为环形图
fig = plt.gcf() # “get current figure” 的缩写。
fig.gca().add_artist(centre_circle) #fig.gca() 获取当前图形的当前子图。如果当前图形没有子图，那么它会创建一个子图。在这里，gca 是 “get current axes” 的缩写。

plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=12)  # 调整图例的位置和字体大小
celltext = np.array(pei_name+weight).reshape(2,8)
print(celltext)
plt.table(cellText=celltext,cellColours=None,cellLoc='right',rowLabels=['peiliao','weight'])
plt.show()
