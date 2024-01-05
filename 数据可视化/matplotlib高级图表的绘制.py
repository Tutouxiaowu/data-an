import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
# 绘制棉棒图
# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['axes.unicode_minus'] = False
# labels = ['武磊登上电影频道','东京奥运会海报','浓眉哥受伤','安东尼准绝杀','湖人单场20记盖帽','第77届金球奖红毯','孟非大赞武磊','李铁上任','活塞vs湖人','英超']
# x_data = np.arange(1, 11)
# y_data = [62253,51255,34541,28733,17073,9000,5963,2041,1879,1681]
# data = {'体育热点': ['武磊登上电影频道','东京奥运会海报','浓眉哥受伤','安东尼准绝杀','湖人单场20记盖帽','第77届金球奖红毯','孟非大赞武磊','李铁上任','活塞vs湖人','英超'],
#         '搜索指数': [62253,51255,34541,28733,17073,9000,5963,2041,1879,1681]}
# df = pd.DataFrame(data)
# fig = plt.figure(figsize=(20,10), dpi= 50)
# plt.stem(labels,y_data)
# plt.ylabel("搜索指数")
# plt.xlabel("体育热点")
# for i, v in enumerate(df['搜索指数']):
#     plt.text(i, v + 1000, str(v), ha='center')
# plt.show()
# 桑基图
import pandas as pd
from matplotlib.sankey import Sankey
import matplotlib.pyplot as plt

data = {'收支明细': ['购物', '餐饮', '交通', '工资', '奖金'], '金额（元）': [-200, -100, -50, 500, 200]}
df = pd.DataFrame(data)

# 将数据分为支出和收入两部分
expenditure = df[df['金额（元）'] < 0]
income = df[df['金额（元）'] > 0]

# 计算支出和收入的总和
total_expenditure = -sum(expenditure['金额（元）'])
total_income = sum(income['金额（元）'])

# 如果支出和收入总和不相等，则在支出或收入中添加一个调整项
if total_expenditure != total_income:
    if total_expenditure > total_income:
        income = pd.concat([income, pd.DataFrame({'收支明细': ['调整项'], '金额（元）': [total_expenditure - total_income]})], ignore_index=True)
    else:
        expenditure = pd.concat([expenditure, pd.DataFrame({'收支明细': ['调整项'], '金额（元）': [total_income - total_expenditure]})], ignore_index=True)

# 创建桑基图对象
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, aspect='auto')

# 绘制桑基图
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180)
sankey.add(flows=[total_expenditure, total_income],
           labels=['支出', '收入'],
           orientations=[-1, 1],
           pathlengths=[0.5, 0.5],
           trunklength=1.5,
           color='gray')

sankey.add(flows=expenditure['金额（元）'].values,
           labels=expenditure['收支明细'].values,
           orientations=[-1] * len(expenditure),
           pathlengths=[0.3] * len(expenditure),
           trunklength=1,
           prior=0,
           connect=(1, 0),
           alpha=0.5)

sankey.add(flows=income['金额（元）'].values,
           labels=income['收支明细'].values,
           orientations=[1] * len(income),
           pathlengths=[0.3] * len(income),
           trunklength=1,
           prior=0,
           connect=(0, 1),
           alpha=0.5)

# 添加注释文本
for i, expenditure_label in enumerate(expenditure['收支明细']):
    ax.text(0, i, expenditure_label, ha='right', va='center', fontsize=10, fontweight='bold')

for i, income_label in enumerate(income['收支明细']):
    ax.text(1, i, income_label, ha='left', va='center', fontsize=10, fontweight='bold')

# 设置标题和标签
ax.set_title('小兰当月日常生活收支流量桑基图')
ax.set_xticks([])
ax.set_yticks([])

plt.show()
