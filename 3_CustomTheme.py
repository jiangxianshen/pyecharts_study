
'''
echarts-themes-pypkg 提供了 vintage, macarons, infographic, shine 和 roma 主题
# 更换单个主题
bar.use_theme('vintage')
# 更换运行环境所有主题
from pyecharts import configure  置顶
configure(global_theme="dark")
'''

from pyecharts import Bar
import random
bar=Bar('图表标题','图标副标题')
bar.use_theme('roma')
kind=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
bar.add('商家A',kind,[random.randint(10,100) for _ in range(6)],is_more_utils=True)
bar.add('商家B',kind,[random.randint(10,100) for _ in range(6)],is_more_utils=True)
bar.add('商家C',kind,[random.randint(10,100) for _ in range(6)],is_more_utils=True)
bar.add('商家D',kind,[random.randint(10,100) for _ in range(6)],is_more_utils=True)
bar.render()

'''
使用pyecharts-snapshot插件保存图形
如果想直接将图片保存为 png, pdf, gif 格式的文件，可以使用 pyecharts-snapshot
调用 render 方法  bar.render(path='snapshot.png') 文件结尾可以为 svg/jpeg/png/pdf/gif。
请注意，svg 文件需要你在初始化 bar 的时候设置 renderer='svg'。
'''
bar.render(path='snapshot.png')