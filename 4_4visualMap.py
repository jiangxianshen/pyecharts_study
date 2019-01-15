from pyecharts import Map
attr=["福建", "山东", "北京", "上海"]
value=[155, 10, 66, 78]
map=Map('china map',width=1200,height=500)
map.add('',attr,value,maptype='china',
        is_visualmap=True,
        visual_text_color='#000',
        is_piecewise=True,
        visual_range_text=['',''],
        pieces=[
            {'max':160,'min':70,'label':'高数值'},
            {'max':69,'min':0,'label':'低数值'}
        ]
        )
map.render()