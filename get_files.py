import sys
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
AOC_TOKEN = os.environ.get("AOC_TOKEN")
session, token = AOC_TOKEN.split("=")
cookies = {session: token}


def fetch_day_file(day: int, year: int = 2024):
    if Path(f"{year}-{day}.txt").exists():
        return
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies=cookies,
    )
    print(response.status_code)
    response.raise_for_status()

    with open(f"{year}-{day}.txt", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    day, year = sys.argv[1], 2024
    if len(sys.argv) > 2:
        year = sys.argv[2]
    fetch_day_file(int(day), int(year))
