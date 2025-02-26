from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from app01 import models


def GetUserId(request):
    userId = models.User.objects.all()
    json_data = serializers.serialize('json', userId)
    response = HttpResponse(json_data)
    response["Access-Control-Allow-Origin"] = "*"
    return response

def CreateUser(request):
    models.User.objects.create(name="用户1")
    return HttpResponse("创建成功")

def Test(request):
    return HttpResponse("测试")


def GetSampleData(request):
    # 获取分页参数
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    try:
        page_size = int(page_size)
        if page_size not in [5, 10, 20, 50]:
            page_size = 10
    except ValueError:
        page_size = 10

    # 获取数据并分页
    queryset = models.SampleInfo_forTest.objects.all().order_by('sample_id')
    paginator = Paginator(queryset, page_size)

    try:
        page_obj = paginator.page(page_number)
    except:
        page_obj = paginator.page(1)

    # 构造响应数据
    response_data = {
        "results": [
            {"fields": {field.name: getattr(obj, field.name) for field in obj._meta.fields}}
            for obj in page_obj
        ],
        "current_page": page_obj.number,
        "total_pages": paginator.num_pages,
        "total_items": paginator.count
    }
    response = JsonResponse(response_data)
    # 添加CORS头
    response["Access-Control-Allow-Origin"] = "*"
    return response