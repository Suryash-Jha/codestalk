from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from codingData.callApi import getGFGData, getCodeforcesData

# Create your views here.


def getBasicData(request, id):
    res = getGFGData(id)
    res = getCodeforcesData(id)
    return JsonResponse(res)


def index(request):
    return HttpResponse("Hello, world. You're at the codingData index.")
