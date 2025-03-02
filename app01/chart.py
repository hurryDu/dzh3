from django.shortcuts import render
from django.http  import JsonResponse
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