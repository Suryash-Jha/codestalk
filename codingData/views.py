from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from codingData.models import userDetails
from codingData.callApi import (
    getGFGData,
    getCodeforcesData,
    getCodechefData,
    getHackkerankData,
    getLeetcodeData,
)
from django import forms

# Create your views here.


class BasicData(forms.ModelForm):
    id_leetcode = forms.CharField(required=False)
    id_codeforces = forms.CharField(required=False)
    id_codechef = forms.CharField(required=False)
    id_gfg = forms.CharField(required=False)
    id_hackkerank = forms.CharField(required=False)

    class Meta:
        model = userDetails
        fields = (
            "name",
            "codestalk_handle",
            "country",
            "university",
            "id_leetcode",
            "id_codeforces",
            "id_codechef",
            "id_gfg",
            "id_hackkerank",
        )


def getBasicData(request, id):
    # res = getGFGData(id)
    # res = getCodeforcesData(id)
    # res = getCodechefData(id)
    # res = getHackkerankData(id)
    res = getLeetcodeData(id)

    return JsonResponse(res)


def createId(request):
    if request.method == "POST":
        print(request.POST)
        form = BasicData(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
    else:
        form = BasicData()
    return render(request, "createId.html", {"form": form})
    # return render(request, "createId.html")


def index(request):
    return HttpResponse("Hello, world. You're at the codingData index.")
