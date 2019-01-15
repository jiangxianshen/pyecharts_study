from pyecharts import GeoLines,Style
style=Style(
    title_top='#fff',
    title_pos='center',
    width=1200,
    height=500,
    #background_color='#404a59'
)
style_geo=style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color='#eee',
    legend_pos='right',
    geo_effect_symbol='plane',
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos='right',
    label_formatter='{b}',
    label_text_color='#eee'
)

data_shanghai=[
    ["上海", "广州"],
    ["上海", "北京"],
    ["上海", "南京"],
    ["上海", "重庆"],
    ["上海", "兰州"],
    ["上海", "杭州"]
]
data_guangzhou=[
    ["广州", "上海", 10],
    ["广州", "北京", 20],
    ["广州", "南京", 30],
    ["广州", "重庆", 40],
    ["广州", "兰州", 50],
    ["广州", "杭州", 60]
]
data_beijing = [
    ["北京", "上海"],
    ["北京", "广州"],
    ["北京", "南京"],
    ["北京", "重庆"],
    ["北京", "兰州"],
    ["北京", "杭州"]
]
geoline=GeoLines('线路示例',**style.init_style)
geoline.add('从上海出发',data_shanghai,maptype='china',is_more_utils=True,**style_geo)
geoline.add('从广州出发',data_guangzhou,maptype='china',tooltip_formatter="{a} : {c}",is_more_utils=True,**style_geo)
geoline.add('从北京出发',data_beijing,maptype='china',is_more_utils=True,**style_geo)
geoline.render()