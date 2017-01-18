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

apis=["AIzaSyB5ztRJqq4qaPo6s-2-s3PTuO0bt1OAmCI",\
"AIzaSyDBS4E2IYOnzmhuwI-QcjBrDX5Z7tZyFvE","AIzaSyDt9UmAid642Wa5sa0VGHfeoYgXmBlj6ow",\
"AIzaSyC2Lu4B5thDJBxI_-xfbcoincN5AdFibuU","AIzaSyDVysasZ851z1f0K5uJt0NzrGJMOvYlgtM",\
"AIzaSyBeWbrSE2GqxWp_7P5ooI24hRIvoIUd77U","AIzaSyCM8oUqUzzXcK7y4obzRSZaZQUhfefDJ0U",\
"AIzaSyAatwEaqfIv2Te0KPmaeWLxESkkdQBVsh0","AIzaSyAatwEaqfIv2Te0KPmaeWLxESkkdQBVsh0",\
"AIzaSyAndvYsoGl0ryVsJReO27VYlqSD-ElZf6E","AIzaSyBPhXQQlIipVBxKW1DbgdrIpUSJLVCdw4o"]

cx_id='006837156905925461928:ini4xlggkhc'

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