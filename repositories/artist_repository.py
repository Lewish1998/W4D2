from db.run_sql import run_sql
from repositories import album_repository
from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artist (name, id) VALUES (%s,%s) RETURNING *"
    values = [artist.name, artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():
    artists_list = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        album = album_repository.select(row["id"])
        artist = Artist (
            row['name'],
            row['id'],
            album
            )

        artists_list.append(artist)
    return artists_list