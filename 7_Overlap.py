'''
结合不同类型图表叠加画在同张图上
Overlap 类的使用：
1、引入 Overlap 类，from pyecharts import Overlap
2、实例化 Overlap 类，overlap = Overlap() ，可指定 page_title, width, height, jhost 参数。
3、使用 add() 向 overlap 中添加图
4、使用 render() 渲染生成 .html 文件

Overlap.add() 方法签名
add(chart, 图表示例
    xaxis_index=0, x 坐标轴索引，默认为 0
    yaxis_index=0, y 坐标轴索引，默认为 0
    is_add_xaxis=False, 是否新增一个 x 坐标轴，默认为 False
    is_add_yaxis=False)  是否新增一个 y 坐标轴，默认为 False

'''
# Line + Bar
from pyecharts import Overlap,Line,Bar

attr=['A', 'B', 'C', 'D', 'E', 'F']
v1=[10, 20, 30, 40, 50, 60]
v2=[38, 28, 58, 48, 78, 68]
bar=Bar('Line-Bar示例')
bar.add('bar',attr,v1)

line=Line()
line.add('line',attr,v2)

overlap=Overlap()
overlap.add(line)
overlap.add(bar)
overlap.render()