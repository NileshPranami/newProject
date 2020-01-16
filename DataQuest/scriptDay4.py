decade_frequency = {}
for item in decades:
    if item not in decade_frequency:
        decade_frequency[item] = 1
    else:
        decade_frequency[item] += 1

artist = "Pablo Picasso"
birth_year = 1881

output = "{0}'s birth year is {1}".format(artist,birth_year)
print(output)