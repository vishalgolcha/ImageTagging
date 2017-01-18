from instagram.client import InstagramAPI
id=''
sec=''
api= InstagramAPI(client_id=id,client_secret=sec)
popular_media=api.media_popular(count=20)
for media in popular_media:
	print media.images['standard_resolution'].url