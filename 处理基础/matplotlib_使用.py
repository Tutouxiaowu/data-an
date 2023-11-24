import  numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
a = np.random.rand(100)
s = pd.DataFrame(a)
print(s)
# 折线图
plt.plot(s)
plt.xlabel('lol')
plt.ylabel('fxxkpython')
# 直方图
plt.hist(s)
# 条形图
l1 = ['python','java','c']
l2 = [60,30,10]
plt.bar(l1,l2)
# 饼图
plt.pie(labels=l1,x=l2)
# 散点图
x = np.random.rand(300)
y = np.random.rand(300)
plt.scatter(x,y)
# 箱形图
a2 = np.random.randint(20,size=(10,4))
plt.boxplot(a2)
plt.show()