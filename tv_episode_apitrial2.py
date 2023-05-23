import re
import requests

api_key = 'my_api_key'
search_engine_id = 'my_search_engine_id'

query = 'TV Shows'

url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}'
response = requests.get(url)

if response.status_code == 200:
    api_data = response.json()

    for item in api_data['items']:
        title = item['TV Episode Titles']
        link = item['link']
        snippet = item['snippet']

        match = re.match(r'^(.+)\sS(\d{2})E(\d{2}): (.+)$', TV Episode Titles)
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
            print("No match found.")
else:
    print("API request failed with status code:", response.status_code)

