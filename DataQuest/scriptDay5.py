artist_freq = {}
for item in moma:
    artist = item[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1

def artist_summary(name):
    count = artist_freq[name]
    print("There are {} artworks by {} in the data set".format(count,name))
artist_summary("Henri Matisse")

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for country in pop_millions:
    print("The population of {} is {:,.2f} million".format(country[0],country[1]))

import csv
frequency_tbl = {}
with open('artworks_clean.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        gender = row[5]
        if gender not in frequency_tbl:
            frequency_tbl[gender] = 1
        else:
            frequency_tbl[gender] +=1

for gen, val in frequency_tbl.items():
    print("There are {:,} artworks by {} artists".format(val,gen))