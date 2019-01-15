'''
Map.add() 方法签名
add(name, attr, value,
    maptype='china',
    is_roam=True,
    is_map_symbol_show=True, **kwargs)
name -> str
图例名称
attr -> list
属性名称
value -> list
属性所对应的值
maptype -> str
地图类型。
is_roam -> bool/str
是否开启鼠标缩放和平移漫游。默认为 True
如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启
is_map_symbol_show -> bool
是否显示地图标记红点，默认为 True。

'''
from pyecharts import Map
attr=["福建","山东","北京","上海"]
value=[155, 10, 66, 78]
map=Map('全国地图实例',width=1200,height=600)
# 1、基本显示
# map.add("",attr,value,maptype='china',is_roam=True,is_map_symbol_show=True)
# 2、显示各区域名称
# map.add("",attr,value,maptype='china',is_label_show=True,is_more_utils=True)
# 3、结合Visualmap 使用
map.add("",attr,value,maptype='china',is_label_show=True,is_visualmap=True)
map.render()