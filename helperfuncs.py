from movieutils import *

def strip_whitespace_from_title(title):
    title = title.replace(" ", "+")
    return title

def is_valid_year(year):
    if year.isdigit():
        if int(year) >=1900 and int(year) <=2020:
            return str(year)
    else:
        return False
