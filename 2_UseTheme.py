from pyecharts import Bar
bar=Bar('图表标题','图标副标题')
bar.use_theme('dark')
kind=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
bar.add('服装',kind,[5,20,36,10,75,90],is_more_utils=True)
bar.render()