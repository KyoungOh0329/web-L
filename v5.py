import requests
import json

def get_summoner_info(api_key, summoner_name, region):
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_match_history(api_key, account_id, region):
    url = f"https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}"
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_match_details(api_key, match_id, region):
    url = f"https://{region}.api.riotgames.com/lol/match/v4/matches/{match_id}"
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

# 사용 예시
api_key = "RGAPI-c2db0de1-1f29-4ae7-acd1-1ff6e5965397"
summoner_name = "정경오"
region = "KR"

# 소환사 정보 조회
summoner_info = get_summoner_info(api_key, summoner_name, region)
print("Summoner Info:")
print(json.dumps(summoner_info, indent=4))

# 소환사의 전적 조회
account_id = summoner_info["accountId"]
match_history = get_match_history(api_key, account_id, region)
print("Match History:")
print(json.dumps(match_history, indent=4))

# 매치 상세 정보 조회
match_id = match_history["matches"][0]["gameId"]
match_details = get_match_details(api_key, match_id, region)
print("Match Details:")
print(json.dumps(match_details, indent=4))
