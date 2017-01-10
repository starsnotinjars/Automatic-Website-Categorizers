import json
import gspread
import re
import time
from oauth2client.client import SignedJwtAssertionCredentials
import random

json_key = json.load(open('creds.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("title_scraper").sheet1 # open sheet

# all_cells = sheet.range('D2:D10')

# for cell in all_cells:
#	print cell.value

keys_ads=['remove','ad','ads','virus','advertising', 'pop-up', 'pop-ups','Remove','Ad','Ads','Virus','Advertising', 'Pop-up', 'Pop-ups']

keys_commerce=['buy', 'shop', 'shopping', 'buyers', 'sellers', 'online-store', 'online-marketplace', 'commerce', 'e-commerce','import','imports','export','exports','Buy', 'Shop', 'Shopping', 'Buyers', 'Sellers', 'Online-store', 'Online-marketplace', 'Commerce', 'E-commerce','Import', 'Imports', 'Export', 'Exports']

keys_search=['search', 'search-engine','searching','searches','Search','Search-engine','Searching','Searches']

keys_adult=['adult', 'sex', 'uncensored', 'adult content', '18+','Adult', 'Sex', 'Uncensored', 'Adult content','Adult Content']

keys_news=['news','weather', 'latest stories']

keys_service=['service','services','Service','Services']

keys_platform=['post', 'share', 'weblog', 'blog', 'online social community','social media','social-networking','social networking','Post', 'Share', 'Weblog', 'Blog', 'Online social community','Social media','Social-networking','Social networking','Online Social Community','Social Media','Social-Networking','Social Networking']



for a in range(278,2000):

	try:

		sheet.update_acell('A2:A101', sheet.acell('F'+str(a-1)).value)

		time.sleep(16)
        	time.sleep(10*random.random())

#	while sheet.acell('G2').value=='#N/A':

#		time.sleep(10)

		counts_ads=[]

		counts_commerce=[]

		counts_search=[]

		counts_adult=[]

		counts_news=[]

		counts_service=[]

		counts_platform=[]

		for z in range(0, len(keys_ads)):

			counts_ads.append(0)

		for z in range(0, len(keys_commerce)):

			counts_commerce.append(0)

		for z in range(0, len(keys_search)):

			counts_search.append(0)

		for z in range(0, len(keys_adult)):

			counts_adult.append(0)

		for z in range(0, len(keys_news)):

			counts_news.append(0)

		for z in range(0, len(keys_service)):

			counts_service.append(0)

		for z in range(0, len(keys_platform)):

			counts_platform.append(0)


	#print len(counts_ads)
	#print len(counts_commerce)
	#print len(counts_search)
	#print len(counts_adult)
	#print len(counts_news)
	#print len(counts_service)
	#print len(counts_platform)

####################################################

		for i in range(2,12):

			val=sheet.acell('G'+str(i)).value
			split_val=re.split('\s+', val)

		# print val, "value"

			for j in range(0, len(keys_ads)):

				for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_ads[j], "key"

					if split_val[k]==keys_ads[j]:

					# print split_val[k],keys_ads[j]

						counts_ads[j]=counts_ads[j]+1

		# print counts_ads, "int counts_ads"

		for l in range(0, len(counts_ads)):

			if counts_ads[l] >=1:

				sheet.update_acell('H'+str(a-1), 'Ads')

				# print a

				# break;

###########################################################

####################################################

		for i in range(2,12):

			val=sheet.acell('G'+str(i)).value
			split_val=re.split('\s+', val)

		# print val, "value"

			for j in range(0, len(keys_commerce)):

				for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_commerce[j], "key"

					if split_val[k]==keys_commerce[j]:

					# print split_val[k],keys_commerce[j]

						counts_commerce[j]=counts_commerce[j]+1

		# print counts_commerce, "int counts_commerce"

		for l in range(0, len(counts_commerce)):

			if counts_commerce[l] >=1:

				sheet.update_acell('H'+str(a-1), 'Commerce')

				# print a

				# break;

###########################################################

####################################################

		for i in range(2,12):

			val=sheet.acell('G'+str(i)).value
			split_val=re.split('\s+', val)

		# print val, "value"

			for j in range(0, len(keys_search)):

				for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_search[j], "key"

					if split_val[k]==keys_search[j]:

					# print split_val[k],keys_search[j]

						counts_search[j]=counts_search[j]+1

		# print counts_search, "int counts_search"

		for l in range(0, len(counts_search)):

			if counts_search[l] >=1:

				sheet.update_acell('H'+str(a-1), 'Search')

				# print a

				# break;

###########################################################

####################################################

		for i in range(2,12):

			val=sheet.acell('G'+str(i)).value
			split_val=re.split('\s+', val)

		# print val, "value"

			for j in range(0, len(keys_adult)):

				for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_adult[j], "key"

					if split_val[k]==keys_adult[j]:

					# print split_val[k],keys_adult[j]

						counts_adult[j]=counts_adult[j]+1

		# print counts_adult, "int counts_adult"

		for l in range(0, len(counts_adult)):

			if counts_adult[l] >=1:

				sheet.update_acell('H'+str(a-1), 'Adult')

				# print a

				# break;

###########################################################

####################################################

		for i in range(2,12):

			val=sheet.acell('G'+str(i)).value
			split_val=re.split('\s+', val)

		# print val, "value"

			for j in range(0, len(keys_news)):

				for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_news[j], "key"

					if split_val[k]==keys_news[j]:

					# print split_val[k],keys_news[j]

						counts_news[j]=counts_news[j]+1

		# print counts_news, "int counts_news"

		for l in range(0, len(counts_news)):

			if counts_news[l] >=1:

				sheet.update_acell('H'+str(a-1), 'News')

				# print a

				# break;

###########################################################

####################################################

		for i in range(2,12):

			val=sheet.acell('G'+str(i)).value
			split_val=re.split('\s+', val)

		# print val, "value"

			for j in range(0, len(keys_service)):

				for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_service[j], "key"

					if split_val[k]==keys_service[j]:

					# print split_val[k],keys_service[j]

						counts_service[j]=counts_service[j]+1

		# print counts_service, "int counts_service"

		for l in range(0, len(counts_service)):

			if counts_service[l] >=1:

				sheet.update_acell('H'+str(a-1), 'Service')

				# print a

				# break;

###########################################################

####################################################

		for i in range(2,12):

			val=sheet.acell('G'+str(i)).value
			split_val=re.split('\s+', val)

		# print val, "value"

			for j in range(0, len(keys_platform)):

				for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_platform[j], "key"

					if split_val[k]==keys_platform[j]:

					# print split_val[k],keys_platform[j]

						counts_platform[j]=counts_platform[j]+1

		# print counts_platform, "int counts_platform"

		for l in range(0, len(counts_platform)):

			if counts_platform[l] >=1:

				sheet.update_acell('H'+str(a-1), 'Platform')

				# print a

				# break;

###########################################################

		final_counts=[counts_ads,counts_commerce,counts_search,counts_adult,counts_news,counts_service,counts_platform]
		sheet.update_acell('I'+str(a-1),final_counts)

	except:

		pass
				
	
	






