import nltk
import json
import pymongo
import hashlib 
import spotlight 
import time
from pymongo import MongoClient
from apiclient.discovery import build

apis=[]
cx_id=''

def custom_search(dkey,cx_id,your_search):
	
	service = build("customsearch", "v1",
	               developerKey=dkey)
	res = service.cse().list(
	    q=your_search,
	    cx=cx_id,
	    searchType='image',
	    num=10,
	    # imgType='clipart',
	    imgSize='medium',
	    # fileType='png',
	    safe= 'off'
	).execute()

	links=[]
	
	if not 'items' in res:
		pass# print 'No result !!\nres is: {}'.format(res)
	else:
		for item in res['items']:
			links.append(item['link'])
	time.sleep(1)
	return links        


client=MongoClient()
client =MongoClient('mongodb://')
db=client.links 
collection=db.db_nltk
encount=0
kcount=0
final=[]
kfinal=[]

for x in collection.find():
	encount+=len(x['Named Entities'])
	kcount+=len(x['Key words'])
	final.extend(x['Named Entities'])
	kfinal.extend(x['Key words'])
# print encount
# print kcount
# len1 =len(list(set(final)))
# print len1
# len2 =len(list(set(kfinal)))
# print len2

final =list(set(final))
kfinal=list(set(kfinal))
dub=final+kfinal
db1=client.links
collection1=db1.imgurls

for i in range(139,len(dub)):
	try :
		x=custom_search(apis[i%11],cx_id,dub[i])
		data = {"named entities":dub[i],"urls":x}
		collection1.insert_one(data)
	except :
		pass

# x=[custom_search(apis[i%10],cx_id,dub[i]) for i in range(len(dub))]
# # t=zip(final,x)
# t=0
# data = [{"named entities":dub[i],"urls":x[i]} for i in range(len(dub)) ]
# collection1.insert_many(data)


