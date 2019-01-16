'''
WordCloud.add() 方法签名
add(name,  图例名称
attr,  属性名称
value,  属性所对应的值
shape="circle", 词云图轮廓，有'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'可选
word_gap=20, 单词间隔，默认为 20
word_size_range=None, 单词字体大小范围，默认为 [12, 60]。
rotate_step=45) 旋转单词角度，默认为 45
'''

from pyecharts import WordCloud
name=['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
    'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
    'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
    'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value=[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
    965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]

wc=WordCloud(width=1200,height=500)
wc.add('词云图',name,value,shape='star',word_size_range=[20,100])
wc.render()