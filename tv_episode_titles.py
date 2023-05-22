import re

pattern = r'^(.+)\sS(\d{2})E(\d{2}): (.+)$'
string = "Sistas S06E02: Full Circle Moments"

match = re.match(pattern, string)
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

