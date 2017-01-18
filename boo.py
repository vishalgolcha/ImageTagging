import simplejson
import httplib2
import sys
from instagram.client import InstagramAPI
i='0021b9fcc4844715b0baa79d30629303'
sec='68f1636cc02348b6b46a401500ab6722'
api= InstagramAPI(client_id=i,client_secret=sec)
popular_media=api.recent_media(count=1)
print popular_media
