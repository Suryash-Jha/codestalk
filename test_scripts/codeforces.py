import requests
import bs4
import regex as re

response = requests.get(f"https://codeforces.com/profile/{id}")
soup = bs4.BeautifulSoup(response.text, "html.parser")
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

print(res)
