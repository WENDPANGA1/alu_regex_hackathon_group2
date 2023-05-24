import re

def match_isbn_number():
    # ISBN numbers: "ISBN xxx-x-xxx-xxxxx-x"
    isbn_pattern = r"ISBN \d{3}-\d-\d{3}-\d{5}-\d"

    # Get user input
    input_string = input("Enter an ISBN number: ")

    # Match against the regular expression pattern
    isbn_match = re.match(isbn_pattern, input_string)

    if isbn_match:
        isbn_number = isbn_match.group()
        print("Valid ISBN Number:", isbn_number)
    else:
        print("Invalid ISBN Number")

# Call the function
match_isbn_number()
