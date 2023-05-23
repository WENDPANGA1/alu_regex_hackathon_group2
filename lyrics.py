#!/usr/bin/python3

import re
# song lyrics string
input_string = "[Verse 1] Lift me up hold me down\n [Verse 2] keep me close safe and sound\n [Verse 3] Burning in a hope less dream hold me when you go to sleep"

#Regular expression pattern
pattern = '\[(Verse \d+)\] (.*?)'

# matches
matches = re.findall(pattern, input_string)

for match in matches:
    verse_label = match[0]
    lyrics = match[1]
    print(f"{verse_label}: {lyrics}")
