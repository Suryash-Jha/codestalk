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


# http://127.0.0.1:8000/api/suryashjha123


def getBasicData(request, id):
    # res = getGFGData(id)
    res = getCodeforcesData(id)
    # res = getCodechefData(id)
    # res = getHackkerankData(id)
    # res = getLeetcodeData(id)

    return JsonResponse(res)


def createId(request):
    statusCode = 200
    status = ""

    if request.method == "POST":
        try:
            form = BasicData(request.POST)
            if form.is_valid():
                form.save()

        except Exception as e:
            statusCode = 404
            status = "Failed to save data" + str(e)
    else:
        form = BasicData()
    return render(
        request,
        "createId.html",
        {"form": form, "status": status, "statusCode": statusCode},
    )
    # return render(request, "createId.html")


def apiRes(request, id):
    finRes = {}
    tot = 0
    id_codechef = userDetails.objects.get(codestalk_handle=id).id_codechef
    id_codeforces = userDetails.objects.get(codestalk_handle=id).id_codeforces
    id_hackkerank = userDetails.objects.get(codestalk_handle=id).id_hackkerank
    id_gfg = userDetails.objects.get(codestalk_handle=id).id_gfg
    id_leetcode = userDetails.objects.get(codestalk_handle=id).id_leetcode

    try:
        res = getGFGData(id_gfg)
        finRes["total_question_gfg"] = res["total_problem_solved"]
        tot += int(res["total_problem_solved"])

        res = getCodeforcesData(id_codeforces)
        finRes["total_question_cf"] = res["total_problem_solved"]
        tot += int(res["total_problem_solved"])

        res = getCodechefData(id_codechef)
        finRes["total_question_cc"] = res["total_problem_solved"]
        tot += int(res["total_problem_solved"])

        res = getLeetcodeData(id_leetcode)
        finRes["total_question_lc"] = res["total_problem_solved"]
        tot += int(res["total_problem_solved"])

        res = getHackkerankData(id_hackkerank)
        finRes["total_question_hk"] = res["total_problem_solved"]
        tot += int(res["total_problem_solved"])

        finRes["total_question"] = tot

    except Exception as e:
        finRes["total_question_gfg"] = 0
        finRes["total_question_cf"] = 0
        finRes["total_question_cc"] = 0
        finRes["total_question_lc"] = 0
        finRes["total_question_hk"] = 0
        finRes["total_question"] = 0
        finRes["error"] = str(e)

    return JsonResponse(finRes)


def index(request):
    return HttpResponse("Hello, world. You're at the codingData index.")
