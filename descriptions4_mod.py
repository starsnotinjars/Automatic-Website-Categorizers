import json
import gspread
import re
import time
from oauth2client.client import SignedJwtAssertionCredentials
import random

keys_ads=['remove','ad','ads','virus','advertising', 'pop-up', 'pop-ups','Remove','Ad','Ads','Virus','Advertising', 'Pop-up', 'Pop-ups','remove.','ad.','ads.','virus.','advertising.', 'pop-up.', 'pop-ups.','Remove.','Ad.','Ads.','Virus.','Advertising.', 'Pop-up.', 'Pop-ups.'
'remove,','ad,','ads,','virus,','advertising,', 'pop-up,', 'pop-ups,','Remove,','Ad,','Ads,','Virus,','Advertising,', 'Pop-up,', 'Pop-ups,']

keys_commerce=['buy', 'shop', 'shopping', 'buyers', 'sellers', 'online-store', 'online-marketplace', 'commerce', 'e-commerce','import','imports','export','exports','Buy', 'Shop', 'Shopping', 'Buyers', 'Sellers', 'Online-store', 'Online-marketplace', 'Commerce', 'E-commerce','Import', 'Imports', 'Export', 'Exports','buy.', 'shop.', 'shopping.', 'buyers.', 'sellers.', 'online-store.', 'online-marketplace.', 'commerce.', 'e-commerce.','import.','imports.','export.','exports.','Buy.', 'Shop.', 'Shopping.', 'Buyers.', 'Sellers.', 'Online-store.', 'Online-marketplace.', 'Commerce.', 'E-commerce.','Import.', 'Imports.', 'Export.', 'Exports.','buy,', 'shop,', 'shopping,', 'buyers,', 'sellers,', 'online-store,', 'online-marketplace,', 'commerce,', 'e-commerce,','import,','imports,','export,','exports,','Buy,', 'Shop,', 'Shopping,', 'Buyers,', 'Sellers,', 'Online-store,', 'Online-marketplace,', 'Commerce,', 'E-commerce,','Import,', 'Imports,', 'Export,', 'Exports,', 'marketplace', 'Marketplace','marketplace.','Marketplace.','marketplace,','Marketplace,']

keys_search=['search', 'search-engine','searching','searches','Search','Search-engine','Searching','Searches','search.', 'search-engine.','searching.','searches.','Search.','Search-engine.','Searching.','Searches.','search,', 'search-engine,','searching,','searches,','Search,','Search-engine,','Searching,','Searches,']

keys_adult=['adult', 'sex', 'uncensored', 'adult content', '18+','Adult', 'Sex', 'Uncensored', 'Adult content','Adult Content','adult.', 'sex.', 'uncensored.', 'adult content.', '18+.','Adult.', 'Sex.', 'Uncensored.', 'Adult content.','Adult Content.','adult,', 'sex,', 'uncensored,', 'adult content,', '18+,','Adult,', 'Sex,', 'Uncensored,', 'Adult content,','Adult Content,']

keys_news=['news','weather', 'latest stories','news.','weather.', 'latest stories.','news,','weather,', 'latest stories,']

keys_service=['service','services','Service','Services','service.','services.','Service.','Services.','service,','services,','Service,','Services,']

keys_platform=['post', 'share', 'weblog', 'blog', 'online social community','social media','social-networking','social networking','Post', 'Share', 'Weblog', 'Blog', 'Online social community','Social media','Social-networking','Social networking','Online Social Community','Social Media','Social-Networking','Social Networking','post.', 'share.', 'weblog.', 'blog.', 'online social community.','social media.','social-networking.','social networking.','Post.', 'Share.', 'Weblog.', 'Blog.', 'Online social community.','Social media.','Social-networking.','Social networking.','Online Social Community.','Social Media.','Social-Networking.','Social Networking.','post,', 'share,', 'weblog,', 'blog,', 'online social community,','social media,','social-networking,','social networking,','Post,', 'Share,', 'Weblog,', 'Blog,', 'Online social community,','Social media,','Social-networking,','Social networking,','Online Social Community,','Social Media,','Social-Networking,','Social Networking,','platform','Platform','platform.','Platform.','platform,','Platform,']

