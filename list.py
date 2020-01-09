from csv import reader

opened_file = open('artworks.csv', encoding="utf8")

read_file = reader(opened_file)

artwork = list(read_file)

artwork = artwork[1:]

print(artwork)