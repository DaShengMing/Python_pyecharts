# -*- coding:utf-8 -*-


from pyecharts import Geo, Style


style = Style(
    title_top = "#fff",
    title_pos = "left",
    width = 1000,
    height = 800,
    background_color = "#404a59"
    )

data = [['北京', '阿拉善左旗'],['北京', '阿克苏'],['北京', '安顺'],['北京', '鞍山'],
        ['北京', '包头'],['北京', '白城'],['北京', '毕节'],['北京', '保山'],['北京', '巴彦淖尔'],
        ['北京', '松原'],['北京', '深圳'],['北京', '三亚'],['北京', '上海'],['北京', '十堰']]

style_geo = style.add(is_label_show=True,
                      line_curve=0.2,#曲线的弯曲度
                      line_opacity=0.5,#航线的透明度
                      legend_text_color="#eee",
                      legend_pos="right",#示例的位置
                      geo_effect_symbol="plane",
                      geo_effect_symbolsize=10,#飞机大小
                      label_color=['#ffa022', '#ffa022', '#46bee9'],
                      label_pos="right",
                      label_formatter="{b}",#地方标签的格式
                      label_text_color="#eee",)

geolines = Geo("GeoLines 示例",**style.init_style)#相当于设置背景
geolines.add("从北京出发",data,tooltip_formatter="{a} : {c}", **style_geo)


geolines.render("F:/Python-study-diary/pyechartsss/airport1.html")

