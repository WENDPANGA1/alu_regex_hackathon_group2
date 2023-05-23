import re

def match_twitter_handle():
    # Twitter Usernames: "@username"
    twitter_pattern = r"@(\w+)"

    # Get user input
    input_string = input("Enter a Twitter handle: ")

    # Match against the regular expression pattern
    twitter_match = re.match(twitter_pattern, input_string)

    if twitter_match:
        username = twitter_match.group(1)
        print("Valid Twitter Username:", username)
    else:
        print("Invalid Twitter Username")

# Call the function
match_twitter_handle()
