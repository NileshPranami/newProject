artist_freq = {}
for item in moma:
    artist = item[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1