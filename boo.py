import simplejson
import httplib2
import sys
from instagram.client import InstagramAPI
i=''
sec=''
api= InstagramAPI(client_id=i,client_secret=sec)
popular_media=api.recent_media(count=1)
print popular_media
