def make_album(title, artist):
	return {"title": title, "artist": artist}


def get_album(title, artist):
	return make_album(title, artist)


album = get_album("The Dark Side of the Moon", "Pink Floyd")
print(album)

album1 = make_album("Abbey Road", "The Beatles")
print(album1)

ma = make_album
album2 = ma("Back in Black", "AC/DC")
print(album2)

album3 = ma("Thriller", "Michael Jackson")
print(album3)

ma, ga = make_album, get_album
album4 = ma("Rumours", "Fleetwood Mac")
print(album4)
