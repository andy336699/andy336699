from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import  csrf_exempt
from django.http import HttpResponse
import os,json

# Create your views here.
@csrf_exempt
def msgproc(request):
    dirname = 'reco_img/'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    #fo = open(dirname + request.POST[tempFiles][0]+'.png', 'wb+')
            #pic_url[-15:-5]+'.png', 'wb+')
    fo = open(dirname + 'imgreco.png', 'wb+')
    fo.write(request.FILES['image'].read())
    print(request.FILES['image'])
    fo.close()
    #print(request.FILES['image'])
    #print(request.FILES.get('name'))
    # for k, v in request.environ.items():
    #     print(k, v)

    import wx_sdk


    url = 'https://aiapi.jd.com/jdai/ocr_universal'
    #img = 'C:\fakepath\微信图片_20200514220220.jpg' 
    img = dirname + "微信图片_20200514220235.jpg"  # 上传图片的位置
    params = {
        'appkey': '8cef5cb0ad11b5055526b2c6b374ee7f',
        'secretkey': '0a6549c60bf1affd1f85737302d3d757'
    }
   
    response = wx_sdk.wx_post_req(url, params, img=img)
    # type(response.text))
    # #contents=response.text['resultData']

    print(response.text)
    # print(contents)
    contents = []
    #a=response.text["result"].json()
    a = (json.loads(response.text))["result"]
    for x in a["resultData"]:
        if x["text"]:
            contents.append(x["text"])
    #print(contents)
    for i in contents:
        print(i)
    
    return HttpResponse("成功上传")


# def msgproc(request):
#     datalist=[]
#     if request.method=="POST":

#         userA=request.POST.get("userA",None)
#         userB=request.POST.get('userB',None)
#         msg=request.POST.get("msg",None)
#         time=datetime.now()
#         with open('msgdata.txt',"a+") as f:
#             #f.write(userA)
#             f.write("{}--{}--{}--{}--\n".format(userB,userA,msg,time.strftime("%Y-%m-%d %H:%M:%S")))

#     if request.method=="GET":
#         userC=request.GET.get("userC",None)
#         if userC!=None:
#             with open("msgdata.txt","r")as f:
#                 cnt=0
#                 for line in f:
#                     linedata=line.split("--")
#                     if linedata[0]==userC:
#                         cnt=cnt+1
#                         d = {"userA": linedata[1], "msg": linedata[2], "time": linedata[3]}
#                         datalist.append(d)
#                         if cnt==10:
#                             break
#     return render(request,"MsgSingleWeb.html",{"data":datalist})


# def img_reco(request):
#     print(request)
    


