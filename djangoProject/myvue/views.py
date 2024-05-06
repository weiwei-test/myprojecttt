import json,random

from django.shortcuts import render
from django.http import JsonResponse
from myvue import models
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def get_size(request):
    if request.method == "GET":
        skc = request.GET.get("skc")
        if skc !='':
            return JsonResponse({
                "code": 20000,
                "skc": skc,
                "info": [
                    {"sku": "sku00001"},
                    {"sku": "sku00002"},
                    {"sku": "sku00003"},
                    {"sku": "sku00004"},
                ]
            }, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({
                "code": 40001,
                "message": "Missing 'sku' parameter"
            }, status=400)  # 返回400状态码表示请求错误
    else:
        return JsonResponse({
            "code": 40002,
            "message": "Invalid request method, must be GET"
        }, status=400)  # 返回400状态码表示请求错误



def order(request):
    if request.method == 'POST':
        # stockType = request.POST.get("stockType")
        # skc = request.POST.get("skc")
        request.data = json.loads(request.body)

        stockType = request.data.get("stockType")
        skc = request.data.get("skc")
        skulist = request.data.get("skulist")
        # orderQuantity = request.data.get("orderQuantity")
        if stockType != '' and skc !='':
            return JsonResponse({
                "success": True,
                "code": 20000,
                "stockType": stockType,
                "skc": skc,
                "info":[{"msg":"查询订单成功","code":0,"dmsid":random.randint(1,1000)}]

            }, json_dumps_params={"ensure_ascii": False})
        else:
            return JsonResponse({
                "success": False,
                "code": 40000,
                "message": "请输入订单号",
                "data": {
                    "stockType": "备货类型为空"
                }
            }, json_dumps_params={"ensure_ascii": False})
def login_demo(request):
    if request.method == "POST":
        request.data = json.loads(request.body)
        username = request.data.get('username')  # 字段对应表单的input属性
        password = request.data.get('password')
        user = models.User.objects.filter(username=username,password=password)
        if user:
            return JsonResponse({
    "success": True,
    "code": 20000,
    "message": "登录成功",
    "data": {
        "token": "eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSSkzJzcxT0lFKrShQsjI0NzAztDQ1MTarBQApbp7JIAAAAA.roXXX6Zevwqcuvsti-FerXDhaLFTsIn0AqpNn7bYFNAHW-X8dh3jIpShwpfWwB_eljbW4-KGTchxNpYvRj7log"
    }
},json_dumps_params={"ensure_ascii": False})
        else:
            return JsonResponse({'code':2,'message':'登录失败，请检查'},json_dumps_params={"ensure_ascii": False},status=400)
def detail_demo(request):
    if request.method == "GET":
        return JsonResponse({
    "success": True,
    "code": 20000,
    "message": "进入成功",
    "data": {
        "routes": [
            "btn.xuefen.add",
            "user"
        ],
        "buttons": [
            "3123"
        ],
        "roles": [
            "平台管理员"
        ],
        "name": "admin",
        "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
    }
},json_dumps_params={"ensure_ascii": False})

def logout_demo(request):
    if request.method=='POST':
        return JsonResponse({"success":True,"code":20000,"message":"退出成功","data":{}})



def home_list(request):
    if request.method=='GET':
        return JsonResponse({
    "success": True,
    "code": 20000,
    "message":"进入页面",
    "data": {
        "salesTotal": 114779,
        "salesToday": 112356,
        "salesGrowthLastDay": -19.16,
        "salesGrowthLastMonth": 56.67,
        "visitTotal": 88460,
        "visitToday": 1234,
        "visitTrend": [
            610,
            432,
            220,
            534,
            790,
            430,
            220,
            320,
            532,
            320,
            834,
            690,
            530,
            220,
            620
        ],
        "payTotal": 182425,
        "payRate": 60.2,
        "payTrend": [
            410,
            82,
            200,
            334,
            390,
            330,
            220,
            150,
            82,
            200,
            134,
            290,
            330,
            150
        ],
        "activityRate": 78,
        "activityGrowthLastDay": -17.7,
        "activityGrowthLastMonth": 47.12,
        "orderFullYearAxis": [
            "1月",
            "2月",
            "3月",
            "4月",
            "5月",
            "6月",
            "7月",
            "8月",
            "9月",
            "10月",
            "11月",
            "12月"
        ],
        "orderFullYear": [
            410,
            82,
            200,
            334,
            390,
            330,
            220,
            150,
            82,
            200,
            134,
            290
        ],
        "userFullYearAxis": [
            "1月",
            "2月",
            "3月",
            "4月",
            "5月",
            "6月",
            "7月",
            "8月",
            "9月",
            "10月",
            "11月",
            "12月"
        ],
        "userFullYear": [
            110,
            120,
            90,
            220,
            175,
            212,
            192,
            95,
            88,
            120,
            250,
            310
        ],
        "orderRank": [
            {
                "no": 1,
                "name": "肯德基",
                "money": "323,234"
            },
            {
                "no": 2,
                "name": "麦当劳",
                "money": "299,132"
            },
            {
                "no": 3,
                "name": "肯德基",
                "money": "283,998"
            },
            {
                "no": 4,
                "name": "海底捞",
                "money": "266,223"
            },
            {
                "no": 5,
                "name": "西贝筱面村",
                "money": "223,445"
            },
            {
                "no": 6,
                "name": "汉堡王",
                "money": "219,663"
            },
            {
                "no": 7,
                "name": "真功夫",
                "money": "200,997"
            }
        ],
        "userRank": [
            {
                "no": 1,
                "name": "麦当劳",
                "money": "211,335"
            },
            {
                "no": 2,
                "name": "肯德基",
                "money": "210,597"
            },
            {
                "no": 3,
                "name": "必胜客",
                "money": "200,998"
            },
            {
                "no": 4,
                "name": "海底捞",
                "money": "199,220"
            },
            {
                "no": 5,
                "name": "西贝筱面村",
                "money": "195,444"
            },
            {
                "no": 6,
                "name": "汉堡王",
                "money": "180,161"
            },
            {
                "no": 7,
                "name": "真功夫",
                "money": "172,995"
            }
        ],
        "searchWord": [
            {
                "word": "北京",
                "count": 3440,
                "user": 1626
            },
            {
                "word": "上海",
                "count": 8101,
                "user": 6660
            },
            {
                "word": "广州",
                "count": 7814,
                "user": 2196
            },
            {
                "word": "深圳",
                "count": 8888,
                "user": 7102
            },
            {
                "word": "南京",
                "count": 6204,
                "user": 1949
            },
            {
                "word": "杭州",
                "count": 8159,
                "user": 3548
            },
            {
                "word": "合肥",
                "count": 269,
                "user": 151
            },
            {
                "word": "济南",
                "count": 2045,
                "user": 1320
            },
            {
                "word": "太原",
                "count": 5693,
                "user": 2297
            },
            {
                "word": "成都",
                "count": 4850,
                "user": 1635
            },
            {
                "word": "重庆",
                "count": 906,
                "user": 269
            },
            {
                "word": "苏州",
                "count": 5576,
                "user": 3937
            },
            {
                "word": "无锡",
                "count": 1576,
                "user": 796
            },
            {
                "word": "常州",
                "count": 9002,
                "user": 8508
            },
            {
                "word": "温州",
                "count": 8103,
                "user": 4903
            },
            {
                "word": "哈尔滨",
                "count": 7961,
                "user": 6173
            },
            {
                "word": "长春",
                "count": 5916,
                "user": 3117
            },
            {
                "word": "大连",
                "count": 5012,
                "user": 78
            },
            {
                "word": "沈阳",
                "count": 8410,
                "user": 5696
            },
            {
                "word": "拉萨",
                "count": 3385,
                "user": 2547
            },
            {
                "word": "呼和浩特",
                "count": 4672,
                "user": 34
            },
            {
                "word": "武汉",
                "count": 7386,
                "user": 4047
            },
            {
                "word": "南宁",
                "count": 6192,
                "user": 612
            },
            {
                "word": "必胜客",
                "count": 3504,
                "user": 2480
            },
            {
                "word": "肯德基",
                "count": 3727,
                "user": 2527
            },
            {
                "word": "麦当劳",
                "count": 8959,
                "user": 6198
            },
            {
                "word": "海底捞",
                "count": 5295,
                "user": 2264
            },
            {
                "word": "美食",
                "count": 7348,
                "user": 5555
            },
            {
                "word": "商超",
                "count": 1628,
                "user": 1295
            },
            {
                "word": "水果",
                "count": 892,
                "user": 215
            },
            {
                "word": "跑腿",
                "count": 254,
                "user": 40
            },
            {
                "word": "送药",
                "count": 8377,
                "user": 4363
            },
            {
                "word": "烩饭",
                "count": 2009,
                "user": 1080
            },
            {
                "word": "面条",
                "count": 7684,
                "user": 4299
            },
            {
                "word": "小龙虾",
                "count": 3187,
                "user": 562
            },
            {
                "word": "牛肉",
                "count": 3612,
                "user": 3449
            },
            {
                "word": "鸡腿",
                "count": 4460,
                "user": 367
            },
            {
                "word": "全家桶",
                "count": 7206,
                "user": 3682
            },
            {
                "word": "麦乐鸡",
                "count": 3383,
                "user": 3048
            },
            {
                "word": "炭烤",
                "count": 8818,
                "user": 26
            },
            {
                "word": "麻辣",
                "count": 1297,
                "user": 905
            },
            {
                "word": "冒菜",
                "count": 3015,
                "user": 2362
            }
        ],
        "saleRank": {
            "online": {
                "name": [
                    "家用电器",
                    "食用酒水",
                    "个护健康",
                    "服饰箱包",
                    "母婴产品",
                    "其他"
                ],
                "value": [
                    244,
                    321,
                    301,
                    41,
                    111,
                    69
                ]
            },
            "shop": {
                "name": [
                    "家用电器",
                    "食用酒水",
                    "个护健康",
                    "服饰箱包",
                    "母婴产品",
                    "其他"
                ],
                "value": [
                    68,
                    15,
                    41,
                    56,
                    70,
                    25,
                    31
                ]
            }
        }
    }
})
















# 定义其他接口...
