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
    finRes = {}
    tot = 0
    id_codechef = userDetails.objects.get(codestalk_handle=id).id_codechef
    id_codeforces = userDetails.objects.get(codestalk_handle=id).id_codeforces
    id_hackkerank = userDetails.objects.get(codestalk_handle=id).id_hackkerank
    id_gfg = userDetails.objects.get(codestalk_handle=id).id_gfg
    id_leetcode = userDetails.objects.get(codestalk_handle=id).id_leetcode
    DbObj = userDetails.objects.get(codestalk_handle=id)

    try:
        res = getGFGData(id_gfg)
        finRes["total_question_gfg"] = res["total_problem_solved"]
        DbObj.totalQuestions_gfg = res["total_problem_solved"]
        DbObj.save()
        tot += int(res["total_problem_solved"])

        res = getCodeforcesData(id_codeforces)
        finRes["total_question_cf"] = res["total_problem_solved"]
        DbObj.totalQuestions_codeforces = res["total_problem_solved"]
        DbObj.save()
        tot += int(res["total_problem_solved"])

        res = getCodechefData(id_codechef)
        finRes["total_question_cc"] = res["total_problem_solved"]
        DbObj.totalQuestions_codechef = res["total_problem_solved"]
        DbObj.save()
        tot += int(res["total_problem_solved"])

        res = getLeetcodeData(id_leetcode)
        finRes["total_question_lc"] = res["total_problem_solved"]
        DbObj.totalQuestions_leetcode = res["total_problem_solved"]
        DbObj.save()
        tot += int(res["total_problem_solved"])

        res = getHackkerankData(id_hackkerank)
        finRes["total_question_hk"] = res["total_problem_solved"]
        DbObj.totalQuestions_hackkerank = res["total_problem_solved"]
        DbObj.save()
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


def getAllUsers(request):
    usr = userDetails.objects.all()
    print(usr)
    return render(request, "showApiRes.html", {"finRes": usr})
