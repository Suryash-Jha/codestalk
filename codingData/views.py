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
import time

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


def IdExists(id):
    try:
        userDetails.objects.get(codestalk_handle=id)
    except userDetails.DoesNotExist:
        return False
    return True


def retrieveFromDb(request, id):
    finRes = {}
    try:
        if IdExists(id):
            DatafromDb = userDetails.objects.get(codestalk_handle=id)
            finRes = {
                "status": 200,
                "total_question_gfg": DatafromDb.totalQuestions_gfg,
                "total_question_cf": DatafromDb.totalQuestions_codeforces,
                "total_question_cc": DatafromDb.totalQuestions_codechef,
                "total_question_lc": DatafromDb.totalQuestions_leetcode,
                "total_question_hk": DatafromDb.totalQuestions_hackkerank,
                "total_question": DatafromDb.totalQuestions_codeforces
                + DatafromDb.totalQuestions_codechef
                + DatafromDb.totalQuestions_gfg
                + DatafromDb.totalQuestions_hackkerank
                + DatafromDb.totalQuestions_leetcode,
                "id": id,
            }
        else:
            finRes = {
                "status": 402,
                "total_question_gfg": 0,
                "total_question_cf": 0,
                "total_question_cc": 0,
                "total_question_lc": 0,
                "total_question_hk": 0,
                "total_question": 0,
                "id": id,
                "error": "Id does not exist",
            }

    except Exception as e:
        finRes = {
            "status": 404,
            "total_question_gfg": 0,
            "total_question_cf": 0,
            "total_question_cc": 0,
            "total_question_lc": 0,
            "total_question_hk": 0,
            "total_question": 0,
            "id": id,
            "error": str(e),
        }
        # return HttpResponse("Id does not exist")
    return render(request, "showApiRes.html", {"finRes": finRes})


def apiRes(request, id):
    platforms = {
        "id_codechef": {
            "data_function": getCodechefData,
            "result_key": "total_question_cc",
        },
        "id_codeforces": {
            "data_function": getCodeforcesData,
            "result_key": "total_question_cf",
        },
        "id_hackkerank": {
            "data_function": getHackkerankData,
            "result_key": "total_question_hk",
        },
        "id_gfg": {"data_function": getGFGData, "result_key": "total_question_gfg"},
        "id_leetcode": {
            "data_function": getLeetcodeData,
            "result_key": "total_question_lc",
        },
    }

    finRes = {}
    tot = 0

    try:
        for platform, platform_data in platforms.items():
            platform_id = getattr(
                userDetails.objects.get(codestalk_handle=id), platform
            )
            try:
                start_time = time.time()
                res = platform_data["data_function"](platform_id)
                duration = time.time() - start_time
                finRes[platform_data["result_key"]] = res["total_problem_solved"]
                finRes[platform_data["result_key"] + "_duration"] = duration
                tot += int(res["total_problem_solved"])
            except Exception:
                finRes[platform_data["result_key"]] = 0
                finRes[platform_data["result_key"] + "_duration"] = 0

        finRes["total_question"] = tot
        finRes["id"] = id
    except Exception as e:
        finRes = {
            "total_question_gfg": 0,
            "total_question_cf": 0,
            "total_question_cc": 0,
            "total_question_lc": 0,
            "total_question_hk": 0,
            "total_question": 0,
            "id": id,
        }

    return JsonResponse(finRes)


def index(request):
    return HttpResponse("Hello, world. You're at the codingData index.")
