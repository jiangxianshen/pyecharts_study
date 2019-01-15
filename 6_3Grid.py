#上下左右类型，Bar + Line + Scatter + EffectScatter
from pyecharts import Grid,Bar,Line,Scatter,EffectScatter

attr_1=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1=[5, 20, 36, 10, 75, 90]
v2=[10, 25, 8, 60, 20, 80]
bar=Bar('柱状图示例',title_pos='65%')
bar.add('商家A',attr_1,v1,is_stack=True)
bar.add('商家B',attr_1,v2,is_stack=True,legend_pos='80%')

attr_2=["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
v3=[11, 11, 15, 13, 12, 13, 10]
v4=[1, -2, 2, 5, 3, 2, 0]
line=Line('折线图示例')
line.add('最高气温',attr_2,v3,mark_point=['max','min'],mark_line=['average'])
line.add('最低气温',attr_2,v4,mark_point=['max','min'],mark_line=['average'],legend_pos='20%')

scatter=Scatter('散点图示例',title_top="50%", title_pos="65%")
v1=[5, 20, 36, 10, 75, 90]
v2=[10, 25, 8, 60, 20, 80]
scatter.add('scatter',
            v1,
            v2,
            legend_top="50%", legend_pos="80%")

effectscatter=EffectScatter('动态散点图示例',title_top="50%")
effectscatter.add('es',
                  [11, 11, 15, 13, 12, 13, 10],
                  [1, -2, 2, 5, 3, 2, 0],
                  effect_scale=6,
                  legend_top="50%",
                  legend_pos="20%",
                  )

grid=Grid(width=1200,height=720)
grid.add(bar,grid_bottom='60%',grid_left='60%')
grid.add(line,grid_bottom='60%',grid_right='60%')
grid.add(scatter,grid_top='60%',grid_left='60%')
grid.add(effectscatter,grid_top='60%',grid_right='60%')
grid.render()