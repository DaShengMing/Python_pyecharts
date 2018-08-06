# -*- coding:utf-8 -*-
# 制作3D动态航线图

from pyecharts import GeoLines, Style

style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#404a59"
    )

data_beijing = [
    ["北京", "上海"],
    ["北京", "广州"],
    ["北京", "南京"],
    ["北京", "重庆"],
    ["北京", "兰州"],
    ["北京", "杭州"]
]

style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
)
geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从北京出发", data_beijing, **style_geo)
geolines.render("F:/Python-study-diary/pyechartsss/airport3.html")





