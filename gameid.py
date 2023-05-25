import json
import requests
import pandas as pd
from time import sleep

api_key = "RGAPI-b9e70107-acf0-471c-b7cf-927551687783"   

csv = pd.read_csv('Name.csv', encoding="UTF-8")
name = csv['Name']

Game_id = []
for i in range(len(name)):
    try:
        URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name[i]
        res = requests.get(URL, headers={"X-Riot-Token": api_key})
        resobj = json.loads(res.text)
        URL = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + resobj["puuid"]+"/ids?start=0&count=100"
        res = requests.get(URL, headers={"X-Riot-Token": api_key})
        resobj = json.loads(res.text)
        for j in range(len(resobj)):
            Game_id.append(resobj[j])
            print(len(Game_id))
    except:
        print(i)
        continue
    sleep(3)

temp = set(Game_id)
Game_id = list(temp)

df = pd.DataFrame(Game_id, columns=['Game_id'])
df.to_csv('Game_id.csv', index=False, encoding='utf-8')