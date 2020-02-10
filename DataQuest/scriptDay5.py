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