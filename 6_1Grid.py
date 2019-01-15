'''
Grid 类的使用：
1、引入 Grid 类，from pyecharts import Grid
2、实例化 Grid 类，grid = Grid() ，可指定 page_title, width, height, jhost 参数。
3、使用 add() 向 grid 中添加图，至少需要设置一个 grid_top, grid_bottom, grid_left, grid_right 四个参数中的一个。
                                                             grid_width 和 grid_height 一般不用设置，默认即可。
4、使用 render() 渲染生成 .html 文件

Grid.add() 方法签名
add(chart, 图表实例
    grid_width=None, grid 组件的宽度。默认自适应。
    grid_height=None, grid 组件的高度。默认自适应。
    grid_top=None, grid 组件离容器顶部的距离。默认为 None, 有'top', 'center', 'middle'可选，也可以为百分数或者整数
    grid_bottom=None, grid 组件离容器底部的距离
    grid_left=None, grid 组件离容器左侧的距离
    grid_right=None) grid 组件离容器右侧的距离
'''
# 上下类型，Bar + Line
from pyecharts import Grid,Bar,Line

attr_1=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1=[5, 20, 36, 10, 75, 90]
v2=[10, 25, 8, 60, 20, 80]
bar=Bar('柱状图示例',height=720)
bar.add('商家A',attr_1,v1,is_stack=True)
bar.add('商家B',attr_1,v2,is_stack=True)

attr_2=["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
v3=[11, 11, 15, 13, 12, 13, 10]
v4=[1, -2, 2, 5, 3, 2, 0]
line=Line('折线图示例',title_top='50%')
line.add('最高气温',attr_2,v3,mark_point=['max','min'],mark_line=['average'])
line.add('最低气温',attr_2,v4,mark_point=['max','min'],mark_line=['average'],legend_top='50%')

grid=Grid()
grid.add(bar,grid_bottom='60%')
grid.add(line,grid_top='60%')
grid.render()