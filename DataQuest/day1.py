for n in moma:
    gender = n[5].title()
    n[5] = gender
    if not gender:
        n[5] = "Gender Unknown/Other"

    nationality = n[2].title()
    n[2] = nationality
    if not nationality:
        n[2] = "Nationality Unknown"
