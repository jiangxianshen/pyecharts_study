from pyecharts import Map
attr=["China", "Canada", "Brazil", "Russia", "United States"]
value=[95.1, 23.2, 43.3, 66.4, 88.5]
map=Map('世界地图示例',width=1200,height=500)
map.add(
    '',
    attr,
    value,
    maptype='world',
    is_label_show=False,
    is_visualmap=True,
    is_map_symbol_show=False,
    visual_text_color='#000'
    )
map.render()