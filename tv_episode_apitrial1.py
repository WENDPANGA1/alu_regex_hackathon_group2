import re
import requests

response = requests.get('https://api.tvmaze.com/shows')

if response.status_code == 200:
    api_data = response.json()
    for item in api_data:
        match = re.match(r'^(.+)\sS(\d{2})E(\d{2}): (.+)$', item['TV Episode Titles'])
        if match:
            show_name = match.group(1)
            season_number = match.group(2)
            episode_number = match.group(3)
            episode_title = match.group(4)

            print("Show Name:", show_name)
            print("Season Number:", season_number)
            print("Episode Number:", episode_number)
            print("Episode Title:", episode_title)
else:
    print("API request failed with status code:", response.status_code)

