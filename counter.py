import nltk
import json
import pymongo
import hashlib 
import spotlight 
import time
from pymongo import MongoClient
from apiclient.discovery import build

apis=["AIzaSyB5ztRJqq4qaPo6s-2-s3PTuO0bt1OAmCI",\
"AIzaSyDBS4E2IYOnzmhuwI-QcjBrDX5Z7tZyFvE","AIzaSyDt9UmAid642Wa5sa0VGHfeoYgXmBlj6ow",\
"AIzaSyC2Lu4B5thDJBxI_-xfbcoincN5AdFibuU","AIzaSyDVysasZ851z1f0K5uJt0NzrGJMOvYlgtM",\
"AIzaSyBeWbrSE2GqxWp_7P5ooI24hRIvoIUd77U","AIzaSyCM8oUqUzzXcK7y4obzRSZaZQUhfefDJ0U",\
"AIzaSyAatwEaqfIv2Te0KPmaeWLxESkkdQBVsh0","AIzaSyAatwEaqfIv2Te0KPmaeWLxESkkdQBVsh0",\
"AIzaSyAndvYsoGl0ryVsJReO27VYlqSD-ElZf6E","AIzaSyBPhXQQlIipVBxKW1DbgdrIpUSJLVCdw4o"]
cx_id='006837156905925461928:ini4xlggkhc'

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
client =MongoClient('mongodb://digi1:digi1234@52.21.107.21:27017')
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


