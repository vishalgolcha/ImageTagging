from apiclient.discovery import build
import urllib
import csv
import time

names=[]

with open('olympics.csv','rb') as csvfile:
    csvreader = csv.reader(csvfile)
    # output_fil = open('output.txt', 'ab')
    for row in csvreader:
        for elem in row:
        	names.append(str(elem))
        # print result
        # output_fil.writelines(str(result))

apis=[]

cx_id=''

def serch(que,ap):
	links=[]

	service = build("customsearch", "v1",
	               developerKey=ap)
	
	res = service.cse().list(
	    q=que+' olympics',
	    cx=cx_id,
	    searchType='image',
	    num=5,
	    # imgType='clipart',
	    # imgSize='medium',
	    # fileType='jpg',
	    rights='cc_publicdomain',
	    safe= 'off'
	).execute()

	if not 'items' in res:
	    print 'No result !!\nres is: {}'.format(res)
	else:
	    for item in res['items']:
	        # print('{}:\n\t{}'.format(item['title'].encode('utf-8'), item['link']))
	        links.append(item['link'])
	time.sleep(1)
	return links 

# count=len(names[i])*5;
# print names 

for j in range(len(names)):
	try:
		t=serch(names[j],apis[j%11])
		for i in range (len(t)):	
			xyz=str(i%5)

			urllib.urlretrieve(t[i],names[j]+xyz+t[i][-5:])
			# print t[i]
			# print names[j]+xyz+".jpg"
	except:
		pass