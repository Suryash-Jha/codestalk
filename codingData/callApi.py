import requests
import json
import bs4
import regex as re


def getGFGData(id):
    try:
        url = f"https://auth.geeksforgeeks.org/user/{id}"
        html = requests.get(url)
        soup = bs4.BeautifulSoup(html.text, "html.parser")
        total_score = soup.find_all("span", {"class": "score_card_value"})[0].string
        total_problem_solved = soup.find_all("span", {"class": "score_card_value"})[
            1
        ].string

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
    try:
        url = f"https://codeforces.com/profile/{id}"
        html = requests.get(url)
        soup = bs4.BeautifulSoup(html.text, "html.parser")
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


def getCodechefData(id):
    try:
        response = requests.get(f"https://www.codechef.com/users/{id}")
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        soup = soup.find_all("section", class_="rating-data-section problems-solved")
        h5 = soup[0].find_all("h5")[0].getText()
        questionVal = int(re.search(r"\d+", h5).group())
        res = {
            "status": 200,
            "user": id,
            "profile": f"https://www.codechef.com/users/{id}",
            "total_problem_solved": questionVal,
        }
    except:
        res = {
            "status": 404,
            "user": id,
            "profile": "",
            "total_problem_solved": 0,
        }
    return res


def getHaackkerankData(id):
    try:
        cookies = {
            'hackerrank_mixpanel_token': 'c8badb28-5dcd-4e85-9c1d-df4479d1db0f',
            '_ga': 'GA1.2.866134674.1688145707',
            '_gid': 'GA1.2.1640686629.1688145707',
            'hrc_l_i': 'F',
            '_hrank_session': '933cbb1af73c8b65882cf9de30e41d9c',
            'user_type': 'hacker',
            '_gat_UA-45092266-28': '1',
            '_gat_UA-45092266-26': '1',
            '_hp2_id.547804831': '%7B%22userId%22%3A%221470468072689568%22%2C%22pageviewId%22%3A%224522818040282766%22%2C%22sessionId%22%3A%221450101182291234%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
            '_hp2_ses_props.547804831': '%7B%22ts%22%3A1688198394509%2C%22d%22%3A%22www.hackerrank.com%22%2C%22h%22%3A%22%2Fjoblesscoder2468%22%2C%22q%22%3A%22%3Fhr_r%3D1%22%7D',
        }

        headers = {
            'authority': 'www.hackerrank.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'if-none-match': 'W/"fe5b9cef0b2f678db37085baccd65b45"',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
            'x-csrf-token': '+HoDulpylNUOhoKX2qbc7oFyvCzBCUdpI8Uk8sKXm+ZiX4rJ2UAg8KqEPtnaWkeezkj0FD91clingBpKkMgeTg==',
        }

    response = requests.get('https://www.hackerrank.com/rest/hackers/joblesscoder2468/badges', cookies=cookies, headers=headers)
    print(response.text)
    except:
        pass