pin1 = open('translated.txt','r')
lines1 = pin1.readlines();
translated=[]

for line in lines1: 

	values1 = re.split('\n', line);

	translated.append(values1)

for a in range(0, len(translated)):

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
		# print translated[a]

		split_val=re.split('\s+', translated[a][0])

		if translated[a][0] == '#N/A':
          		continue

######################################

		for j in range(0, len(keys_ads)):

			for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_ads[j], "key"

				if split_val[k]==keys_ads[j]:

					# print split_val[k],keys_ads[j]

					counts_ads[j]=counts_ads[j]+1

		# print counts_ads, "int counts_ads"

###########################################################

####################################################


		for j in range(0, len(keys_commerce)):

			for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_commerce[j], "key"

				if split_val[k]==keys_commerce[j]:

					# print split_val[k],keys_commerce[j]

					counts_commerce[j]=counts_commerce[j]+1

		# print counts_commerce, "int counts_commerce"


###########################################################

####################################################


		for j in range(0, len(keys_search)):

			for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_search[j], "key"

				if split_val[k]==keys_search[j]:

					# print split_val[k],keys_search[j]

					counts_search[j]=counts_search[j]+1

		# print counts_search, "int counts_search"

###########################################################

####################################################


		for j in range(0, len(keys_adult)):

			for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_adult[j], "key"

				if split_val[k]==keys_adult[j]:

					# print split_val[k],keys_adult[j]

					counts_adult[j]=counts_adult[j]+1

		# print counts_adult, "int counts_adult"

###########################################################

####################################################


		for j in range(0, len(keys_news)):

			for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_news[j], "key"

				if split_val[k]==keys_news[j]:

					# print split_val[k],keys_news[j]

					counts_news[j]=counts_news[j]+1

		# print counts_news, "int counts_news"

###########################################################

####################################################


		for j in range(0, len(keys_service)):

			for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_service[j], "key"

				if split_val[k]==keys_service[j]:

					# print split_val[k],keys_service[j]

					counts_service[j]=counts_service[j]+1

		# print counts_service, "int counts_service"

###########################################################

####################################################


		for j in range(0, len(keys_platform)):

			for k in range(0, len(split_val)):

				# print split_val[k], "split"

				# print keys_platform[j], "key"

				if split_val[k]==keys_platform[j]:

					# print split_val[k],keys_platform[j]

					counts_platform[j]=counts_platform[j]+1

		# print counts_platform, "int counts_platform"

###########################################################

		flagged=0

		for l in range(0, len(counts_news)):

			if counts_news[l] >=1 and flagged!=1:

				print translated[a],'News'
				flagged=1

		for l in range(0, len(counts_ads)):

			if counts_ads[l] >=1 and flagged!=1:

				print translated[a],'Ads'
				flagged=1

		for l in range(0, len(counts_commerce)):

			if counts_commerce[l] >=1 and flagged!=1:

				print translated[a],'Commerce'
				flagged=1

		for l in range(0, len(counts_search)):

			if counts_search[l] >=1 and flagged!=1:

				print translated[a],'Search'
				flagged=1

		for l in range(0, len(counts_adult)):

			if counts_adult[l] >=1 and flagged!=1:

				print translated[a],'Adult'
				flagged=1

		for l in range(0, len(counts_service)):

			if counts_service[l] >=1 and flagged!=1:

				print translated[a],'Service'
				flagged=1

		for l in range(0, len(counts_platform)):

			if counts_platform[l] >=1 and flagged!=1:

				print translated[a],'Platform'
				flagged=1

		if flagged==0:
			print translated[a],'Nothing'
