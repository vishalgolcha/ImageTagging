import nltk
from nltk import ngrams
import json
import pymongo
from pymongo import MongoClient
import spotlight 

def ngramize(tclip,n):
	n_grams = ngrams(tclip.split(), n)
	f=[e for e in n_grams]	
	return f

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

	return list(set(b))

def get_keywords(sample):
	sentences = nltk.sent_tokenize(sample)
	tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
	# print tokenized_sentences 
	tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
	# print tagged_sentences
	filt=['NN','NNP','NNS','FW']
	d= [extra[i][0] for extra in tagged_sentences for i in range(len(extra)) if extra[i][1] in filt ]
	return list(set(d))

def  get_descriptors(sample):
	sentences = nltk.sent_tokenize(sample)
	tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
	# print tokenized_sentences 
	tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
	# print tagged_sentences
	filt=['VB','VB','JJ','RB','JJR','VBD','VBG','VBN','VBP','VBZ']
	d= [extra[i][0] for extra in tagged_sentences for i in range(len(extra)) if extra[i][1] in filt ]
	return list(set(d))
 

def get_entity(sample):
	sentences = nltk.sent_tokenize(sample)
	tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
	# print tokenized_sentences 
	tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
	# print tagged_sentences
	chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

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
	    entity_names.extend(extract_entity_names(tree))
	x=set(entity_names)
	# for y in x 
	return list(x)


# client=MongoClient()
client =MongoClient('mongodb://')
db=client.links 
collection=db.toi_feed
word="gistai"

tags=db.cumulative
for x in collection.find():
	for y in range(len(x['VisualData'])):
		# if x['VisualData'][y]['vsrc'].count(word)==2 :
			
		i=x['VisualData'][y]
		# upd=[ngramize(i['dtext'][],2)]
		val_ins={"Text":i['dtext'],"Image":i['vsrc'], \
		"Named Entities & Keywords":list(set(get_more_entities(i['dtext'])+get_keywords(i['dtext']))) , \
		"bi-grams":ngramize(i['dtext'],2),"tri-grams":ngramize(i['dtext'],3)
		}
		
		tags.insert_one(val_ins)			
