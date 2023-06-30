import requests
import json
import bs4
import regex as re


def getGFGData(id):
    # id= "suryashjha"
    url = f"https://auth.geeksforgeeks.org/user/{id}"
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text, "html.parser")
    try:
        total_score = soup.find_all("span", {"class": "score_card_value"})[0].string
        total_problem_solved = soup.find_all("span", {"class": "score_card_value"})[
            1
        ].string
        # print(ques_list)
        # print(soup.find_all("li", {"class": "tab"}))
        # str= "SCHOOL (66)"
        # print(str.split(" ")[1].strip("()"))

        res = {
            "status": 200,
            "user": id,
            "profile": f"https://auth.geeksforgeeks.org/user/{id}",
            "total_score": total_score,
            "total_problem_solved": total_problem_solved,
        }

    except:
        res = {
            "status": 404,
            "user": id,
            "profile": "",
            "total_score": 0,
            "total_problem_solved": 0,
        }
    return res

def getCodeforcesData(id):
    url = f"https://codeforces.com/profile/{id}"
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text, "html.parser")
    try:
        temp = soup.select("._UserActivityFrame_counterValue")[0].getText()
        total_problem_solved = int(re.search(r"\d+", temp).group())
        temp_reting = soup.select(".user-gray")[6].getText()
        print(temp_reting)
        res = {
            "status": 200,
            "user": id,
            "profile": f"https://codeforces.com/profile/{id}",
            "rating": int(temp_reting),
            "total_problem_solved": total_problem_solved,
        }

    except:
        res = {
            "status": 404,
            "user": id,
            "profile": "",
            "rating": 0,
            "total_problem_solved": 0,
        }
    return res
