import numpy as np
import matplotlib.pyplot as plt

# 例子①cos&sin的绘制
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x_data = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_one = np.sin(x_data)
y_two = np.cos(x_data)
fig = plt.figure()
'''
绘制任意位置坐标轴
'''
# 以原坐标轴为例 0.2，0.2 位置绘制一个0.7，0.7大小的坐标轴
ax = fig.add_axes((0.2, 0.2, 0.7, 0.7))
ax.plot(x_data, y_one, label='正弦曲线')
ax.plot(x_data, y_two, label='余弦曲线')
ax.legend()
ax.set_xlim(-2 * np.pi, 2 * np.pi)
ax.set_xticks([-2 * np.pi, -3 * np.pi / 2, -1 * np.pi, -1 * np.pi /
                    2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax.set_xticklabels(['$-2\pi$', '$-3\pi/2$', '$-\pi$', '$-\pi/2$',
                          '$0$', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
ax.set_yticklabels([-1.0, -0.5, 0.0, 0.5, 1.0])

'''
轴脊 的隐藏和移动
-----spines---  top bottom left right
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',0)) 
'''
# 隐藏右轴脊和上轴脊
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 移动左轴脊和下轴脊的位置
ax.spines['left'].set_position(('data', 0))# data为0的位置
ax.spines['bottom'].set_position(('data', 0))
plt.show()

'''
刻度样式
tick_params(axis='both',**kwargs)
axis：表示选择操作的轴，可以取值为'x'、'y'或'both'，默认为'both'。
reset：若设为True，表示在处理其他参数之前均使用参数的默认值。
which：表示选择刻度的类型，可以取值为'major'、'minor'或'both'，默认为'major'。
direction：表示刻度线的方向，可以取值为'in'、'out'或'inout'。
length：表示刻度线的长度。
width：表示刻度线的宽度。
color：表示刻度线的颜色
pad：表示刻度线与刻度标签的距离。
labelsize：表示刻度标签的字体大小。
labelcolor：表示刻度标签的颜色。
bottom，top，left，right：表示是否显示下方、上方、左方、右方的刻度线。
labelbottom ，labeltop ，labelleft,，labelright：表示是否显示下方、上方、左方、右方的刻度标签。
labelrotation：表示刻度标签旋转的角度
'''