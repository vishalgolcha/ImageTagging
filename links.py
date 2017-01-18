import time
import json
import pymongo
from pymongo import MongoClient
from clarifai.client import ClarifaiApi

cf=ClarifaiApi()

client =MongoClient('mongodb://digi1:digi1234@52.21.107.21:27017')

db=client.links 
collection=db.cumulative
fin=[]
cnt=0

tabs=db.clari2

for x in collection.find():
	
	y=x['Image']
	y=y.split("<__>")
	for g in y :
		if(g!=""):
			
			tag=[]
			fin.append(g)
			cnt+=1
			
			if cnt>=114 and cnt<= 900 :
				# cnt+=1
				res=(cf.tag_image_urls(g))
				
				for i in range( len(res['results'][0]['result']['tag']['classes']) ) :
					if res['results'][0]['result']['tag']['probs'][i]>=0.7 :
						tag.append(res['results'][0]['result']['tag']['classes'][i])
				
				# result = collection.update_one()
 				
 				lit=x['Named Entities & Keywords']
				
				dic={}
				dic["link"]=g
				dic["tags 70"]=tag
				
				tag=[]
				for i in range( len(res['results'][0]['result']['tag']['classes'])) :
					if res['results'][0]['result']['tag']['probs'][i]>=0.9 :
						tag.append(res['results'][0]['result']['tag']['classes'][i])

						
				dic["tags 90"]=tag
				dic["NE&K's"]=lit
				
				if type(tag[0])==list :
					tag=tag[0]

				inter=list( set(tag) & set(lit) )


				dic["list intersect"]=inter
				# if cnt<=102 :
				# 	print tag
				# 	print type(tag)
				# 	print lit
				# 	print type(lit)
				# 	print (set(tag) & set(lit))
				# 	print inter 

				tabs.insert_one(dic)
				time.sleep(1)
print len(fin)
# print len(result)





