from pyecharts import Map
attr=['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
value=[20, 190, 253, 77, 65]
map=Map('广东地图示例',width=1200,height=600)
map.add('',attr,value,maptype='广东',is_visualmap=True,is_label_show=True,visual_text_color='#000')
map.render()