# -*- coding:utf-8 -*-
# 利用Pychart库进行绘图
import numpy as np

from pyecharts import Bar
bar = Bar("我的第一个图表","第一个柱状图")
bar.add("服装", ["衬衫","羊毛衫","雪纺衫", "裤子", "高跟鞋", "袜子"],[5, 20, 36, 10, 75, 90],is_more_utils=True)
bar.show_config()
bar.render("F:/Python-study-diary/pyechartsss/my_first_chart.html")

# 绘制动态散点图
from pyecharts import EffectScatter
x = np.random.randn(100)
y = np.random.randn(100)

es = EffectScatter("","动态散点图",title_pos='center',width=800,height=600)
es.add("",x,y,symbol_size=10)
es.render("F:/Python-study-diary/pyechartsss/my_second_chart.html")






