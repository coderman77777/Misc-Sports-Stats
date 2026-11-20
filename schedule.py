import requests
import json
from boxscore import get_box_score
# 12 pm (est?) refresh
def get_todays_games():
    endpoint = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
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
        # print(json.dumps(data['scoreboard'], indent=6, sort_keys=True))
        with open("example.txt", "w", encoding="utf-8") as file:
            for game in data['scoreboard']['games']:
                game_id = game['gameId']
                game_box_score = get_box_score(str(game_id))
                source =f"{game_id}\n ==============\n {game_box_score}"
                print(game_id)
                print("***********")
                print(game_box_score)
                file.write(source)


    else:
        print(f"Failed: {response.status_code}")

    