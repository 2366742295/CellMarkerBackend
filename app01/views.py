from django.core import serializers
from django.http import HttpResponse
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