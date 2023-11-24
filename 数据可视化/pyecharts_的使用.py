'''
pyecharts
'''
# 如果我想绘制一个简单的直方图：
from pyecharts.charts import Bar
x_axis = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y_axis = [85, 120, 136, 103, 75, 90]
(
    Bar() # 初始化
    .add_xaxis(xaxis_data=x_axis)
    .add_yaxis(series_name="商家A",y_axis=y_axis) # 这里的serise_name用于tooltip,进行筛选
    .render_notebook()
     .set_global_opts(title_opts=TileOpts(title='bar'))
)


'''
Ok 但是其实 还是有很多我想要的信息没有表达出来（实际应用的时候，参考文档）
比如如果我要加入这个图的标题
我们可进行全局配置（图）
.set_global_opts(title_opts=TileOpts(title='bar'))
此外set_global_opts还有许多可用参数

'''