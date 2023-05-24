#!/usr/bin/python3

import re

# Jokes string
input_string = "Why did the chicken cross the road? Because it wanted to get to the other side."

# Regular expression pattern for jokes
pattern = r"Why did the .*? \? Because.*"

# Matches
matches = re.findall(pattern, input_string)

if matches:
    for match in matches:
        print("Found a joke: " + match)
else:
    print("No jokes found in the text.")

