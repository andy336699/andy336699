

a={
    "code": 0,
    "resultData": [
        {
            "probility": 0.00003642699,
            "location": {
                "x": 179,
                "width": 432,
                "y": 367,
                "height": 13
            },
            "text": "数据来源:SGS报:SHES150600318501-FOREO LUNA IPX-7 FOREO INC"
        },
        {
            "probility": 0.99757713,
            "location": {
                "x": 175,
                "width": 449,
                "y": 71,
                "height": 34
            },
            "text": "每一处小细节体现人性化设计"
        },
        {
            "probility": 0.9386798,
            "location": {
                "x": 596,
                "width": 161,
                "y": 282,
                "height": 19
            },
            "text": "品牌信誉优质服务"
        },
        {
            "probility": 0.99653083,
            "location": {
                "x": 188,
                "width": 111,
                "y": 257,
                "height": 19
            },
            "text": "12档强度调节"
        },
        {
            "probility": 0.99964404,
            "location": {
                "x": 346,
                "width": 88,
                "y": 281,
                "height": 19
            },
            "text": "使用450次"
        },
        {
            "probility": 0.99839586,
            "location": {
                "x": 192,
                "width": 99,
                "y": 282,
                "height": 18
            },
            "text": "减少不适感"
        },
        {
            "probility": 0.9993311,
            "location": {
                "x": 490,
                "width": 96,
                "y": 281,
                "height": 20
            },
            "text": "安全防水"
        },
        {
            "probility": 0.99016434,
            "location": {
                "x": 490,
                "width": 84,
                "y": 257,
                "height": 20
            },
            "text": "7级*保障"
        },
        {
            "probility": 0.99964345,
            "location": {
                "x": 63,
                "width": 80,
                "y": 281,
                "height": 20
            },
            "text": "不换刷头"
        },
        {
            "probility": 0.89425755,
            "location": {
                "x": 205,
                "width": 65,
                "y": 174,
                "height": 39
            },
            "text": "十-"
        },
        {
            "probility": 0.96294105,
            "location": {
                "x": 621,
                "width": 109,
                "y": 258,
                "height": 19
            },
            "text": "2年免费质保"
        },
        {
            "probility": 0.9995945,
            "location": {
                "x": 346,
                "width": 85,
                "y": 257,
                "height": 20
            },
            "text": "1小时充电"
        },
        {
            "probility": 0.9998901,
            "location": {
                "x": 63,
                "width": 77,
                "y": 257,
                "height": 20
            },
            "text": "经济实惠"
        }
    ],
    "message": "success",
    "request_id": "815774d6ed6ca43e5d0cce316d36d822"
}
reslut=[]
print(a["resultData"])
i=len(a["resultData"])
for x in a["resultData"]:
    if x["text"]:
        reslut.append(x["text"])

print(reslut)

