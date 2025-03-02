from pyecharts import options as opts
from pyecharts.charts import Candlestick

# 数据准备
data = [
    ["2023-07-01", 900, 920, 880, 910],  # 日期，开盘价，最高价，最低价，收盘价
    ["2023-07-02", 910, 930, 890, 920],
    ["2023-07-03", 920, 950, 900, 940],
    ["2023-07-04", 940, 960, 920, 950],
    ["2023-07-05", 950, 980, 940, 970],
]

c = Candlestick()
c.add_xaxis(data[::2])  # x轴为日期
c.add_yaxis("股票A", data[1::2])  # y轴为价格，股票A的价格数据
c.set_global_opts(title_opts=opts.TitleOpts(title="K线图-基本示例"))
c.render()

    .add_yaxis(
    series_name="当天最低价",
    y_axis=low_temperature,
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max", name="最大值"),
            opts.MarkPointItem(type_="min", name="最小值"),
        ]
    ),
    markline_opts=opts.MarkLineOpts(
        data=[opts.MarkLineItem(type_="average", name="平均值")]
    ),
)

    .add_yaxis(
            series_name="当天最高价",
            y_axis=high_temperature,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )

    .add_yaxis(
    series_name="当天最低价预测",
    y_axis=low_temperature_predict,
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max", name="最大值"),
            opts.MarkPointItem(type_="min", name="最小值"),
        ]
    ),
    markline_opts=opts.MarkLineOpts(
        data=[opts.MarkLineItem(type_="average", name="平均值")]
    ),
    )

        .add_yaxis(
            series_name="当天最高价预测",
            y_axis=high_temperature_predict,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )













.add_yaxis(
            series_name="当天最高价",
            y_axis=high_temperature,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )

        .add_yaxis(
            series_name="当天最低价",
            y_axis=low_temperature,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )

        .add_yaxis(
            series_name="当天最高价预测",
            y_axis=high_temperature_predict,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )

        .add_yaxis(
            series_name="当天最低价预测",
            y_axis=low_temperature_predict,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )