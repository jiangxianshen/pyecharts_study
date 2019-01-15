from pyecharts import Bar
bar=Bar('图表标题','图标副标题')
kind=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
bar.add('服装',kind,[5,20,36,10,75,90],is_more_utils=True)
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
bar.render() # 生成本地HTML文件
'''
add() : 主要方法，用于添加图表的数据和设置各种配置项
print_echarts_options() :打印输出图表的所有配置项
render():默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，
如 render(r"e:\my_first_chart.html")，文件用浏览器打开。
Note： 可以按右边的下载按钮将图片下载到本地，如果想要提供更多实用工具按钮，请在 add() 中设置 is_more_utils 为 True

'''