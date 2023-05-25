import requests
import json
import pandas as pd

api_key = "RGAPI-b9e70107-acf0-471c-b7cf-927551687783"

tier_limits = {
    "challenger": 250,
    "grandmaster": 300,
    "master": 1000,
    "diamond": 1000,
    "platinum": 1500,
    "gold": 2000,
    "silver": 1500,
    "bronze": 1300,
    "iron": 300
}

Name = []

for tier, limit in tier_limits.items():
    URL = f"https://kr.api.riotgames.com/lol/league/v4/{tier}leagues/by-queue/RANKED_SOLO_5x5"
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    resobj = json.loads(res.text)
    if "entries" in resobj:
        entries = resobj["entries"][:limit]
        for entry in entries:
            summoner_name = entry.get("summonerName")
            if summoner_name:
                Name.append(summoner_name)
            else:
                print(f"No summonerName found for {tier} tier.")
    else:
        print(f"No entries found for {tier} tier.")

df = pd.DataFrame(Name, columns=['Name'])
df.to_csv('Name.csv', index=False, encoding='utf-8')
