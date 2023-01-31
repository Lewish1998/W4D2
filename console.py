import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repo
import repositories.artist_repository as artist_repo
# ___________ ARTIST

# # artist_repo.delete_all()
# # artist_repo.delete(3)

artist_1 = Artist('Scarlxrd')
# artist_repo.save(artist_1)
# artist_2 = Artist('Eminem')
# artist_repo.save(artist_2)

# # Artist results
# results = artist_repo.select(3)



# __________ ALBUM
album_1 = Album('Rxse', 'Rap', artist_1)
album_repo.save(album_1)

pdb.set_trace()
