import requests


cookies = {
    'csrftoken': 'e38vNeiVnsnfPyB1VRVqnh5yt4ntKoPDUZixqOOrG2vEfw3qr97CFryDaoz0ZoH0',
    '_gid': 'GA1.2.1323516888.1688200682',
    '_gat': '1',
    'gr_user_id': 'ebcd5b7b-e372-4835-a94c-ce75ccc7b439',
    '87b5a3c3f1a55520_gr_session_id': 'b1d3499c-448c-47d0-a0a2-9440c9deb21c',
    '87b5a3c3f1a55520_gr_session_id_sent_vst': 'b1d3499c-448c-47d0-a0a2-9440c9deb21c',
    '_ga': 'GA1.1.1281938833.1688200682',
    '_dd_s': 'rum=0&expire=1688201587060',
    '_ga_CDRWKZTDEX': 'GS1.1.1688200682.1.0.1688200687.55.0.0',
}

headers = {
    'authority': 'leetcode.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': '',
    'baggage': 'sentry-environment=production,sentry-release=fb09be80,sentry-transaction=%2Fu%2F%5Busername%5D,sentry-public_key=2a051f9838e2450fbdd5a77eb62cc83c,sentry-trace_id=1f645152822d40fc9f7df289b70caa8b,sentry-sample_rate=0.03',
    'content-type': 'application/json',
    # 'cookie': 'csrftoken=e38vNeiVnsnfPyB1VRVqnh5yt4ntKoPDUZixqOOrG2vEfw3qr97CFryDaoz0ZoH0; _gid=GA1.2.1323516888.1688200682; _gat=1; gr_user_id=ebcd5b7b-e372-4835-a94c-ce75ccc7b439; 87b5a3c3f1a55520_gr_session_id=b1d3499c-448c-47d0-a0a2-9440c9deb21c; 87b5a3c3f1a55520_gr_session_id_sent_vst=b1d3499c-448c-47d0-a0a2-9440c9deb21c; _ga=GA1.1.1281938833.1688200682; _dd_s=rum=0&expire=1688201587060; _ga_CDRWKZTDEX=GS1.1.1688200682.1.0.1688200687.55.0.0',
    'origin': 'https://leetcode.com',
    'random-uuid': '909503ed-4faa-7f67-4d29-62be840c4893',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '1f645152822d40fc9f7df289b70caa8b-a47a2cbe659bccd4-1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'x-csrftoken': 'e38vNeiVnsnfPyB1VRVqnh5yt4ntKoPDUZixqOOrG2vEfw3qr97CFryDaoz0ZoH0',
}

json_data = {
    'query': '\n    query userProblemsSolved($username: String!) {\n  allQuestionsCount {\n    difficulty\n    count\n  }\n  matchedUser(username: $username) {\n    problemsSolvedBeatsStats {\n      difficulty\n      percentage\n    }\n    submitStatsGlobal {\n      acSubmissionNum {\n        difficulty\n        count\n      }\n    }\n  }\n}\n    ',
    'variables': {
        'username': f'{id}',
    },
    'operationName': 'userProblemsSolved',
}

response = requests.post('https://leetcode.com/graphql/', cookies=cookies, headers=headers, json=json_data)
json_data = response.json()
totalQues = int(json_data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][0]['count'])
print(FIN_DATA)
# print(response.text)