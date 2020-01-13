for n in moma:
    gender = n[5].title()
    n[5] = gender
    if not gender:
        n[5] = "Gender Unknown/Other"

    nationality = n[2].title()
    n[2] = nationality
    if not nationality:
        n[2] = "Nationality Unknown"


def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for item in moma:
    value1 = clean_and_convert(item[3])
    value2 = clean_and_convert(item[4])
    item[3] = value1
    item[4] = value2


test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = []

for date in test_data:
    date = strip_characters(str(date))
    stripped_test_data.append((date))

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(", ")", "c", "C", ".", "s", "'", " "]


def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, "")
    return string


stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']


def process_date(string):
    if "-" in string:
        split_date = string.split("-")
        date_one = int(split_date[0])
        date_two = int(split_date[1])
        avg_date = round((date_one + date_two) / 2)
        return avg_date

    else:
        return int(string)


processed_test_data = []
for item in test_data:
    striped = strip_characters(item)
    processed = int(process_date(striped))
    processed_test_data.append(processed)

for item in moma:
    value = process_date(strip_characters(item[6]))
    item[6] = int(value)