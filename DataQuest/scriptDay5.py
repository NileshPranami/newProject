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