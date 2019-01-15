# Line + Pie

from pyecharts import Grid,Pie,Line

attr_2=["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
v3=[11, 11, 15, 13, 12, 13, 10]
v4=[1, -2, 2, 5, 3, 2, 0]
line=Line('折线图示例')
line.add('最高气温',attr_2,v3,mark_point=['max','min'],mark_line=['average'])
line.add('最低气温',attr_2,v4,mark_point=['max','min'],mark_line=['average'],legend_pos='20%')

attr_1=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1=[5, 20, 36, 10, 75, 90]
pie=Pie('饼图示例',title_pos='55%')
pie.add('',attr_1,v1,radius=[45,65],center=[65,50],legend_pos='80%',legend_orient='vertical')

grid=Grid(width=1200)
grid.add(line,grid_right='55%')
grid.add(pie,grid_left='60%')
grid.render()