from db.run_sql import run_sql
from repositories import artist_repository
from models.artist import Artist
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (title, genre, artists, id) VALUES (%s,%s,%s,%s) RETURNING *"
    values = [album.title, album.genre, album.artists, album.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums_list = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row["id"])
        album = Album (
            row['title'],
            row['genre'],
            row['artists'],
            row['id'],
            artist
            )

        albums_list.append(album)
    return albums_list