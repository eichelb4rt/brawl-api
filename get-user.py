import json
import requests
from dotenv import dotenv_values


config = dotenv_values(".env")
API_TOKEN = config["API_TOKEN"]


def find_steam(steam_id: int) -> int:
    res = requests.get(f"https://api.brawlhalla.com/search", params={
        "api_key": API_TOKEN,
        "steamid": steam_id
    })
    return int(res.json()["brawlhalla_id"])


def get_rankings(name: str):
    res = requests.get(f"https://api.brawlhalla.com/rankings/1v1/eu/1", params={
        "api_key": API_TOKEN,
        "name": name
    })
    return res.json()


def get_ranked(brawl_id: int):
    return requests.get(f"https://api.brawlhalla.com/player/{brawl_id}/ranked", params={"api_key": API_TOKEN}).json()


def get_stats(brawl_id: int):
    return requests.get(f"https://api.brawlhalla.com/player/{brawl_id}/stats", params={"api_key": API_TOKEN}).json()


def main():
    # Bruce: 76561198306273971
    rankings = get_rankings("eichelbart")
    print(rankings)
    brawl_id = find_steam(76561198306273971)

    stats = get_stats(brawl_id)
    with open("stats.json", "w") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    ranked = get_ranked(brawl_id)
    with open("ranked.json", "w") as f:
        json.dump(ranked, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
