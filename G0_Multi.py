# -*- coding:utf-8 -*-
# 制作3D动态航线图(多例模式)

from pyecharts import GeoLines, Style

style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#404a59"
    )

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

data_guangzhou = [
    ["广州", "上海"],
    ["广州", "北京"],
    ["广州", "南京"],
    ["广州", "重庆"],
    ["广州", "兰州"],
    ["广州", "杭州"]
]

data_beijing = [
    ["北京", "上海"],
    ["北京", "广州"],
    ["北京", "南京"],
    ["北京", "重庆"],
    ["北京", "兰州"],
    ["北京", "杭州"]
]

data_dalian=[
    ["大连","银川"],
    ["大连", "杭州"],
    ["大连", "拉萨"],
    ["大连", "沈阳"],
    ["大连", "昆明"],
    ["大连", "石河子"]
    ]

geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从广州出发", data_guangzhou, **style_geo)
geolines.add("从北京出发", data_beijing, **style_geo)
geolines.add("从大连出发", data_dalian, **style_geo)
geolines.render("F:/Python-study-diary/pyechartsss/airport5.html")


