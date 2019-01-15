'''
提供时间线轮播多张图
Timeline 类的使用：
1、引入 Timeline 类，from pyecharts import Timeline
2、实例化 Timeline 类
3、使用 add() 向 timeline 中添加图。如 add(bar, '2013') 接受两个参数，第一个为图实例，第二个为时间线的 ”时间点“。
4、使用 render() 渲染生成 .html 文件

'''
from pyecharts import Pie, Timeline
from random import randint
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
pie_1 = Pie("2012 年销量比例", "数据纯属虚构")
pie_1.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

pie_2 = Pie("2013 年销量比例", "数据纯属虚构")
pie_2.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

pie_3 = Pie("2014 年销量比例", "数据纯属虚构")
pie_3.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

pie_4 = Pie("2015 年销量比例", "数据纯属虚构")
pie_4.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

pie_5 = Pie("2016 年销量比例", "数据纯属虚构")
pie_5.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

timeline = Timeline(is_auto_play=True, timeline_bottom=0)
timeline.add(pie_1, '2012 年')
timeline.add(pie_2, '2013 年')
timeline.add(pie_3, '2014 年')
timeline.add(pie_4, '2015 年')
timeline.add(pie_5, '2016 年')
timeline.render()