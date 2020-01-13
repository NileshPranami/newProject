from csv import reader

opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
mona = list(read_file)
mona = mona[1:]

for row in moma:
    birth_date = row[3]
    if birth_date!= "":
        birth_date = int(birth_date)
    row[3] = birth_date

for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

ages = []

for row in moma:
    date = row[6]
    birth = row[3]
    age = 0
    if type(birth) is int:
        age = date - birth

    ages.append(age)

final_ages = []
for age in ages:
    if age > 20:
        final_ages.append(age)
    else:
        final_ages.append("Unknown")