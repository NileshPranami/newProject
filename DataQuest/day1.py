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