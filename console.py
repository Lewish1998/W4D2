import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repo
import repositories.artist_repository as artist_repo

artist_1 = Artist('Scarlxrd')
artist_repo.save(artist_1)

artist_2 = Artist('Eminem')
artist_repo.save(artist_2)

# Artist results
results = artist_repo.select_all()

pdb.set_trace()