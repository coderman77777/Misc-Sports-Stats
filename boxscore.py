import requests
import json

def get_box_score(game_code):
    endpoint = f"https://cdn.nba.com/static/json/liveData/boxscore/boxscore_{game_code}.json"
    custom_headers = {
       'Host': 'cdn.nba.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.9',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Referer': 'https://www.nba.com/',
'Origin': 'https://www.nba.com',
'Connection': 'keep-alive',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site',
'Priority': 'u=4',
'TE': 'trailers', 
    }

    response = requests.get(endpoint, headers=custom_headers)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data['game'], indent=4, sort_keys=True))
        return json.dumps(data['game'], indent=4, sort_keys=True)
    else:
        print(f"Failed: {response.status_code}")

    