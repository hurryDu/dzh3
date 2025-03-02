from flask import Flask,render_template
from django.shortcuts import render
from django.http  import JsonResponse
app=Flask(__name__)

#创建了网址 /show/info 和函数index的对应关系
#以后用户在浏览器上访问 /show/info,网站自动执行 index

@app.route("/show/info")
def index():
    ##return "中<h1>国</h1><span style='color:red;'>联通</span>"
    return render_template("index.html")

@app.route("/goods/list")
def goods_list():
    return render_template("goods_list.html")

@app.route("/show/ch")
def show_ch():
    return render_template('chart.html')

@app.route("/good/ga")
def chart_list(requset):
    "“”数据统计页面“”"
    return render(requset,'chart_list.html')

def chart_bar(request):
    """构造柱状图的数据"""
    #数据可以去数据库获取
    legend=["销量","业绩"]
    series_list=[
          {
            "name": '销量',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
          },
            {
            "name": '业绩',
            "type": 'bar',
            "data": [15, 10, 18, 58, 40, 25]
            }
        ]
    x_axis=['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    result={
        "status":True,
        "data":{
           'legend':legend,
            'series_list':series_list,
            'x_axis':x_axis,
        }
    }
    return JsonResponse(result)

@app.route("/")
def login():
    return render_template("add_user.html")

if __name__=='__main__':
    app.run()