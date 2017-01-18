#!/usr/bin/env python
import nltk
from  nltk import * 

def filter_bigram(tex):
	tokens = nltk.word_tokenize(tex)

	pairs = [ " ".join(pair) for pair in nltk.bigrams(tokens)]
	
	for pair in nltk.bigrams(tokens):
		
		print pair
	return pairs 

def sentence_split(tex):
	sents=nltk.sent_tokenize(tex)
	print sents
	t=[]
	
	for i in sents:
		t.extend(filter_bigram(i))
	return t

tex= "Sergio Ramos is horrible . Spain's fan following is still incredible "

# print filter_bigram(tex)
print nltk.pos_tag(tex)
print filter_bigram(tex)
# print sentence_split(tex)

# tokens = nltk.word_tokenize(sentence)
# pairs = [ " ".join(pair) for pair in nltk.bigrams(tokens)]