
#!/usr/bin/env python
import nltk
import json
import pymongo
import hashlib 
import spotlight 
from pymongo import MongoClient

def get_more_entities(sample):
	a=get_keywords(sample)
	b=get_entity(sample)
	c=list(set(a)^set(b))
	more=[]
	for i in range(len(c)):
		try :
			annotations = spotlight.annotate('http://spotlight.sztaki.hu:2222/rest/annotate',\
				c[i],confidence=0.4,support=20,spotter='Default')
			# print annotations
			b.append(c[i])
		except :
			pass

	return b

def get_keywords(sample):
	sentences = nltk.sent_tokenize(sample)
	tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
	# print tokenized_sentences 
	tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
	# print tagged_sentences
	filt=['NN','NNP','NNS','FW']
	d= [extra[i][0] for extra in tagged_sentences for i in range(len(extra)) if extra[i][1] in filt ]
	return list(set(d))

def get_entity(sample):
	sentences = nltk.sent_tokenize(sample)
	tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
	# print tokenized_sentences 
	tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
	# print tagged_sentences
	chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
	# print chunked_sentences

	# tags=['NN','NNP','NNS','FW']
	# d= [extra[i][0] for extra in tagged_sentences for i in range(len(extra)) if extra[i][1] in tags ]
	# keywords.extend(list(set(d)))
	def extract_entity_names(t):
	    entity_names = []

	    if hasattr(t, 'label') and t.label:
	        if t.label()=='NE':
	            entity_names.append(' '.join([child[0] for child in t]))
	        else:
	            for child in t:
	                entity_names.extend(extract_entity_names(child))

	    return entity_names

	entity_names = []

	for tree in chunked_sentences:
	    # Print results per sentence
	    # print extract_entity_names(tree)
	    entity_names.extend(extract_entity_names(tree))

	# Print all entity names
	# print entity_names

	# Print unique entity names
	x=set(entity_names)
	# for y in x 
	return list(x)


client=MongoClient()
client =MongoClient('mongodb://')
db=client.links 
collection=db.toi_feed
# print collection.count()
# print db.collection_names(include_system_collections=False)

word="gistai"
t= collection.find_one( {"id": "52651186"})#.pretty()
# data=[ x['VisualData'][y] for x in collection.find() for y in range(len(x['VisualData'])) if x['VisualData'][y]['vsrc'].count(word)==2]

# val_ins=[ {"Text":i['dtext'],"Image":i['vsrc'],"Named Entities":get_more_entities(i['dtext']),"Key words":get_keywords(i['dtext'])} for i in data ]
for x in collection.find():
	for y in range(len(x['VisualData'])):
		if x['VisualData'][y]['vsrc'].count(word)==2 :
			
			i=x['VisualData'][y]

			val_ins={"Text":i['dtext'],"Image":i['vsrc'], \
			"Named Entities":get_more_entities(i['dtext']),"Key words":get_keywords(i['dtext'])} ]

			tags_2.insert_one(val_ins)			


# .insert_many(val_ins)

tags=db.tags_2
# tags_2.insert_many(val_ins)

print len(val_ins)
print len(data)

#print 
#db.toi_names(include_system_collections=False)


