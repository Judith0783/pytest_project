
from lib.report_length import *

def report_the_number_of_characters():
    result = report_length("welcome")
    assert result == "This string was 7 characters long."







"""def report_length(str):
    length = len(str)
    return f"This string was {length} characters long."


report the number of characters of str,
save that number of characters in a variable
return "This string was {length} characters long."
"""