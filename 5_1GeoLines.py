'''
用于带有起点和终点信息的线数据的绘制，主要用于地图上的航线，路线的可视化
GeoLines.add() 方法签名
add(name, 图例名称
    data, 数据项 ["广州", "北京"，100]，则指定从广州到北京。第三个值用于表示该 line 的数值
    maptype='china',地图类型
    coordinate_region="中国", 城市坐标所属国家
    symbol=None, 线两端的标记类型
    symbol_size=12, 线两端的标记大小
    border_color="#111", 地图边界颜色
    geo_normal_color="#323c48", 正常状态下地图区域的颜色
    geo_emphasis_color="#2a333d",高亮状态下地图区域的颜色
    geo_cities_coords=None, 用户自定义地区经纬度
    geo_effect_period=6, 特效动画的时间，单位为 s，默认为 6s
    geo_effect_traillength=0, 特效尾迹的长度。取从 0 到 1 的值，数值越大尾迹越长。默认为 0
    geo_effect_color='#fff', 特效标记的颜色
    geo_effect_symbol='circle', 特效图形的标记。有 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'plane' 可选
    geo_effect_symbolsize=5, 特效标记的大小
    is_geo_effect_show=True, 是否显示特效
    is_roam=True, **kwargs) 是否开启鼠标缩放和平移漫游
'''

from pyecharts import GeoLines,Style
style=Style(
    title_top='#fff',
    title_pos='center',
    width=1200,
    height=500,
    background_color='#404a59'
)
data_guangzhou=[
    ["广州", "上海"],
    ["广州", "北京"],
    ["广州", "南京"],
    ["广州", "重庆"],
    ["广州", "兰州"],
    ["广州", "杭州"]
]
geoline=GeoLines('线路示例',**style.init_style)
geoline.add('从广州出发',data_guangzhou,maptype='china',is_legend_show=False)
geoline.render()
