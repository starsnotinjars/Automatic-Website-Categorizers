# -*- coding: utf-8 -*-
import re
import sys
import common

def parse_keywords_from_file( filename ):
	lines2 = common.read_lines_from_file(filename)
	parsed=[]

	for line in lines2:
		values2 = re.split(',', line);
		#print (values2)
		for i in range(0,len(values2)):
			word=list(values2[i])
			if word[len(word)-1]=='$':
				word[len(word)-1]=','
				values2[i]=''.join(word)
			parsed.append(values2[i])

	return parsed

keys_ads = parse_keywords_from_file('ads2.txt')
# print (keys_ads)

keys_commerce = parse_keywords_from_file('commerce2.txt')

keys_search = parse_keywords_from_file('search2.txt')

keys_adult = parse_keywords_from_file('adult2.txt')

keys_news = parse_keywords_from_file('news2.txt')

keys_service = parse_keywords_from_file('service2.txt')

keys_platform = parse_keywords_from_file('platform2.txt')

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

count=0
on=0
on2=0
temp=[]

pin1 = open('output.txt','r')
lines1 = pin1.readlines();

target = open('output_from_search3.txt', 'w')

for line in lines1:

	values1 = re.split('\s+', line);
#	print (values1)

	if values1[1]=="'query':":

		target.write(str(values1[2]))

		on=1
		count=0

	if on==1 and values1[1]=="'snippet':":

		on=2

	if on==2:

		for i in range(0, len(values1)):

			if values1[i]=="'title':":

				#print ("Temp",temp)
				nothing=1
###############

				for j in range(0, len(keys_ads)):

					for k in range(0, len(temp)):

						if temp[k]==keys_ads[j]:

							counts_ads[j]=counts_ads[j]+1
							target.write(' Ads ')
							nothing=0


###############

###############

				for j in range(0, len(keys_commerce)):

					for k in range(0, len(temp)):

						if temp[k]==keys_commerce[j]:

							counts_commerce[j]=counts_commerce[j]+1
							target.write(' Commerce ')
							nothing=0



###############

###############

				for j in range(0, len(keys_search)):

					for k in range(0, len(temp)):

						if temp[k]==keys_search[j]:

							counts_search[j]=counts_search[j]+1
							target.write(' Search ')
							nothing=0



###############

###############

				for j in range(0, len(keys_adult)):

					for k in range(0, len(temp)):

						if temp[k]==keys_adult[j]:

							counts_adult[j]=counts_adult[j]+1
							target.write(' Adult ')
							nothing=0



###############

###############

				for j in range(0, len(keys_news)):

					for k in range(0, len(temp)):

						if temp[k]==keys_news[j]:

							counts_news[j]=counts_news[j]+1
							target.write(' News')
							nothing=0



###############

###############

				for j in range(0, len(keys_service)):

					for k in range(0, len(temp)):

						if temp[k]==keys_service[j]:

							counts_service[j]=counts_service[j]+1
							target.write(' Service')
							nothing=0



###############

###############

				for j in range(0, len(keys_platform)):

					for k in range(0, len(temp)):

						if temp[k]==keys_platform[j]:

							counts_platform[j]=counts_platform[j]+1
							target.write(' Platform')
							nothing=0

				if nothing==1:
					target.write(' Nothing')

###############
				target.write("\n")
				on=0
				on2=0
				temp=[]
				break;

			if values1[i]!="'title':":

				# print (values1[i])
				temp.append(values1[i])

###############



###########################################################








